#!/usr/bin/env python
import unittest
import os
import sys

THIS_DIR = os.path.join(os.path.dirname(__file__))
BASE = os.path.join(THIS_DIR, '..', '..')
sys.path.append(os.path.join(BASE))

from frontend import create_doc
from src.util import path_ex

TESTCASES = os.path.join(BASE, "src", "test", "testcases")

class TestCreateDoc(unittest.TestCase):
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

	def test_create_doc(self):
		manifest = os.path.join(TESTCASES, "backend", "input", "manifest.mb")
		target = os.path.join(TESTCASES, "backend", "output", "doc.html")
		ref = os.path.join(TESTCASES, "backend", "reference", "doc.html")
		
		self.failIf(create_doc.main([None, "-m", manifest, "-f", target]) != 0)
		self._diff(ref, target)
		


def main(args):
	
	doc_suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDoc)
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(doc_suite)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
