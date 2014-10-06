#!/usr/bin/env python

"""usage: %prog [options] project1 [project2 [project3 [...]]]

This will create a python file for every named project. The python file contains information about the different configurations in each project.

The result is a completely standalone file (i.e no dependencies on M-Build), so it can be shipped without M-Build.
"""

import optparse
import os
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import m2
from src.build import p2
from src.build import plugin_manager
from src.build import error_messages

from src.visual_studio import vc_configuration

def main(args):
	parser = optparse.OptionParser(__doc__)
	parser.add_option("-m", "--manifest", dest="manifest",
	                  default=os.path.join(BASE, 'manifest.mb'),
	                  help="Choose a root manifest to use")
	parser.add_option("-o", "--output_dir", dest="build_info_root",
	                  default=None, help="Choose a directory for created build info files")
	parser.add_option("--profile", dest="profile",
	                  default=False, action="store_true",
	                  help="Run with cProfile.")
	
	(options, args) = parser.parse_args(args=args)
	
	if len(args) <= 1:
		parser.error("You must specify at least one project to produce build info for.")
	
	# Load manifest
	try:
		manifest = m2.M2(options.manifest)
	except error_messages.ManifestError, e:
		print(str(e))
		return 1
	
	do_it = lambda: create_build_info_files(manifest, options.build_info_root, args[1:])
	
	if options.profile:
		import cProfile
		profiler = cProfile.Profile(builtins=False)
		try:
			profiler.runcall(do_it)
		finally:
			_display_profile_info(profiler.getstats())
			ret = 0
	else:
		ret = do_it()
	
	return ret


def create_build_info_files(manifest, build_info_root, projects):
	# Load plugins
	p2_plugin_manager = plugin_manager.PluginManager(manifest, p2, [])
	project_loader = p2.ProjectLoader(manifest, p2_plugin_manager)

	for p in projects:
		project = project_loader.get_project(p)

		write_build_info(manifest, project)
	
	return 0

def str_ordered(dictionary):
	"""Returns the equivalent to repr(dictionary), but with the keys in sorted
	order"""
	ret = "{%s}" % ", ".join(['%r: %r' % (k, dictionary[k]) for k in sorted(dictionary.keys())])
	return ret

def write_build_info(manifest, project):
	configurations = p2.Project.get_configurations(project)
	
	out = []
	out.append("'''Build information for %s" % project.get_name())
	out.append('build_info is a list of tuples, each tuple is of the form:')
	out.append('')
	out.append('  (id, configuration, filename, extra)')
	out.append('')
	out.append('With:')
	out.append('            id: A string unique to this configuration')
	out.append(' configuration: A dictionary mapping dimension names to values')
	out.append('      filename: The filename (relative to BASE) of the output')
	out.append('         extra: Tool specific data for building')
	out.append('                 if configuration["tool"] is "make" then')
	out.append('                   extra=([executables], [variables])')
	out.append('                   With:')
	out.append('                     executables: a list of executables that need')
	out.append('                       to exist in your $PATH in order to build')
	out.append('                       this configuration.')
	out.append('                     variables: a list of environment variables')
	out.append('                       that must be set in order to build this')
	out.append('                       configuration.')
	out.append('                 if configuration["tool"] is "msvs*" then')
	out.append('                   extra=(proj_filename, configuration_name)')
	out.append('                   With:')
	out.append('                     proj_filename: the file name of either')
	out.append('                       the .sln file or the .vcproj/.vcxproj')
	out.append('                       file (for static libraries).')
	out.append('                     configuration_name: the name of the build')
	out.append('                       configuration as used by Visual Studio.')
	out.append("'''")
	out.append('')
	out.append('import os')
	out.append('BASE = os.path.dirname(__file__)')
	out.append('')
	out.append('# There are %d configurations here' % len(configurations))
	out.append('build_info = \\')
	out.append('\t[')
	
	msvs_version = {"msvs2005":"2005"
	               ,"msvs2008":"2008"
	               ,"msvs2010":"2010"
	               ,"msvs2012":"2012"
				   ,"msvs2013":"2013"}
	
	for config in configurations:
		action = 'use'
		if not action in project.get_actions():
			raise ValueError("Project type is unknown")
		output_name = project.get_output_name(action, config)
		if config['tool'] in ['msvs2005', 'msvs2008', 'msvs2010', 'msvs2012', 'msvs2013']:
			ext = os.path.splitext(output_name[-1])[1]
			output_name[-1] = project.get_identifier(config, ['tool', 'toolchain', 'os', 'processor'])
			output_name.append(None)
			output_name.append(project.get_name() + ext)
			
			version = msvs_version[config['tool']]
			output_name[-2] = 'vs%s' % version
			
			project_file_name = "%s_%s" % (project.get_name(), version)
			if ext == '.lib':
				if version in ['2005', '2008']:
					project_file_name += '.vcproj'
				else:
					project_file_name += '.vcxproj'
			else:
				project_file_name += '.sln'
			
			vc_config = vc_configuration.VcConfiguration(manifest, project, config, version)
			vs_config_name = vc_config.get_vs_full_identifier()
			
			extra = (project_file_name, vs_config_name)
			out.append('\t\t(%r, %s, %r, %r),' % (project.get_identifier(config, []), str_ordered(config), output_name, extra))
		
		elif config['tool'] == 'make':
			extra_executables = ['make',
			         project.get_attribute(config, 'MAKE_CC', m2.NoPaths(), False),
			         project.get_attribute(config, 'MAKE_LD', m2.NoPaths(), False),
			         project.get_attribute(config, 'MAKE_AS', m2.NoPaths(), False),
			         project.get_attribute(config, 'MAKE_AR', m2.NoPaths(), False)]
			extra_variables = project.get_attribute(config, 'MAKE_REQUIRE_ENVIRONMENT_VARIABLES', m2.NoPaths(), False)
			extra = (extra_executables, extra_variables)
			out.append('\t\t(%r, %s, %r, %r),' % (project.get_identifier(config, []), str_ordered(config), output_name, extra))
		else:
			raise ValueError("tool: %r is unknown" % (config['tool']))
	out.append('\t]')
	out.append('')
	
	filename = os.path.splitext(project.get_project_filename())[0] + '.py'
	f = open(filename, 'w')
	try:
		for line in out:
			f.write(line + '\n')
	finally:
		f.close()
	

def _display_profile_info(info):
	# cProfile seems to have a different interface in my pypy and my python
	# interpreter. This gives us a consistent interface:
	if isinstance(info[0], tuple):
		code_fn = lambda stat: stat[0]
		inline_time_fn = lambda stat: stat[4]
	else:
		code_fn = lambda stat: stat.code
		inline_time_fn = lambda stat: stat.inlinetime
		
	calls_by_tot_time = sorted(info, cmp=lambda a, b: cmp(inline_time_fn(b), inline_time_fn(a)))
	
	for c in calls_by_tot_time:
		print "%6f  %s" % (inline_time_fn(c), code_fn(c))


if __name__ == '__main__':
	sys.exit(main(sys.argv))

