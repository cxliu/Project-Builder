import sys
import os
import ntpath
import fnmatch
import copy
from xml.dom import minidom

# See visual_studio.py for why we use this parser.
import non_strict_element_tree as ElementTree

from src.build import m2
from src.build import error_messages
from src.util import path_ex
from src.util import try_write
import visual_studio
import vc_configuration

class VcProjectBase(object):
	def __init__(self, project, filename, manifest, configurations, verbose_listing, vs_version):
		assert all([isinstance(c, vc_configuration.VcConfiguration) for c in configurations])
		assert vs_version in visual_studio.SUPPORTED_VS_VERSIONS
		self._name = project.get_name()
		self._project = project
		self._manifest = manifest
		self._configurations = configurations
		self._verbose = verbose_listing
		self.projects_updated = 0
		self.projects_failed = 0
		self.projects_attempted = 0
		self._guid = visual_studio.deterministic_guid(self._name)
		self._vs_version = vs_version
	
	def get_guid(self):
		return self._guid
	
	def get_filename(self):
		return self._filename
	
	def get_project(self):
		return self._project

	def has_any_configuration(self, vc_configurations):
		"""Returns true if any of the vc_configurations passed in are built by
		this project"""
		configurations = [c.get_configuration() for c in vc_configurations]
		for c in self._configurations:
			if any([self._project.configurations_compatible(c.get_configuration(), c2) for c2 in configurations]):
				return True
		
		return False
	
	def _read_enum(self, attribute_fn, enum, configuration, manifest):
		assert enum in self.ENUMS, "Unknown enum %s" % enum
		value = attribute_fn(enum)
		if value is None:
			message = error_messages.unknown_attribute_value(enum, manifest)
			raise visual_studio.VsError(None, self.get_project(), configuration.get_configuration(), message)
		
		if not value in self.ENUMS[enum]:
			raise visual_studio.VsError(None, self.get_project(), configuration.get_configuration(), "Unexpected enum value %r for %s" % (value, enum))
		
		return self.ENUMS[enum][value]
	
	def notify_write_out(self):
		print("Writing VC%s project: %s ..." % (self._vs_version, self._filename)),

	@staticmethod
	def _include_filename_in_project(filename):
		valid_patterns = ['*.c', '*.h', '*.cpp', '*.rc', '*.def', '*.txt', '*.asm', '*.lib', "*.s"]
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])

	@staticmethod
	def _is_header_file(filename):
		valid_patterns = ['*.h', '*.def', ]
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])
	
	@staticmethod
	def _is_static_library_file(filename):
		valid_patterns = ['*.lib' ]
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])
	
	@staticmethod
	def _is_compiled_file(filename):
		valid_patterns = ['*.c', '*.cpp', ]
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])
	
	@staticmethod
	def _is_assembled_file(filename):
		valid_patterns = ['*.asm']
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])
	
	@staticmethod
	def _is_resource_file(filename):
		valid_patterns = ['*.rc']
		return any([fnmatch.fnmatchcase(filename.lower(), p) for p in valid_patterns])
	
	def sorted_configurations(self):
		return sorted(self._configurations, key=lambda a: a.get_vs_identifier())
	
	def _versioned_name(self, name):
		return "VS%s_%s" % (self._vs_version, name)
		
	def _get_all_files(self, path_transform):
		# This recreates the directory tree as a tree of 'Filter' nodes.
		
		keywords = set([])
		for c in self._configurations:
			keywords.update(c.get_keywords())
		
		tree_root = self._manifest.get_attribute(keywords, 'CODE_ROOT', m2.LocalPath())

		# For each file, determine which configurations it is used for
		# (so if it is only used for a subset of configurations, then
		# we know to exclude it from other builds)
		all_files = []
		for c in self.sorted_configurations():
			# We assume that the configurations passed in are meant for us
			assert c.get_configuration()['tool'] in ['msvs2005', 'msvs2008', 'msvs2010', 'msvs2012', 'msvs2013']
			configuration_files = \
				[{"pwd_relative": m2.LocalPath().write_path(path_transform(f)),
				  "project_relative": m2.WindowsPath(os.path.dirname(self._filename)).write_path(path_transform(f)),
				  "filter_relative": m2.WindowsPath(tree_root).write_path(path_transform(f)),
				  "tags": f.get_tags()
				 } for f in self._manifest.get_file_set(c.get_keywords())
				   if self._include_filename_in_project(f.get_path(m2.LocalPath()))
				]
			
			for f in configuration_files:
				for a_file in all_files:
					if a_file["pwd_relative"] == f["pwd_relative"]:
						a_file["configurations"].append(c.get_vs_full_identifier())
						break
				else:
					f["configurations"] = [c.get_vs_full_identifier()]
					all_files.append(f)
		
		return all_files
	

