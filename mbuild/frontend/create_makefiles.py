#!/usr/bin/env python

"""usage: %prog [options]

This will generate makefiles for all configurations of all projects.
"""

import optparse
import os
import sys
import re

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.build import m2
from src.build import p2
from src.make import t3
from src.build import plugin_manager
from src.build import error_messages
from src.make import make
from src.util import get_projects
from src.util import path_ex

def main(args):
	parser = optparse.OptionParser(__doc__)
	parser.add_option("-m", "--manifest", dest="manifest",
	                  default=os.path.join(BASE, 'manifest.mb'),
	                  help="Choose a root manifest to use")
	parser.add_option("-o", "--output_dir", dest="makefile_root",
	                  default=None, help="Choose a directory for created makefiles")
	parser.add_option("-p", "--profile", dest="profile",
	                  default=False, action="store_true",
	                  help="Run with cProfile.")
	parser.add_option("-v", "--verbose_listing", dest="verbose_listing", action="store_true",
	                  default=False, help="Display all files checked, even if unchanged")
	parser.add_option("-r", "--restrict-projects", dest="restrict_projects", action="store",
	                  metavar="REGEXP", default=None, 
	                  help="Only regenerate projects with names matching REGEXP (be careful).")
	parser.add_option("-l", "--list-projects", dest="list_projects", action="store_true",
	                  default=False, help="Display all (restricted) projects")
	parser.add_option("-s", "--skip-non-writeable", dest="skip_non_writeable", action="store_true",
	                  default=False, help="Don't throw interactive questions when Makefile update failed for the file is non-writeable.")
	
	(options, args) = parser.parse_args(args=args)
	
	# Load manifest
	try:
		manifest = m2.M2(options.manifest)
	except error_messages.ManifestError, e:
		print(str(e))
		return 1
	
	# Initial project loader
	project_filter = lambda x: True
	if options.restrict_projects:
		rexp = re.compile(options.restrict_projects)
		project_filter = lambda x: not rexp.search(x) is None
	
	# Load (restricted) project files
	try:
		force_dimensions = manifest.get_attribute(["default"], "MBUILD_MAKE_SUPPORT", m2.NoPaths())
		projects, project_loader = get_projects.get_projects(manifest, project_filter, force_dimensions)
	except error_messages.ProjectError, e:
		print str(e)
		return 1
	
	if options.list_projects:
		for project in projects:
			print "\t" + os.path.basename(project.get_project_filename())
		return 0
	
	# Create the function to do makefile creation, this way we can either run
	# it directly, or get the profiler to run it
	do_it = lambda: create_makefiles(options.verbose_listing, options.makefile_root, options.skip_non_writeable, \
	                                 manifest, projects, project_loader, {})
	
	if options.profile:
		import cProfile
		profiler = cProfile.Profile(builtins=False)
		try:
			profiler.runcall(do_it)
		finally:
			_display_profile_info(profiler.getstats())
			ret = 0
	else:
		try:
			ret = do_it()
		except error_messages.ManifestError, e:
			print(str(e))
			return 1
	
	if options.restrict_projects:
		print error_messages.warning_about_restricting_projects()
	return ret
	
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

def create_makefiles(verbose_listing, makefile_root, skip_non_writeable, manifest, projects, project_loader, dimensions):
	# Load plugins
	try:
		t3_plugin_manager = plugin_manager.PluginManager(manifest, t3, [])
	except plugin_manager.PluginError, err:
		print "Couldn't create makefiles due to error in plugin loading:"
		print str(err)
		return 1
	
	# Generate Makefiles
	total_number_attempted = 0
	total_number_written = 0
	total_number_failed = 0
	failed_makefiles = {}

	try:
		for project in projects:
			m = make.Make(project,t3_plugin_manager, verbose_listing)
			m.write_out(manifest, makefile_root, dimensions, project_loader, failed_makefiles)
			total_number_attempted += m.number_attempted
			total_number_written += m.number_written
			total_number_failed += m.number_failed
		
		if len(failed_makefiles) > 0 and not skip_non_writeable:
			number_written = make.regenerate_failed_makefiles(manifest, t3_plugin_manager, project_loader, failed_makefiles, verbose_listing)
			total_number_written += number_written
			total_number_failed  -= number_written
	except (error_messages.ManifestError, make.MakeError), e:
		print(str(e))
		return 1
		
	print("\n---\n")
	print("Makefiles checked: %d, updated: %d, failed %d" % (total_number_attempted, total_number_written, total_number_failed))
	
	if total_number_failed > 0:
		print("\nWARNING: Some files could not be updated!")

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))

