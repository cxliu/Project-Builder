#!/usr/bin/env python

import unittest
import os
import sys

THIS_DIR = os.path.join(os.path.dirname(__file__))
BASE = os.path.join(THIS_DIR, '..', '..')
sys.path.append(os.path.join(BASE))

from frontend import create_vs_projects
from src.util import path_ex

TESTCASES = os.path.join(BASE, "src", "test", "testcases")

class TestVisualStudio(unittest.TestCase):
	def _diff(self, reference, other):
		"""File diff. 
		Also handles DOS/UNIX line endings.
		"""
		
		try:
			f0 = open(reference, "rU")
		except IOError, err:
			assert False, "Error opening reference file: %s" % err
		try:
			f1 = open(other, "rU")
		except IOError, err:
			assert False, "Error opening file: %s" % err

		line_no = 1
		for line_0 in f0:
			line_1 = f1.readline()
			assert line_0 == line_1, \
				"%s and %s differ at line number %d (\n%s\n%s\n)" % (reference, other, line_no, line_0, line_1)
			
			line_no += 1

		assert not f1.readline(), "File %s is longer than %s" % (other, reference)

	def _test_visual_studio(self, key):
		"""Regression test of generated project/solution files
		"""
		manifest = os.path.join(TESTCASES, "backend", "input", "manifest.mb")
		output_dir = os.path.join(TESTCASES, "backend", "output")
		reference_dir = os.path.join(TESTCASES, "backend", "reference")
		
		self.failIf(create_vs_projects.main([None, "-m", manifest, "-o", output_dir]) != 0)
		
		num_diffs = 0
		for path, dirs, files in os.walk(reference_dir):
			for f in files:
				if os.path.splitext(f)[1] in ['.sln', '.vcproj', '.vcxproj', '.filters']:
					reference_file = os.path.join(path, f)
					new_file = reference_file.replace("reference", "output")
					self._diff(reference_file, new_file)
					num_diffs += 1

		self.failIf(num_diffs == 0)

	def test_visual_studio_backend(self):
		self._test_visual_studio("backend")
	
def main(args):
	
	visual_studio_suite = unittest.TestLoader().loadTestsFromTestCase(TestVisualStudio)
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(visual_studio_suite)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