class VcProject(VcProjectBase):
	ENUMS = {
	  'CHARACTER_SET':                 {'not_set': '0',
	                                    'unicode': '1',
	                                    'multibyte': '2'},
	  'CONFIGURATION_TYPE':            {'makefile': '0',
	                                    'application':  '1',
	                                    'dynamic_library':  '2',
	                                    'static_library':  '4',
	                                    'utility': '10'},
	  'WHOLE_PROGRAM_OPTIMIZATION':    {'off': '0',
	                                    'link_time_code_gen': '1'},
	  'LINK_INCREMENTAL':              {'false': '1',
	                                    'true': '2'},
	  'COMPILE_AS':                    {'default': '0',
	                                    'c': '1',
	                                    'cplusplus': '2'},
	  'OPTIMIZATION':                  {'disabled': '0',
	                                    'min_size': '1',
	                                    'max_speed': '2',
	                                    'full': '3'},
	  'DEBUG_INFO_FORMAT':             {'disabled': '0',
	                                    'c7': '1',
	                                    'prog_db': '3',
	                                    'prog_db_edit_cont': '4'},
	  'RUNTIME_CHECKS':                {'default': '0',
	                                    'stack_frames': '1',
	                                    'uninitialized_variables': '2',
	                                    'both': '3'},
	  'RUNTIME_LIBRARY':               {'threaded': '0',
	                                    'threaded_debug': '1',
	                                    'threaded_dll': '2',
	                                    'threaded_debug_dll': '3'},
	  'ENABLE_COMDAT_FOLDING':         {'false': '1',
	                                    'true': '2'},
	  'OPTIMIZE_REFERENCES':           {'keep': '1',
	                                    'eliminate': '2'},
	  'SUBSYSTEM':                     {'console': '1',
	                                    'windows': '2',
	                                    'native': '3'},
	  'TARGET_MACHINE':                {'x86':  '1',
	                                    'x64': '17'},
	  'WARNING_LEVEL':                 {'off': '0',
	                                    'min': '1',
	                                    'lite': '2',
	                                    'standard': '3',
	                                    'max': '4'},
	  'CPP_EXCEPTIONS':                {'disabled': '0',
	                                    'enabled': '1',
	                                    'enabled_seh': '2'},
	  'MINIMAL_REBUILD':               {'false': '0',
	                                    'true': '1'},
	  'BUFFER_SECURITY_CHECK':         {'false': '0',
	                                    'true': '1'},
	  'USE_PRECOMPILED_HEADER':        {'false': '0',
	                                    'true': '1'},
	  'DETECT_64BIT_PROBLEMS':         {'false': '0',
	                                    'true': '1'},
	  'GENERATE_DEBUG_INFO':           {'false': '0',
	                                    'true': '1'},
	  'LINK_LIBRARY_DEPENDENCIES':     {'false': '0',
	                                    'true': '1'},
	  'USE_STRICT_LANGUAGE':           {'false': 'false',
	                                    'true': 'true'},
	  }
	
	def __init__(self, project, filename, manifest, configurations, verbose_listing, vs_version):
		super(VcProject, self).__init__(project, filename, 
		                                           manifest, configurations, verbose_listing, vs_version)
		assert vs_version in ("2005", "2008")
		self._filename = filename
	
	def write_out(self, path_transform, all_vc_projects):
		
		
		try:
			root = ElementTree.Element('VisualStudioProject', 
			                           ProjectType='Visual C++',
			                           Version={'2005':'8.00', '2008':'9.00'}[self._vs_version],
			                           Name=self._name,
			                           ProjectGUID="{%s}" % (self._guid),
			                           RootNamespace=self._name,
			                           Keyword='Win32Proj')
			
			platforms = ElementTree.SubElement(root, "Platforms")
			platform_names = set()
			for c in self._configurations:
				platform_names.add(c.get_vs_platform())
			
			for p in sorted(platform_names):
				platform = ElementTree.SubElement(platforms, "Platform", Name=p)
			
			all_files = self._get_all_files(path_transform)
			
			toolfiles = ElementTree.SubElement(root, 'ToolFiles')
			
			# We have at least one .asm file
			if any([os.path.splitext(a['filter_relative'])[1] == '.asm' for a in all_files]):
				ElementTree.SubElement(toolfiles, 'DefaultToolFile', FileName='masm.rules')
			
			configurations_node = ElementTree.SubElement(root, 'Configurations')
			
			for c in self.sorted_configurations():
				a = lambda name: self._manifest.get_attribute(c.get_keywords(), self._versioned_name(name), m2.NoPaths())
				e = lambda name: self._read_enum(a, name, c, self._manifest)
				
				configuration = ElementTree.SubElement(configurations_node, 'Configuration',
					Name='|'.join([c.get_vs_identifier(), c.get_vs_platform()]),
					OutputDirectory='$(SolutionDir)$(ConfigurationName)\\VS%s' % self._vs_version,
					IntermediateDirectory='$(ConfigurationName)\\VS%s' % self._vs_version,
					ConfigurationType=e('CONFIGURATION_TYPE'),
					CharacterSet=e('CHARACTER_SET'),
					WholeProgramOptimization=e('WHOLE_PROGRAM_OPTIMIZATION'))
				
				for t in self._tools():
					if 'attribute_gen' in t:
						try:
							attributes = t['attribute_gen'](c, self._manifest, path_transform)
						except error_messages.UnsetAttributeError, err:
							message = error_messages.unknown_attribute_value(err.get_attribute_name(), self._manifest)
							raise visual_studio.VsError(None, self.get_project(), c.get_configuration(), message)
						
						if attributes['Enabled']:
							del(attributes['Enabled'])
							ElementTree.SubElement(configuration, 'Tool', 
								attributes,
								Name=t['name'])
					else:
						ElementTree.SubElement(configuration, 'Tool', 
							Name=t['name'])
			
			
			ElementTree.SubElement(root, 'References')
			
			files_node = ElementTree.SubElement(root, 'Files')
			
			
			
			for f in sorted(all_files, key=lambda a: a["filter_relative"]):
				filter_path = path_ex.split_path(ntpath.dirname(f["filter_relative"]), ntpath)
				filt = self._get_filter(files_node, filter_path)
				file_node = ElementTree.SubElement(filt, 'File',
					RelativePath=ntpath.normpath(f["project_relative"]))

				for c in self.sorted_configurations():
					if not c.get_vs_full_identifier() in f["configurations"]:
						file_configuration_node = ElementTree.SubElement(file_node, 'FileConfiguration',
							Name=c.get_vs_identifier(),
							ExcludedFromBuild="true")
						ElementTree.SubElement(file_configuration_node, 'Tool',
							Name=self._get_file_tool(f["pwd_relative"]))

			ElementTree.SubElement(root, 'Globals')

			path_ex.makedirs(os.path.dirname(self._filename))
			result = try_write.try_write(self._filename, ElementTree.tostring(root, 'Windows-1252'), text_mode=False, overwrite=True)
			self.projects_attempted += 1 
			if result == try_write.CHANGED:
				self.notify_write_out()
				self.projects_updated += 1
				print(" ok (updated)")
			elif result == try_write.NO_CHANGE:
				if self._verbose:
					self.notify_write_out()
					print(" ok")
			elif result == try_write.COULDNT_CHANGE:
				self.notify_write_out()
				self.projects_failed += 1 
				print(" couldn't update")

			return result
		except IOError:
			print("Error")
			raise

	@staticmethod
	def _get_file_tool(filename):
		if os.path.splitext(filename)[1] == '.c':
			return 'VCCLCompilerTool'
		return 'VCCustomBuildTool'

	def _get_filter(self, root, filter_path):
		assert filter_path

		traverse = None
		filter_name = filter_path[0]
		for c in root.getchildren():
			if c.tag == 'Filter' and c.attrib["Name"] == filter_name:
				traverse = c
				break
		else:
			traverse = ElementTree.SubElement(root, 'Filter', Name=filter_name)

		if len(filter_path) == 1:
			return traverse

		return self._get_filter(traverse, filter_path[1:])


	def _tools(self):
		return [
			{'name': 'VCPreBuildEventTool'}, 
			{'name': 'VCCustomBuildTool'},
			{'name': 'VCXMLDataGeneratorTool'},
			{'name': 'VCWebServiceProxyGeneratorTool'},
			{'name': 'VCCLCompilerTool', 'attribute_gen': self._compiler_attributes},
			{'name': 'VCManagedResourceCompilerTool'},
			{'name': 'VCResourceCompilerTool'},
			{'name': 'VCPreLinkEventTool'},
			{'name': 'VCLinkerTool', 'attribute_gen': self._linker_attributes},
			{'name': 'VCLibrarianTool', 'attribute_gen': self._librarian_attributes},
			{'name': 'VCALinkTool'},
			{'name': 'VCManifestTool'},
			{'name': 'VCXDCMakeTool'},
			{'name': 'VCBscMakeTool'},
			{'name': 'VCFxCopTool'},
			{'name': 'VCAppVerifierTool'},
			{'name': 'VCWebDeploymentTool'},
			{'name': 'VCPostBuildEventTool'}
		]
	
	@staticmethod
	def _escape_define_value(v):
		return v.replace('"', r'\"').replace("'", r"\'")
			
	def _compiler_attributes(self, configuration, manifest, path_transform):
		path_type = m2.TransformPath(m2.WindowsPath(os.path.dirname(self._filename)), path_transform)
		raw_a = lambda name: manifest.get_attribute(configuration.get_keywords(), name, path_type)
		a = lambda name: raw_a(self._versioned_name(name))
		e = lambda name: self._read_enum(a, name, configuration, manifest)
		
		define_attribute = raw_a('DEFINE')
		defines = []
		for k in sorted(define_attribute.keys()):
			v = define_attribute[k]
			if v is None:
				defines.append('%s' % (k))
			else:
				defines.append('%s=%s' % (k, self._escape_define_value(v)))
		
		return {
			'Enabled': True,
			'Optimization': e('OPTIMIZATION'),
			'AdditionalIncludeDirectories': ';'.join(raw_a('INCLUDE')),
			'PreprocessorDefinitions': ';'.join(defines),
			'MinimalRebuild': e('MINIMAL_REBUILD'),
			'ExceptionHandling': e('CPP_EXCEPTIONS'),
			'BasicRuntimeChecks': e('RUNTIME_CHECKS'),
			'BufferSecurityCheck': e('BUFFER_SECURITY_CHECK'),
			'RuntimeLibrary': e('RUNTIME_LIBRARY'),
			'UsePrecompiledHeader': e('USE_PRECOMPILED_HEADER'),
			'DisableLanguageExtensions': e('USE_STRICT_LANGUAGE'),
			'WarningLevel': e('WARNING_LEVEL'),
			'Detect64BitPortabilityProblems': e('DETECT_64BIT_PROBLEMS'),
			'DebugInformationFormat': e('DEBUG_INFO_FORMAT'),
			'CompileAs': e('COMPILE_AS'),
			'DisableSpecificWarnings': ';'.join(a('DISABLE_SPECIFIC_WARNINGS')),
		}
	
	def _linker_attributes(self, configuration, manifest, path_transform):
		path_type = m2.TransformPath(m2.WindowsPath(os.path.dirname(self._filename)), path_transform)
		raw_a = lambda name: manifest.get_attribute(configuration.get_keywords(), name, path_type)
		a = lambda name: raw_a(self._versioned_name(name))
		e = lambda name: self._read_enum(a, name, configuration, manifest)
		
		# Get the location of the module definition file (relative to pwd)
		# If this file exists, then it drives our output filename.
		def_files = manifest.find_file_pattern(configuration.get_keywords(), path_type, "*.def")
		def_files_local = manifest.find_file_pattern(configuration.get_keywords(), m2.LocalPath(), "*.def")
		
		if len(def_files) == 0:
			module_definition_file = ''
			module_definition_file_local = ''
		elif len(def_files) == 1:
			module_definition_file = def_files[0]
			module_definition_file_local = def_files_local[0]
		else:
			raise visual_studio.VsError(None, self.get_project(), configuration.get_configuration(), "Multiple *.def files were found (%r)" % def_files)
		
		if module_definition_file is None:
			module_definition_file = ''
		configuration_type = a('CONFIGURATION_TYPE')
		ext = raw_a('EXT')
		output_file = visual_studio.get_output_file(module_definition_file_local, configuration_type, ext, '\\')
		
		if not configuration_type in ('application', 'dynamic_library'):
			return {'Enabled': False}
		
		return {
			'Enabled': True,
			'OutputFile': output_file,
			'LinkIncremental': e('LINK_INCREMENTAL'),
			'AdditionalDependencies': ' '.join(a('LIBRARIES')),
			'AdditionalLibraryDirectories': ';'.join(a('LIBRARY_DIRECTORIES')),
			'IgnoreDefaultLibraryNames': ';'.join(a('IGNORE_DEFAULT_LIBRARY_NAMES')),
			'GenerateDebugInformation': e('GENERATE_DEBUG_INFO'),
			'SubSystem': e('SUBSYSTEM'),
			'OptimizeReferences': e('OPTIMIZE_REFERENCES'),
			'EnableCOMDATFolding': e('ENABLE_COMDAT_FOLDING'),
			'ModuleDefinitionFile': module_definition_file,
			'TargetMachine': e('TARGET_MACHINE'),
		}

	def _librarian_attributes(self, configuration, manifest, path_transform):
		path_type = m2.TransformPath(m2.WindowsPath(os.path.dirname(self._filename)), path_transform)
		a = lambda name: manifest.get_attribute(configuration.get_keywords(), self._versioned_name(name), path_type)
		e = lambda name: self._read_enum(a, name, configuration, manifest)
		
		if not a('CONFIGURATION_TYPE') == 'static_library':
			return {'Enabled': False}

		return {
			'Enabled': True,
			'LinkLibraryDependencies': e('LINK_LIBRARY_DEPENDENCIES'),
			'AdditionalDependencies': ' '.join(a('LIBRARIES')),
			'AdditionalLibraryDirectories': ';'.join(a('LIBRARY_DIRECTORIES')),
			'IgnoreDefaultLibraryNames': ';'.join(a('IGNORE_DEFAULT_LIBRARY_NAMES')),
		}


