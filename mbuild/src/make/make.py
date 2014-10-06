import os

from src.build import plugin_manager
from src.build import error_messages
from src.build import m2
from src.build import p2
from src.util import path_ex
from src.util import try_write
from src.make import t3

class MakeError(Exception):
	def __init__(self, action, config, message):
		self._action = action
		self._config = config
		self._message = message
	
	def __str__(self):
		if self._action is None:
			action_string = ''
		else:
			action_string = " (action=%r)" % self._action
		
		if self._config is None:
			config_string = ''
		else:
			config_string = " (config=%r)" % self._config
		
		return "Couldn't generate Makefile for %s%s: %s" % (
			action_string,
			config_string,
			self._message)

class Make(object):
	def __init__(self, project, make_plugin_manager, verbose_listing):
		self._project = project
		self._makefile_flags = {}
		self._verbose_listing = verbose_listing
		self._make_plugin_manager = make_plugin_manager
		
	def get_project(self):
		return self._project
	
	def write_makefile(self, manifest, project_loader, makefiles, makefile_path):
		# Generate makefile object for each Makefile
		makefile = t3.Makefile(makefile_path, self._project, project_loader)
		
		# Generate contents of each Makefile
		actions = makefiles[makefile_path]
		contents = self._real_makefile(manifest, actions, self._make_plugin_manager, makefile, project_loader)
		
		# Now write it out
		path_ex.makedirs(os.path.dirname(makefile_path))
		result = try_write.try_write(makefile_path, contents, text_mode=True, overwrite=True)

		return result
	
	def write_out(self, manifest, makefile_root, dimensions, project_loader, failed_makefiles):
		# We will put one makefile in each directory that has a build artifact in it
		# some of these makefiles will be able to build multiple things
		# Here we create a dictionary which maps Makefile filename to a list of 
		# configurations which will be built by it.
		
		
		# Work out where all our makefiles are going
		makefiles = {}
		proj_dir = os.path.dirname(self._project.get_project_filename())
		if makefile_root is None:
			makefile_dir = proj_dir
		else:
			rel_proj_dir = path_ex.make_path_relative(proj_dir, os.path.dirname(manifest.get_root_manifest()), os.path)
			makefile_dir = os.path.join(makefile_root, rel_proj_dir)
		
		# Get the list of configurations that use make
		configs = p2.Project.get_configurations(self._project)
		if dimensions:
			configs = [conf for conf in configs if 
			   reduce(lambda x, y: x and y, [conf[key] in dimensions[key] for key in dimensions.keys()])]
		
		for action in self._project.get_actions():
			for c in configs:
				try:
					name = self._project.get_output_name(action, c)
				except error_messages.ManifestError, err:
					raise error_messages.ProjectConfigError(self._project, c, err)
				directory = os.path.join(*name[0:-1])
				makefile_name = os.path.join(makefile_dir, directory, 'Makefile')
				
				if not makefile_name in makefiles:
					makefiles[makefile_name] = {}
				
				if not action in makefiles[makefile_name]:
					makefiles[makefile_name][action] = []
				
				makefiles[makefile_name][action].append(c)
		
		self.number_attempted = 0
		self.number_written = 0
		self.number_failed = 0
		
		for makefile_path in sorted(makefiles.keys()):
			result = self.write_makefile(manifest, project_loader, makefiles, makefile_path)
			self.number_attempted += 1
			if result == try_write.CHANGED:
				print("Writing Makefile: %s ...  ok (updated)" % (makefile_path))
				self.number_written += 1
			elif result == try_write.NO_CHANGE:
				if self._verbose_listing:
					print("Writing Makefile: %s ...  ok" % (makefile_path))
			elif result == try_write.COULDNT_CHANGE:
				print("Writing Makefile: %s ...  couldn't update" % (makefile_path))
				if not failed_makefiles.has_key(self._project.get_name()):
					failed_makefiles[self._project.get_name()] = {}
				failed_makefiles[self._project.get_name()].update({makefile_path:makefiles[makefile_path]})
				self.number_failed += 1

	
	@staticmethod
	def _cmp_configs(a, b):
		"""This doesn't have to return anything particularly significant, it just
		needs to be consistent across different python implementations. pypy and
		python give different results for the built in cmp operation on dict types.
		"""
		ret = cmp(len(a), len(b))
		if ret:
			return ret
		
		ret = cmp(a.keys(), b.keys())
		if ret:
			return ret
		
		for k in sorted(a.keys()):
			ret = cmp(a[k], b[k])
			if ret:
				return ret
		
		return 0
	
	def _real_makefile(self, manifest, actions, plugin_manager, makefile, project_loader):
		plugin_functions = plugin_manager.get_extensions()

		# collect all makefile plugin objects
		make_plugins = {}
		for func in plugin_functions:
			if func.startswith('makefn'):
				plugin = plugin_functions[func]()
				make_plugins[plugin.dimension + '_' + plugin.dimension_value] = plugin
		
		for action, configs in actions.iteritems():
			completed_configs = []
			for config in sorted(configs, cmp=self._cmp_configs):
				if config not in completed_configs and config['tool'] == 'make':
					completed_configs.append(config)
					exclude_dimensions = self._get_makefile_id_exclude_dimensions()
					full_identifier = self._project.get_name() + '_' + self._project.get_identifier(config, ['tool'])
					
					for dim in sorted(config.keys()):
						plugin_name = dim + '_' + config[dim]
						if plugin_name in make_plugins:
							makefile.set_attributes(manifest, config)
							makefile.set_fquery(manifest, config)
							identifier = self._project.get_identifier(config, exclude_dimensions)
							out_name = self._project.get_output_name('use', config)
							make_plugins[plugin_name].setup_fn(makefile, config, action, identifier, full_identifier, out_name, make_plugins[plugin_name])
		
		if len(makefile.rules) == 0:
			raise MakeError(None, None, "No Makefile plugin found")
		
		# Create required environment variables
		for func in plugin_functions:
			if func == "get_environment_variables":
				plugin_functions[func](makefile)
		
		makefile.condense()
		
		#if a function doesn't end in _toolchain, it is assumed to be a structure function
		structure_functions = []
		for func in plugin_functions:
			if func.startswith('structure_fn_check'):
				structure_function = (plugin_functions[func])(actions)
				if structure_function:
					structure_functions.append(structure_function)
		if len(structure_functions) != 1:
			raise MakeError(None,None,"Multiple makefile structure functions found")
		
		full_text = structure_functions[0](makefile)
		
		return full_text 
	
	def _get_makefile_id_exclude_dimensions(self):
		ret = ['tool']
		for p in self._project.get_action_name_dependencies('use')[0:-1]:
			ret += p
		return ret

