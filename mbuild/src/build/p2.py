import os
import m2
import error_messages
import p2_naming

class ProjectPluginError(ValueError): pass
class ProjectError(ValueError): pass
class DimensionError(ProjectError): pass

def get_plugin_environment():
	env = {'ActionSpec': ActionSpec,
	       'BuildConfiguration': BuildConfiguration,
	       'ProjectStyle': ProjectStyle}
	env.update(p2_naming.get_environment())
	return env

def get_plugin_pattern():
	return "*.p2_plugin"

class BuildConfiguration(object):
	def __init__(self, dimensions, is_valid):
		self._dimensions = dimensions
		self._is_valid = is_valid
	
	def get_dimensions(self):
		return self._dimensions
	
	def is_valid(self, configuration):
		return self._is_valid(configuration)

class ProjectSpec(object):
	def __init__(self, actions, depends, build_configuration):
		self._style = actions
		self._depends = depends
		self._build_configuration = build_configuration
	
	def get_actions(self):
		return self._style.get_actions()
	
	def get_identifier(self, configuration, exclude_dimensions):
		all_dims = self._style.order_dimensions(configuration.keys())
		dims = [d for d in all_dims if not d in exclude_dimensions]
		return "_".join([configuration[d] for d in dims])
	
	def get_depends(self):
		return self._depends
	
	def get_build_configuration(self):
		return self._build_configuration

class ProjectStyle(object):
	def __init__(self, actions, order_dimension_fn):
		self._actions = actions
		self._order_dimension_fn = order_dimension_fn
	
	def get_actions(self):
		return self._actions
	
	def order_dimensions(self, dimensions):
		return self._order_dimension_fn(dimensions)

class ActionSpec(object):
	def __init__(self, name_structure):
		self._name_structure = name_structure
	
	def get_name(self, manifest, project, configuration):
		return [n.expand(configuration, manifest, project) for n in self._name_structure(project.get_dimensions())]
	
	def get_dimension_dependencies(self, all_dimensions):
		return [n.get_dimension_dependencies() for n in self._name_structure(all_dimensions)]

class ProjectLoader(object):
	def __init__(self, manifest, plugin_manager, force_dimensions={}):
		self._manifest = manifest
		self._plugin_manager = plugin_manager
		self._force_dimensions = force_dimensions
		self._projects = {}
	
	def get_project(self, name):
		return self.get_project_with_parents(name, None)
	
	def get_project_with_parents(self, name, parent_names):
		if not name in self._projects:
			self._projects[name] = Project(self._manifest, name, self._plugin_manager, parent_names, self)
		
		return self._projects[name]