class VcxProject(VcProjectBase):
	ENUMS = {
	  'CHARACTER_SET':                 {'not_set': '',
	                                    'unicode': 'Unicode',
	                                    'multibyte': 'MultiByte'},
	  'CONFIGURATION_TYPE':            {'application':  'Application',
	                                    'dynamic_library':  'DynamicLibrary',
	                                    'static_library':  'StaticLibrary',
	                                    #'10': 'Utility'
	                                   },
	  'WHOLE_PROGRAM_OPTIMIZATION':    {'off': 'false',
	                                    'link_time_code_gen': 'true'},
	  'LINK_INCREMENTAL':              {'false': 'false',
	                                    'true': 'true'},
	  'COMPILE_AS':                    {'default': 'Default',
	                                    'c': 'CompileAsC',
	                                    'cplusplus': 'CompileAsCpp'},
	  'OPTIMIZATION':                  {'disabled': 'Disabled',
	                                    'min_size': 'MinSize',
	                                    'max_speed': 'MaxSpeed',
	                                    'full': 'Full'},
	  'DEBUG_INFO_FORMAT':             {'disabled': '',
	                                    'c7': 'OldStyle',
	                                    'prog_db': 'ProgramDatabase',
	                                    'prog_db_edit_cont': 'EditAndContinue'},
	  'BASIC_RUNTIME_CHECKS':          {'default': 'Default',
	                                    'both': 'EnableFastChecks',},
	  'RUNTIME_LIBRARY':               {'threaded': 'MultiThreaded',
	                                    'threaded_debug': 'MultiThreadedDebug',
	                                    'threaded_dll': 'MultiThreadedDLL',
	                                    'threaded_debug_dll': 'MultiThreadedDebugDLL'},
	  'RUNTIME_CHECKS':                {'default': 'Default',
	                                    'stack_frames': 'StackFrameRuntimeCheck',
	                                    'uninitialized_variables': 'UninitializedLocalUsageCheck',
	                                    'both': 'EnableFastChecks'},
	  'ENABLE_COMDAT_FOLDING':         {'false': 'false',
	                                    'true': 'true'},
	  'OPTIMIZE_REFERENCES':           {'keep': 'false',
	                                    'eliminate': 'true',},
	  'SUBSYSTEM':                     {'console': 'Console',
	                                    'windows': 'Windows',
	                                    'native': 'Native'},
	  'TARGET_MACHINE':                {'x86': 'MachineX86',
	                                    'x64': 'MachineX64',
	                                    'arm': 'MachineARM'},
	  'WARNING_LEVEL':                 {'off': 'Level0',
	                                    'min': 'Level1',
	                                    'lite': 'Level2',
	                                    'standard': 'Level3',
	                                    'max': 'Level4'},
	  'CPP_EXCEPTIONS':                {'disabled': '',
	                                    'enabled': 'Sync',
	                                    'enabled_seh': 'Async',
	                                    'enabled_extern_c': 'SyncThrow'},
	  'MINIMAL_REBUILD':               {'false': 'false',
	                                    'true': 'true'},
	  'USE_STRICT_LANGUAGE':           {'false': 'false',
	                                    'true': 'true'},
	  'FUNCTION_LEVEL_LINK':           {'false': 'false',
	                                    'true': 'true'},
	  'INTRINSIC_FUNCTIONS':           {'false': 'false',
	                                    'true': 'true'},
	  'LINK_SAFE_EXCEPTION_HANDLER':   {'false': 'false',
	                                    'true': 'true'},
	  'BUFFER_SECURITY_CHECK':         {'false': 'false',
	                                    'true': 'true'},
	  'LINK_LIBRARY_DEPENDENCIES':     {'false': 'false',
	                                    'true': 'true'},
	  }
	def __init__(self, project, filename, manifest, configurations, verbose_listing, vs_version):
		super(VcxProject, self).__init__(project, filename, 
		                                    manifest, configurations, verbose_listing, vs_version)
		assert vs_version in ("2010", "2012", "2013")
		self._filename = filename
		self._filters_filename = self._filename + '.filters'

	def _get_output_filters_file(self):
		return self._filename + '.filters'
		
	def notify_write_out_filters(self):
		print("Writing VS%s filters: %s ..." % (self._vs_version, self._filters_filename)),
	
	def _is_custom_build_file(self, tags):
		custom_build_tag = [tag for tag in tags if tag[0] == "vs_custom_build"]
		return len(custom_build_tag) == 1
	
	def _get_custom_build_tag(self, configuration, file):
		'''Find "vs_custom_build" tag and extract parameters (custom_build_tool, custom_build_suffix, 
		   custom_build_option) of this tag.'''
		assert isinstance(file, dict)
		custom_build_tag = [tag for tag in file['tags'] if tag[0] == "vs_custom_build"]
		assert len(custom_build_tag) != 0, "%s: vs_custom_build tag is not found." % file['project_relative']
		
		if len(custom_build_tag) > 1:
			raise visual_studio.VsError(None, self.get_project(), configuration.get_configuration(), 
			                            "%s: vs_custom_build tag can't be applied more than one time." % file['project_relative'])
		params = custom_build_tag[0][1]
		if len(params) == 2:
			return (params[0], params[1], "")
		elif len(params) == 3:
			return (params[0], params[1], params[2])
		else:
			raise visual_studio.VsError(None, self.get_project(), configuration.get_configuration(), 
			                            "Format of tag vs_custom_build of %s is wrong. The right format is vs_custom_build(tool, suffix, [compile options])" % file['project_relative'])
	
	def write_out(self, path_transform, all_vc_projects):
		
		raw_a = lambda name: self._manifest.get_attribute(c.get_keywords(), name, m2.NoPaths())
		a = lambda name: raw_a(self._versioned_name(name))
		e = lambda name: self._read_enum(a, name, c, self._manifest)
		
		tools_ver = {'2010': '4.0',
		             '2012': '4.0',
		             '2013': '12.0'}[self._vs_version]
		
		root = ElementTree.Element('Project',
		                           ToolsVersion=tools_ver,
		                           DefaultTargets='Build',
		                           xmlns='http://schemas.microsoft.com/developer/msbuild/2003')
		
		# Map project configurations
		project_configs_node = ElementTree.SubElement(root, 'ItemGroup',
		                                              Label='ProjectConfigurations')
		for c in self.sorted_configurations():
			c_node = ElementTree.SubElement(project_configs_node,
			                                'ProjectConfiguration',
			                                Include=c.get_vs_full_identifier())
			ElementTree.SubElement(c_node, 'Configuration').text = c.get_vs_identifier()
			ElementTree.SubElement(c_node, 'Platform').text = c.get_vs_platform()

		# Globals ItemGroup
		globals_node = ElementTree.SubElement(root, 'PropertyGroup', Label='Globals')
		ElementTree.SubElement(globals_node, 'Keyword').text = 'Win32Proj'
		ElementTree.SubElement(globals_node, 'ProjectName').text = self._project.get_name()
		ElementTree.SubElement(globals_node, 'ProjectGuid').text = "{%s}" % self._guid
		ElementTree.SubElement(globals_node, 'RootNamespace').text = self._project.get_name()
		
		# Add extra Global PropertyGroup
		extra_global_propertygroup = a('EXTRA_GLOBAL_PROPERTYGROUP')
		if extra_global_propertygroup:
			for extra_property_name in sorted(extra_global_propertygroup.keys()):
				ElementTree.SubElement(globals_node, extra_property_name).text = \
					extra_global_propertygroup[extra_property_name]
		
		ElementTree.SubElement(root, 'Import', Project=r"$(VCTargetsPath)\Microsoft.Cpp.Default.props")

		for c in self.sorted_configurations():
			node = ElementTree.SubElement(root, 'PropertyGroup',
			                              Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier(),
			                              Label='Configuration')
			charset = e('CHARACTER_SET')
			ElementTree.SubElement(node, 'CharacterSet').text = charset
			config_type = e('CONFIGURATION_TYPE')
			ElementTree.SubElement(node, 'ConfigurationType').text = config_type
			runtimelib = e('RUNTIME_LIBRARY')
			if runtimelib in ['MultiThreaded', 'MultiThreadedDLL']:
				use_debug_libraries = 'false'
			else:
				use_debug_libraries = 'true'
			ElementTree.SubElement(node, 'UseDebugLibraries').text = use_debug_libraries
			ElementTree.SubElement(node, 'PlatformToolset').text = a("PLATFORM_TOOLSET")
			whole_opt = e('WHOLE_PROGRAM_OPTIMIZATION')
			ElementTree.SubElement(node, 'WholeProgramOptimization').text = whole_opt
			
			# Add extra PropertyGroup
			extra_propertygroup = a('EXTRA_PROPERTYGROUP')
			if extra_propertygroup:
				for extra_property_name in sorted(extra_propertygroup.keys()):
					ElementTree.SubElement(node, extra_property_name).text = \
						extra_propertygroup[extra_property_name]
		
		ElementTree.SubElement(root, 'Import', Project=r"$(VCTargetsPath)\Microsoft.Cpp.props")

		all_files = self._get_all_files(path_transform)
		extension_settings = ElementTree.SubElement(root, 'ImportGroup', Label='ExtensionSettings')
		
		# If we have a .asm file, then we want to add some extra bits to our output
		has_asm = False
		if any([os.path.splitext(a['filter_relative'])[1] == '.asm' for a in all_files]):
			has_asm = True
		
		# We have at least one .asm file
		if has_asm:
			ElementTree.SubElement(extension_settings, 'Import', Project=r'$(VCTargetsPath)\BuildCustomizations\masm.props')
		
		for c in self.sorted_configurations():
			node = ElementTree.SubElement(root, 'ImportGroup',
			                              Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier(),
			                              Label='PropertySheets')
			ElementTree.SubElement(node, 'Import',
			                       Project=r"$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props",
			                       Condition=r"exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')",
			                       Label='LocalAppDataPlatform')

		ElementTree.SubElement(root, 'PropertyGroup', Label='UserMacros')

		node = ElementTree.SubElement(root, 'PropertyGroup')
		ElementTree.SubElement(node, '_ProjectFileVersion').text = '10.0.30319.1'
		for c in self.sorted_configurations():
			a = lambda name: self._manifest.get_attribute(c.get_keywords(), self._versioned_name(name), m2.NoPaths())
			e = lambda name: self._read_enum(a, name, c, self._manifest)

			ElementTree.SubElement(node, 'IntDir',
			                       Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier()).text = "$(Configuration)\\VS"+ self._vs_version +"\\"
			ElementTree.SubElement(node, 'OutDir',
			                       Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier()).text = "$(SolutionDir)$(Configuration)\\VS"+ self._vs_version +"\\"
			link_incremental = e('LINK_INCREMENTAL')
			ElementTree.SubElement(node, 'LinkIncremental',
			                       Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier()).text = link_incremental

		for c in self.sorted_configurations():
			keywords = c.get_keywords()
			path_type = m2.TransformPath(m2.WindowsPath(os.path.dirname(self._filename)), path_transform)
			raw_a = lambda name: self._manifest.get_attribute(keywords, name, path_type)
			a = lambda name: raw_a(self._versioned_name(name))
			e = lambda name: self._read_enum(a, name, c, self._manifest)

			idg_node = ElementTree.SubElement(root, 'ItemDefinitionGroup',
			                                  Condition=r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier())

			cl_node = ElementTree.SubElement(idg_node, 'ClCompile')
			incl_dirs = ";".join(raw_a('INCLUDE'))
			ElementTree.SubElement(cl_node, 'AdditionalIncludeDirectories').text = incl_dirs
			runtime_checks = e('RUNTIME_CHECKS')
			ElementTree.SubElement(cl_node, 'BasicRuntimeChecks').text = runtime_checks
			bufsec_check = a('BUFFER_SECURITY_CHECK')
			ElementTree.SubElement(cl_node, 'BufferSecurityCheck').text = bufsec_check
			compile_as = e('COMPILE_AS')
			ElementTree.SubElement(cl_node, 'CompileAs').text = compile_as
			debug_info_format = e('DEBUG_INFO_FORMAT')
			ElementTree.SubElement(cl_node, 'DebugInformationFormat').text = debug_info_format
			disable_warnings = ';'.join(a('DISABLE_SPECIFIC_WARNINGS'))
			ElementTree.SubElement(cl_node, 'DisableSpecificWarnings').text = disable_warnings
			ElementTree.SubElement(cl_node, 'ExceptionHandling').text = e('CPP_EXCEPTIONS')
			minimal_rebuild = e('MINIMAL_REBUILD')
			ElementTree.SubElement(cl_node, 'MinimalRebuild').text = minimal_rebuild
			optimization = e('OPTIMIZATION')
			ElementTree.SubElement(cl_node, 'Optimization').text = optimization
			strict_language = e('USE_STRICT_LANGUAGE')
			ElementTree.SubElement(cl_node, 'DisableLanguageExtensions').text = strict_language
			
			preprocessor_defs = []
			for k, v in sorted(raw_a('DEFINE').iteritems()):
				if v is None:
					preprocessor_defs.append('%s' % (k))
				else:
					preprocessor_defs.append('%s=%s' % (k, v))

			ElementTree.SubElement(cl_node, 'PreprocessorDefinitions').text = ';'.join(preprocessor_defs)
			runtimelib = e('RUNTIME_LIBRARY')
			ElementTree.SubElement(cl_node, 'RuntimeLibrary').text = runtimelib
			ElementTree.SubElement(cl_node, 'PrecompiledHeader')
			warning_level = e('WARNING_LEVEL')
			ElementTree.SubElement(cl_node, 'WarningLevel').text = warning_level
			ElementTree.SubElement(cl_node, 'FunctionLevelLinking').text = e('FUNCTION_LEVEL_LINK')
			ElementTree.SubElement(cl_node, 'IntrinsicFunctions').text = e('INTRINSIC_FUNCTIONS')
			
			# Add extra compiler configurations
			extra_compiler_configurations = a('EXTRA_COMPILER_CONFIGURATIONS')
			if extra_compiler_configurations:
				for extra_compiler_conf_name in sorted(extra_compiler_configurations.keys()):
					ElementTree.SubElement(cl_node, extra_compiler_conf_name).text = \
						extra_compiler_configurations[extra_compiler_conf_name]
			
			ignore_libs = ';'.join(a('IGNORE_DEFAULT_LIBRARY_NAMES'))
			deps = ';'.join(a('LIBRARIES'))
			
			libdirs = ';'.join(a('LIBRARY_DIRECTORIES'))
			
			# StaticLibraries have no <Link> tag, but a <Lib> tag.
			configuration_type = a('CONFIGURATION_TYPE')
			if configuration_type == 'static_library':
				lib_node = ElementTree.SubElement(idg_node, 'Lib')
				ElementTree.SubElement(lib_node, 'AdditionalDependencies').text = deps
				ElementTree.SubElement(lib_node, 'AdditionalLibraryDirectories').text = libdirs
				ElementTree.SubElement(lib_node, 'IgnoreSpecificDefaultLibraries').text = ignore_libs
				ref_node = ElementTree.SubElement(idg_node, 'ProjectReference')
				link_library_deps = a('LINK_LIBRARY_DEPENDENCIES')
				ElementTree.SubElement(ref_node, 'LinkLibraryDependencies').text = link_library_deps
			else:
				link_node = ElementTree.SubElement(idg_node, 'Link')
				ElementTree.SubElement(link_node, 'AdditionalDependencies').text = deps
				ElementTree.SubElement(link_node, 'AdditionalLibraryDirectories').text = libdirs
				comdat = e('ENABLE_COMDAT_FOLDING')
				ElementTree.SubElement(link_node, 'EnableCOMDATFolding').text = comdat
				debug_info = a('GENERATE_DEBUG_INFO')
				ElementTree.SubElement(link_node, 'GenerateDebugInformation').text = debug_info
				ElementTree.SubElement(link_node, 'IgnoreSpecificDefaultLibraries').text = ignore_libs
				
				# Get the location of the module definition file (relative to pwd)
				# If this file exists, then it drives our output filename.
				def_files = self._manifest.find_file_pattern(c.get_keywords(), path_type, "*.def")
				def_files_local = self._manifest.find_file_pattern(c.get_keywords(), m2.LocalPath(), "*.def")
				
				if len(def_files) == 0:
					module_definition_file = ''
					module_definition_file_local = ''
				elif len(def_files) == 1:
					module_definition_file = def_files[0]
					module_definition_file_local = def_files_local[0]
				else:
					raise visual_studio.VsError(None, self.get_project(), c.get_configuration(), "Multiple *.def files were found (%r)" % def_files)
				
				if module_definition_file is None:
					module_definition_file = ''
				ext = raw_a('EXT')
				output_file = visual_studio.get_output_file(module_definition_file_local, configuration_type, ext, '')
				
				ElementTree.SubElement(link_node, 'ModuleDefinitionFile').text = module_definition_file
				optimize_references = e('OPTIMIZE_REFERENCES')
				ElementTree.SubElement(link_node, 'OptimizeReferences').text = optimize_references
				ElementTree.SubElement(link_node, 'OutputFile').text = output_file
				ElementTree.SubElement(link_node, 'SubSystem').text = e('SUBSYSTEM')
				ElementTree.SubElement(link_node, 'TargetMachine').text = e('TARGET_MACHINE')
				if self._vs_version in ['2012', '2013']:
					safe_exception_handler = e('LINK_SAFE_EXCEPTION_HANDLER')
					ElementTree.SubElement(link_node, 'ImageHasSafeExceptionHandlers').text = safe_exception_handler
		
		compile_node = ElementTree.SubElement(root, 'ItemGroup')
		header_node = ElementTree.SubElement(root, 'ItemGroup')
		assemble_node = ElementTree.SubElement(root, 'ItemGroup')
		custom_build_node = ElementTree.SubElement(root, 'ItemGroup')
		static_library_node = ElementTree.SubElement(root, 'ItemGroup')
		resource_node = ElementTree.SubElement(root, 'ItemGroup')
		
		for f in sorted(all_files, key=lambda x: x["filter_relative"]):
			if self._is_custom_build_file(f["tags"]):
				cl = ElementTree.SubElement(custom_build_node, 'CustomBuild',
				                            Include=f['project_relative'])
			elif self._is_header_file(f['pwd_relative']):
				cl = ElementTree.SubElement(header_node, 'ClInclude',
				                            Include=f['project_relative'])
			elif self._is_compiled_file(f['pwd_relative']):
				cl = ElementTree.SubElement(compile_node, 'ClCompile',
				                            Include=f['project_relative'])
			elif self._is_assembled_file(f['pwd_relative']):
				cl = ElementTree.SubElement(assemble_node, 'MASM',
				                            Include=f['project_relative'])
			elif self._is_static_library_file(f['pwd_relative']):
				cl = ElementTree.SubElement(static_library_node, 'Library',
				                            Include=f['project_relative'])
			elif self._is_resource_file(f['pwd_relative']):
				cl = ElementTree.SubElement(resource_node, 'ResourceCompile',
				                            Include=f['project_relative'])
			else:
				cl = None
			
			if cl is not None:
				for c in self.sorted_configurations():
					# If file is not included by current configuration, add "ExcludedFromBuild"
					# tag to this file for this configuration
					if not c.get_vs_full_identifier() in f["configurations"]:
						condition = r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier()
						ElementTree.SubElement(cl, 'ExcludedFromBuild',
						                       Condition=condition).text = 'true'
					
					# If file is included by current configuration and is custom build file,
					# add this file in custom build item group. 
					elif self._is_custom_build_file(f["tags"]):
						(custom_build_tool, custom_build_suffix, custom_build_option) = self._get_custom_build_tag(c, f)
						custom_build_filename = ntpath.basename(f['project_relative']) # windows path must use ntpath module
						src_suffix = os.path.splitext(custom_build_filename)[-1]
						objective_file = custom_build_filename.replace(src_suffix, custom_build_suffix)
						condition = r"'$(Configuration)|$(Platform)'=='%s'" % c.get_vs_full_identifier()
						ElementTree.SubElement(cl, 'Command', 
						                       Condition=condition).text = "%s %s %s -o $(SolutionDir)$(Configuration)\\VS%s\\%s" % \
						                      (custom_build_tool, custom_build_option, f['project_relative'],
						                       self._vs_version, objective_file)
						ElementTree.SubElement(cl, 'Outputs',
						                      Condition=condition).text = "$(SolutionDir)$(Configuration)\\VS%s\\%s" % \
						                      (self._vs_version, objective_file)
		
		if len(self._project.get_all_dependencies()) > 0:
			# TODO: This looks a bit excessive
			vc_proj_dependencies = []
			for d in self._project.get_all_dependencies():
				for other_proj_name in sorted(all_vc_projects.keys()):
					other_proj = all_vc_projects[other_proj_name]
					if other_proj.get_project().get_name() == d.get_name():
						if other_proj.has_any_configuration(self._configurations):
							if d.get_name() != self._project.get_name():
								if other_proj not in vc_proj_dependencies:
									vc_proj_dependencies.append(other_proj)
			
			node = ElementTree.SubElement(root, 'ItemGroup')
			for dep in vc_proj_dependencies:
				relative_path = path_ex.make_path_relative(dep._filename,
				                                           os.path.dirname(self._filename),
				                                           ntpath)
				res = ElementTree.SubElement(node, 'ProjectReference',
				                             Include=relative_path)
				ElementTree.SubElement(res, 'Project').text = "{%s}" % dep._guid
				ElementTree.SubElement(res, 'ReferenceOutputAssembly').text = "false"
		
		ElementTree.SubElement(root, 'Import', Project=r"$(VCTargetsPath)\Microsoft.Cpp.targets")
		
		extension_targets = ElementTree.SubElement(root, 'ImportGroup', Label='ExtensionTargets')
		if has_asm:
			ElementTree.SubElement(extension_targets, 'Import', Project=r'$(VCTargetsPath)\BuildCustomizations\masm.targets')
		
		path_ex.makedirs(os.path.dirname(self._filename))
		project_result = try_write.try_write(self._filename, ElementTree.tostring(root, 'utf-8'), text_mode=False, overwrite=True)
		self.projects_attempted += 1 
		if project_result == try_write.CHANGED:
			self.notify_write_out()
			self.projects_updated += 1
			print(" ok (updated)")
		elif project_result == try_write.NO_CHANGE:
			if self._verbose:
				self.notify_write_out()
				print(" ok")
		elif project_result == try_write.COULDNT_CHANGE:
			self.notify_write_out()
			self.projects_failed += 1 
			print(" couldn't update")
		
		filter_result = self.write_out_filters(path_transform)
		
		return max([project_result, filter_result])

	def write_out_filters(self, path_transform):
		
		root = ElementTree.Element('Project',
		                           ToolsVersion='4.0',
		                           xmlns='http://schemas.microsoft.com/developer/msbuild/2003')
		
		all_files = self._get_all_files(path_transform)
		filters_node = ElementTree.SubElement(root, 'ItemGroup')
		clcompile_node = ElementTree.SubElement(root, 'ItemGroup')
		clinclude_node = ElementTree.SubElement(root, 'ItemGroup')
		classemble_node = ElementTree.SubElement(root, 'ItemGroup')
		clcustom_build_node = ElementTree.SubElement(root, 'ItemGroup')
		clstatic_library_node = ElementTree.SubElement(root, 'ItemGroup')
		clresource_node = ElementTree.SubElement(root, 'ItemGroup')
		
		for f in sorted(all_files, key=lambda a: a["filter_relative"]):
			parts = path_ex.split_path(ntpath.dirname(f["filter_relative"]), ntpath)
			filter_path = None
			for i, part in enumerate(parts):
				if not filter_path:
					filter_path = part
				else:
					filter_path = ntpath.join(filter_path, part)
				filt = self._get_filter(filters_node, filter_path)
				if i+1 == len(parts):
					if self._is_custom_build_file(f['tags']):
						node = ElementTree.SubElement(clcustom_build_node, 'CustomBuild',
						                              Include=ntpath.normpath(f["project_relative"]))
					elif self._is_header_file(f['project_relative']):
						node = ElementTree.SubElement(clinclude_node, 'ClInclude',
						                              Include=ntpath.normpath(f["project_relative"]))
					elif self._is_compiled_file(f['project_relative']):
						node = ElementTree.SubElement(clcompile_node, 'ClCompile',
						                              Include=ntpath.normpath(f["project_relative"]))
					elif self._is_assembled_file(f['project_relative']):
						node = ElementTree.SubElement(classemble_node, 'MASM',
						                              Include=ntpath.normpath(f["project_relative"]))
					elif self._is_static_library_file(f['project_relative']):
						node = ElementTree.SubElement(clstatic_library_node, 'Library',
						                              Include=ntpath.normpath(f["project_relative"]))
					elif self._is_resource_file(f['project_relative']):
						node = ElementTree.SubElement(clresource_node, 'ResourceCompile',
						                              Include=ntpath.normpath(f["project_relative"]))
					else:
						node = None
					if node is not None:
						e = ElementTree.SubElement(node, 'Filter')
						e.text = filter_path
		
		path_ex.makedirs(os.path.dirname(self._filters_filename))
		result = try_write.try_write(self._filters_filename, ElementTree.tostring(root, 'utf-8'), text_mode=False, overwrite=True)
		if result == try_write.CHANGED:
			self.notify_write_out_filters()
			print(" ok (updated)")
		elif result == try_write.NO_CHANGE:
			if self._verbose:
				self.notify_write_out_filters()
				print(" ok")
		elif result == try_write.COULDNT_CHANGE:
			self.notify_write_out_filters()
			print(" couldn't update")

		return result

	def _get_filter(self, filter_node, filter_path):
		assert filter_path

		for child in filter_node.getchildren():
			if child.tag == 'Filter' and child.get('Include') == filter_path:
				return child

		filt = ElementTree.SubElement(filter_node, 'Filter',
		                              Include=filter_path)
		ident = ElementTree.SubElement(filt, 'UniqueIdentifier')
		identifier = visual_studio.deterministic_guid(filter_path).lower()
		ident.text = "{%s}" % identifier
		return filt


