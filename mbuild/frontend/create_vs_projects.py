#!/usr/bin/env python

"""usage: %prog [options]

This script will create Visual Studio project and solution files for all of 
our bundles. 
"""

import optparse
import os
import sys
import re

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.visual_studio import driver
from src.visual_studio import visual_studio
from src.build import m2
from src.build import error_messages
from src.util import get_projects

def main(args):
	parser = optparse.OptionParser(__doc__)
	parser.add_option("-m", "--manifest", dest="manifest_path",
	                  action="store", default=os.path.join(BASE, 'manifest.mb'),
	                  help='Set the root manifest file to use.')
	parser.add_option("-o", "--output_dir", dest="output_dir", metavar="DIR",
	                  default=None, help="Choose a directory for created VS projects")
	parser.add_option("-b", "--binary-mode", dest="binary_mode", action="store_true", 
	                  help="Assume no newline translation will be done after generation (note: if checking files into perforce, then ensure they are marked as binary)")
	parser.add_option("-v", "--verbose_listing", dest="verbose_listing", action="store_true",
	                  default=False, help="Display all files checked, even if unchanged")
	
	parser.add_option("-r", "--restrict-projects", dest="restrict_projects", action="store",
	                  metavar="REGEXP", default=None, 
	                  help="Only regenerate projects with names matching REGEXP (be careful).")
	parser.add_option("-l", "--list-projects", dest="list_projects", action="store_true",
	                  default=False, help="Display all (restricted) projects")
	parser.add_option("-s", "--skip-non-writeable", dest="skip_non_writeable", action="store_true",
	                  default=False, help="Don't throw interactive questions when VS project file update failed for it is non-writeable.")
	
	options, args = parser.parse_args(args[1:])
	if len(args) > 0:
		parser.error("unexpected arguments %s" % args)
	
	newline = os.linesep
	if options.binary_mode:
		newline = '\r\n'
	
	# Load manifest
	try:
		manifest = m2.M2(options.manifest_path)
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
		force_dimensions = manifest.get_attribute(["default"], "MBUILD_MSVS_SUPPORT", m2.NoPaths())
		all_projects, project_loader = get_projects.get_projects(manifest, lambda x: True, force_dimensions)
	except error_messages.ProjectError, e:
		print str(e)
		return 1
	
	if options.list_projects:
		for project in all_projects:
			if project_filter(project.get_project_filename()):
				print "\t" + os.path.basename(project.get_project_filename())
		return 0
	
	try:
		path_transform = lambda x: x.get_filename()
		create_vs_projects(options.verbose_listing, options.output_dir, options.skip_non_writeable, \
		                   manifest, path_transform, all_projects, project_filter, {}, newline)
	
	except visual_studio.VsError, err:
		print str(err)
		return 1
	except error_messages.ManifestError, err:
		print str(err)
		return 1
	
	if options.restrict_projects:
		print error_messages.warning_about_restricting_projects()
	
	return 0

def create_vs_projects(verbose_listing, output_dir, skip_non_writeable, manifest, path_transform, all_projects, project_filter, dimensions, newlines):
	driver.make(verbose_listing, output_dir, skip_non_writeable, manifest, path_transform, all_projects, project_filter, dimensions, newlines)

if __name__ == '__main__':
	sys.exit(main(sys.argv))