def regenerate_failed_makefiles(manifest, t3_plugin_manager, project_loader, failed_makefiles, verbose_listing):
	
	number_written = 0		
	while len(failed_makefiles) > 0 :
		print "\nWARNING: The following Makefiles have changed, but not updated"

		for project_name in sorted(failed_makefiles.keys()):
			for makefile_path in sorted(failed_makefiles[project_name].keys()):
				print makefile_path
		
		rewrite = raw_input("\nDo you want to try again? (Y/N) ")
		if rewrite.lower() in ['y', 'yes']:		
			for project_name in sorted(failed_makefiles.keys()):
				if len(failed_makefiles[project_name]) > 0:
					m = Make(project_loader.get_project(project_name),t3_plugin_manager, verbose_listing)
					
					for makefile_path in sorted(failed_makefiles[project_name].keys()):
						result = m.write_makefile(manifest, project_loader, failed_makefiles[project_name], makefile_path)
						if result == try_write.CHANGED:
							print("Writing Makefile: %s ...  ok (updated)" % (makefile_path))		
							del(failed_makefiles[project_name][makefile_path])
							number_written += 1
						elif result == try_write.COULDNT_CHANGE:
							print("Writing Makefile: %s ...  couldn't update" % (makefile_path))
					if len(failed_makefiles[project_name]) == 0:
						del(failed_makefiles[project_name])
		else:
			break			

			
	return number_written			