class Vc2005Project(VcProject):
	def __init__(self, *args, **kwargs):
		kwargs['vs_version'] = '2005'
		super(Vc2005Project, self).__init__(*args, **kwargs)

	def write_out(self, *args, **kwargs):
		return super(Vc2005Project, self).write_out(*args, **kwargs)

class Vc2008Project(VcProject):
	def __init__(self, *args, **kwargs):
		kwargs['vs_version'] = '2008'
		super(Vc2008Project, self).__init__(*args, **kwargs)

	def write_out(self, *args, **kwargs):
		return super(Vc2008Project, self).write_out(*args, **kwargs)

class Vc2010Project(VcxProject):
	def __init__(self, *args, **kwargs):
		kwargs['vs_version'] = '2010'
		super(Vc2010Project, self).__init__(*args, **kwargs)

	def write_out(self, *args, **kwargs):
		return super(Vc2010Project, self).write_out(*args, **kwargs)

class Vc2012Project(VcxProject):
	def __init__(self, *args, **kwargs):
		kwargs['vs_version'] = '2012'
		super(Vc2012Project, self).__init__(*args, **kwargs)

	def write_out(self, *args, **kwargs):
		return super(Vc2012Project, self).write_out(*args, **kwargs)
		
class Vc2013Project(VcxProject):
	def __init__(self, *args, **kwargs):
		kwargs['vs_version'] = '2013'
		super(Vc2013Project, self).__init__(*args, **kwargs)

	def write_out(self, *args, **kwargs):
		return super(Vc2013Project, self).write_out(*args, **kwargs)
