#!/usr/bin/env python

import os
import sys
import optparse

import process_source
import create_makefiles
import create_vs_projects

from src.build import error_messages
from src.build import m2

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))
DIMENSION_SEPARATOR = ':'

def main(args):
	parser = optparse.OptionParser(__doc__)

	parser.add_option("-m", "--manifest", dest="manifest",
	                  default=os.path.join(BASE, 'manifest.mb'),
	                  help="Choose a root manifest to use")
	parser.add_option("-v", "--verbose", dest="verbose", action="store_true", 
	                  default=False)					  
	parser.add_option("-r", "--report-file", dest="report_loc",
	                  default=None, help="Report file")
	parser.add_option("-w", "--preview", dest="preview", action="store_true",
	                  default=False, help="Generate report only, do not actually process files")
	parser.add_option("-p", "--projects", dest="projects", action="append",
					  default=[], help="Projects to release")
	parser.add_option("-d", "--dimensions", dest="dimensions", action="append",
	                  default=[], help="Dimensions to release")
	parser.add_option("-t", "--targetdir", dest="target_folder",
					  default=os.path.join(BASE, 'product'),
					  help="Root folder for move_to tags")
	(options, args) = parser.parse_args(args=args)
	
	dimensions = {}
	for raw_dimension in options.dimensions:
		assert DIMENSION_SEPARATOR in raw_dimension
		key, val = raw_dimension.split(DIMENSION_SEPARATOR)
		if not key in dimensions:
			dimensions[key] = []
		dimensions[key].append(val)
		
	try:
		manifest = m2.M2(options.manifest)
	except error_messages.ManifestError, e:
		print(str(e))
		return 1
	if options.verbose:
		print "Processing source..."
	ps = process_source.ProcessSource(options.target_folder, options.projects, dimensions)
	return ps.process(manifest=manifest, 
	                       plugins=['strip'], 
						   action_base='compile', 
						   verbose=options.verbose, 
						   preview=options.preview, 
						   report_loc=options.report_loc)
									  
if __name__ == '__main__':
	sys.exit(main(sys.argv))
