#!/usr/bin/env python
import unittest
import os
import sys

THIS_DIR = os.path.join(os.path.dirname(__file__))
BASE = os.path.join(THIS_DIR, '..', '..')
sys.path.append(os.path.join(BASE))

from frontend import create_makefiles
from src.util import path_ex

TESTCASES = os.path.join(BASE, "src", "test", "testcases")

class TestCreateMakefile(unittest.TestCase):
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

	def test_makefile(self):
		"""Regression test of generated makefiles
		"""
		manifest = os.path.join(TESTCASES, "backend", "input", "manifest.mb")
		output_dir = os.path.join(TESTCASES, "backend", "output")
		reference_dir = os.path.join(TESTCASES, "backend", "reference")
		
		self.failIf(create_makefiles.main(['', "-m", manifest, "-o", output_dir]) != 0)
		
		num_diffs = 0
		for path, dirs, files in os.walk(reference_dir):
			relative_path = path_ex.make_path_relative(path, reference_dir, os.path)
			output_path = os.path.join(output_dir, relative_path)
			
			for f in files:
				if f == 'Makefile':
					reference_file = os.path.join(path, f)
					output_file = os.path.join(output_path, f)
					self._diff(reference_file, output_file)
					num_diffs += 1
		
		self.failIf(num_diffs == 0)

def main(args):
	
	makefiles_suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateMakefile)
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(makefiles_suite)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
