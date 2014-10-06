#!/usr/bin/env python
import unittest
import sys

from test_m2 import setup_m2_suite
from test_p2 import setup_p2_suite
from test_create_doc import TestCreateDoc
from test_create_makefiles import TestCreateMakefile
from test_create_vs_project import TestVisualStudio

def main(args):

	m2_suite = setup_m2_suite() # 19 tests for m2 unit test
	p2_suite = setup_p2_suite()
	doc_suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDoc)
	makefiles_suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateMakefile)
	visual_studio_suite = unittest.TestLoader().loadTestsFromTestCase(TestVisualStudio)
	
	all_tests = unittest.TestSuite([m2_suite, p2_suite, doc_suite, makefiles_suite, visual_studio_suite])
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(all_tests)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