class Project(object):
	def __init__(self, manifest, name, plugin_manager, parent_names, project_loader):
		# Initial project name (without suffix .project) and check for circular dependencies
		self._name = name 
		if not parent_names is None and name in parent_names:
			raise ProjectError("Project %r depends on itself" % (name))
		
		self._manifest = manifest
		self._project_loader = project_loader
		self._plugin_manager = plugin_manager
		
		# Load project spec from file *.project
		self._filename = manifest.find_file(['default'], m2.LocalPath(), '%s.project' % (name))
		if self._filename is None:
			raise error_messages.ProjectFileError('%s.project' % (name), parent_names, 'Please make sure it is imported by manifest files correctly.')
		env = {'ProjectSpec': ProjectSpec}
		env.update(p2_naming.get_environment())
		env.update(self._plugin_manager.get_extensions())
		try:
			execfile(self._filename, env)
		except IOError:
			raise error_messages.ProjectFileError(self._filename, parent_names, 'Please make sure the file is accessible at the location specified above.')
		
		spec = env[name]
		if not isinstance(spec, ProjectSpec):
			raise ProjectError("Expected %r to be a ProjectSpec in %r" % (name, project_filename))
		
		# Get content of project spec: actions, depends and build configuration
		self._project_spec = spec
		self._actions = spec.get_actions()
		self._depends = spec.get_depends()
		self._build_configuration = spec.get_build_configuration()
		
		# Cached set of configurations
		self._local_configurations = None
		
		# Load sub projects
		checked_dependency_names = []
		unchecked_dependency_names = self._depends
		
		if parent_names is None:
			parent_names = []
		parent_names = parent_names + [self._name] # Initial parent_names
		
		while unchecked_dependency_names:
			temp_unchecked_dependency_names = unchecked_dependency_names[:]
			unchecked_dependency_names = []
			for project_name in temp_unchecked_dependency_names:
				# The 'parent_names' we are passing will sometimes be incomplete. However, 
				# they are only used for error reporting, so this is harmless.
				depend_project = project_loader.get_project_with_parents(project_name, parent_names)
				checked_dependency_names.append(project_name)
				unchecked_dependency_names.extend([new_dep._name for new_dep in depend_project.get_depend_projects() \
				                                           if not new_dep._name in checked_dependency_names])
		self._all_depends = checked_dependency_names
		
		# Find the set of dimensions and the super configuration function
		super_dimensions = list(self._build_configuration.get_dimensions())
		super_is_valid = [self._build_configuration.is_valid]
		for project in self.get_all_depend_projects():
			dimensions = project.get_dimensions()
			super_dimensions += [dim for dim in dimensions if not dim in super_dimensions]
		self._super_dimensions = super_dimensions
	
	def get_depend_projects(self):
		depend_projects = []
		for name in self._depends:
			depend_projects.append(self._project_loader._projects[name])
		return depend_projects
	
	def get_all_depend_projects(self):
		depend_projects = []
		for name in self._all_depends:
			depend_projects.append(self._project_loader._projects[name])
		return depend_projects
	
	def _is_depend_projects_have_same_dimensions(self):
		"""Return True if all its depend projects have same dimensions."""
		dimensions = self.get_dimensions()
		for project in self.get_depend_projects():
			if not dimensions == project.get_dimensions():
				return False
		return True
	
	def get_plugin_manager(self):
		return self._plugin_manager
	
	def get_project_filename(self):
		return self._filename
	
	def get_build_configuration(self):
		return self._build_configuration
	
	def get_dimensions(self):
		return self._super_dimensions
	
	@staticmethod
	def _next(mix_scale, digit_radix):
		assert len(mix_scale) == len(digit_radix)
		overflow = False
		carry = True
		digit = len(mix_scale) - 1
		while carry:
			mix_scale[digit] += 1
			if mix_scale[digit] == digit_radix[digit]:
				mix_scale[digit] = 0
				if digit > 0:
					digit -= 1
				else:
					overflow = True
					break
			else:
				carry = False
		return overflow
	
	@staticmethod
	def _valid_combinations(dimension_values, is_valid):
		all_dimensions = sorted(dimension_values.keys())
		digit_radix = [len(dimension_values[dimension]) for dimension in all_dimensions]
		mix_scale = [0]*len(all_dimensions)
		overflow = False
		
		ret = []
		while not overflow:
			configuration = {}
			for i in range(len(all_dimensions)):
				dimension = all_dimensions[i]
				configuration[dimension]=dimension_values[dimension][mix_scale[i]]
			if is_valid(configuration):
				ret.append(configuration)
			overflow = Project._next(mix_scale, digit_radix)
		return ret
	
	def _get_dimension_values(self, manifest, dimensions):
		dims = {}
		values = manifest.get_attribute(['default'], 'VALUES', m2.NoPaths())
		force_dimensions = self._project_loader._force_dimensions
		for dim in dimensions:
			if not values.has_key(dim):
				raise DimensionError("Unspecified dimension: %s" % dim)
			if force_dimensions.has_key(dim):
				dims[dim] = [value for value in values[dim] if value in force_dimensions[dim]]
			else:
				dims[dim] = values[dim]
		return dims
	
	def _get_local_configurations(self):
		"""local configurations is the result of all the combinations of its super dimension values
		   passed the filter is_valid() of its build_configuration."""
		if self._local_configurations == None:
			is_valid = self._build_configuration.is_valid
			dimension_values = self._get_dimension_values(self._manifest, self.get_dimensions())
			self._local_configurations = Project._valid_combinations(dimension_values, is_valid)
		return self._local_configurations
	
	@classmethod
	def get_configurations(cls, project):
		# Make sure cls._configurations_cache exist
		if not hasattr(cls, '_configurations_cache'):
			cls._configurations_cache = {}
		
		project_name = project.get_name()
		if project_name not in cls._configurations_cache.keys():
			# Cache miss, calculate the project configurations
			cls._configurations_cache[project_name] = project._calculate_configurations()
		
		return cls._configurations_cache[project_name]
	
	def _is_common_config_of_depend_projects(self, config):
		# if one config doesn't belong to all depend projects, return False
		for project in self.get_all_depend_projects():
			configs = Project.get_configurations(project)
			if config not in configs:
				return False
		return True
	
	def _is_compatible_config_of_depend_projects(self, config):
		# check compatibility with each depend projects
		for project in self.get_depend_projects():
			if not Project.configurations_compatible_with_project(project, config):
				return False
		return True
	
	def _calculate_configurations(self):
		"""Use the configurations of all depend projects and is_valid function of build_configuration of this
		   project to get its configurations."""
		configurations = []
		depend_projects = self.get_all_depend_projects()
		# If this project and all its depend projects have same dimensions, first get the intersection
		# of configurations of all its depend projects, then pass the result through the filter is_valid()
		# to get the configurations of this project. Thus local_configurations is not needed.
		if len(depend_projects) and self._is_depend_projects_have_same_dimensions():
			for config in Project.get_configurations(depend_projects[0]):
				if self._is_common_config_of_depend_projects(config) and \
				   self._build_configuration.is_valid(config):
					configurations.append(config)
		# If the dimensions don't match, first get local_configurations of this project, then test whether one
		# local config is compatible with all the depend projects.
		else:
			for config in self._get_local_configurations():
				if self._is_compatible_config_of_depend_projects(config):
					configurations.append(config)
		return configurations
	
	def get_actions(self):
		return self._actions.keys()
	
	@staticmethod
	def configurations_compatible(c1, c2):
		"""Two configurations are compatible if every dimension they have in common has
		a value in common."""
		for k, v in c1.iteritems():
			if k in c2:
				if c2[k] != v:
					return False
		return True
	
	@staticmethod
	def configurations_compatible_with_project(project, config):
		for depend_config in Project.get_configurations(project):
			if Project.configurations_compatible(config, depend_config):
				return True
		return False
	
	def get_output_name(self, action, configuration):
		"""Returns a list of path components, (e.g. ['dirname1', 'dirname2', 'filename'])
		which is the filename of the build artifact to be produced.
		"""
		if action in self._actions:
			if not self._actions[action] is None:
				return self._actions[action].get_name(self._manifest, self, configuration)
			else:
				raise ProjectError("Action %r has no name in project %r" % (action, self.get_project_filename()))
		else:
			raise ProjectError("Action %r doesn't apply to project %r" % (action, self.get_project_filename()))
	
	def get_action_name_dependencies(self, action):
		"""Returns a list of lists of dimensions, one for each component of the
		path. For each path component, we have a list of the dimensions that
		were used in determining it."""
		return self._actions[action].get_dimension_dependencies(self.get_dimensions())
	
	def get_identifier(self, configuration, exclude_dimensions):
		"""Returns a string which uniquely identifies this configuration
		The identifier should be unique across all dimensions that belong to
		this project (but not necessarily those belonging to dependencies)
		"""
		restricted_configuration = {}
		for dim in self.get_dimensions():
			restricted_configuration[dim] = configuration[dim]
		return self._project_spec.get_identifier(restricted_configuration, exclude_dimensions)
	
	@staticmethod
	def _expand_name(name_list, manifest, configuration, action, project):
		ret = []
		for p in name_list:
			ret.append(p.expand(configuration, action, manifest, project))
		return ret
		
	def get_dependencies(self):
		"""A list of project names, for the immediate dependencies."""
		return self._depends
	
	def get_all_dependencies(self):
		"""A list of project objects, for all dependencies, and dependencies
		of said dependencies (etc). Includes this project too."""
		ret = [self]
		for d in self._depends:
			ret += self._project_loader.get_project(d).get_all_dependencies()
		
		return ret
	
	def get_name(self):
		return self._name
	
	def get_attribute(self, configuration, key, path_type, allow_unfound=False):
		return self._manifest.get_attribute(self.get_keywords(configuration), key, path_type, allow_unfound)
	
	def get_keywords(self, configuration):
		"""The list of all keywords to use for a given configuration"""
		keywords = ['default']
		assert not 'project' in configuration, "Project should not be part of the configuration yet"
		
		for dim in self.get_dimensions():
			keywords.append("%s_%s" % (dim, configuration[dim]))
		
		keywords.append("project_%s" % (self.get_name()))
		
		return keywords
	
	def find_code_root(self, makefile):
		# Returns the CODE_ROOT attribute in two useful forms:
		# 1) As a relative path, suitable for being placed in a makefile (i.e. posix)
		# 2) As a relative path, suitable for being used in python
		keywords = ['default'] # start keywords for searching in manifest
		makefile_suitable = self._manifest.get_attribute(keywords, 'CODE_ROOT', m2.PosixPath(os.path.dirname(makefile)))
		python_suitable = self._manifest.get_attribute(keywords, 'CODE_ROOT', m2.LocalPath())
		return makefile_suitable, python_suitable
