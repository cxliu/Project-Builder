#!/usr/bin/env python
import unittest
import os
import sys

THIS_DIR = os.path.join(os.path.dirname(__file__))
BASE = os.path.join(THIS_DIR, '..', '..')
sys.path.append(os.path.join(BASE, "src", "build"))

import m2
import error_messages

TESTCASES = os.path.join(BASE, "src", "test", "testcases")

class ManifestTest(unittest.TestCase):
	def __init__(self, root_manifest, path_type, queries, error_expected=None):
		unittest.TestCase.__init__(self)
		self._root = root_manifest
		self._queries = queries
		self._path_type = path_type
		self._error_expected = error_expected
	
	def shortDescription(self):
		return "%s (%d queries)" % (self._root, len(self._queries))
	
	@staticmethod
	# get_file_tags() can be used until we have an m2 API for the tags
	def _get_file_tags(m, keywords, qfile, path_type):
		files, attribs, keys = m._clauses.solve(keywords, ignore_errors=False)
		for file in files:
			if os.path.basename(file.get_filename()) == qfile:
				raw_tags = file.get_tags()
				fixed_tags = []
				for t in raw_tags:
					raw_filename = t[2]
					fixed_filename = path_type.write_path(raw_filename)
					this_tag = (t[0], t[1], fixed_filename)
					fixed_tags.append(this_tag)
				return fixed_tags
		return []
	
	def runTest(self):
		try:
			m = m2.M2(os.path.join(THIS_DIR, self._root))
			
			for q in self._queries:
				qtype = q[0]
				keywords = q[1]
				expected = None
				
				try:
					if qtype == 'files':
						expected = q[2]
						result = [f.get_path(self._path_type) for f in m.get_file_set(keywords)]
				
					elif qtype == 'release_files':
						expected = q[2]
						result = [f.get_path(self._path_type) for f in m.get_release_files(keywords)]
				
					elif qtype == 'file_tags':
						expected = q[3]
						result = self._get_file_tags(m, keywords, q[2], self._path_type)
					
					elif qtype == 'attribute':
						expected = q[3]
						result = m.get_attribute(keywords, q[2], self._path_type)
					
					elif qtype == 'keyword_doc':
						expected = q[2]
						result = m.get_doc_text(m2.Documentation.KEYWORD, keywords)
					else:
						raise Exception("Broken test, qtype = '" + str(qtype) + "'")
					self.failUnlessEqual(result, expected,
							 "Keywords = " + str(q[1]) +
							 ". Got " + str(result) +
						 	". Expected " + str(expected))
				except Exception as e:
					if isinstance(expected, type):
						if isinstance(e, expected):
							return
					raise
		except Exception as e:
			if self._error_expected != None:
				if not isinstance(e, self._error_expected):
					raise
				return
			else:
				raise

		self.failUnlessEqual(self._error_expected, None, \
			'This test executed "successfully", but was expected to fail with ' + str(self._error_expected))

		self.failUnlessEqual(result, expected, "Expected %s, but got %s" % (str(expected), 
			                                                                str(result)))

def setup_m2_suite():
	suite = unittest.TestSuite()
	
	suite.addTest(ManifestTest(
		'testcases/basic_sections/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'basic_sections')),
		[
			('files', ['a'], ['b', 'c', 'l', 'q']),
			('files', ['d'], ['e', 'f', 'm']),
			('files', ['a', 'd'], ['o', 'p', 'r', 'b', 'c', 'e', 'f', 'l', 'm', 'q']),
			('files', ['g'], []),
			('files', ['h'], []),
			('files', ['a', 'd', 'h', 'g'], ['k', 'o', 'p', 'r', 'b', 'c', 'e', 'f', 'i', 'j', 'l', 'm', 'q'])]))
	
	suite.addTest(ManifestTest(
		'testcases/attributes/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'attributes')),
		[
			('attribute', ['a'], 'mystring', 'a'),
			('attribute', ['a', 'b'], 'mystring', 'q'),
			('attribute', ['a'], 'mypath', 'b'),
			('attribute', ['a'], 'mylist', ['c', 'd']),
			('attribute', ['a', 'b'], 'mylist', ['e', 'c', 'd']),
			('attribute', ['a'], 'mymap', { 'x': 'g', 'y': 'h' }),
			('attribute', ['a', 'b'], 'mymap', { 'x': 'g', 'y': 'h', 'z': 'i' }),
			('attribute', ['a'], 'mypathmap', { 'a': 'a', 'b': 'b' }),
			('attribute', ['a'], 'mypathlist', [ 'a', 'b' ]),
			('attribute', ['a'], 'mylistmap', { 'x': ['j'] }),
			('attribute', ['a', 'b'], 'mylistmap', { 'x': ['k','j'] }),
			('attribute', ['a'], 'mydifficultlist', [r'xyz', r'\(xyz\)']),
			('attribute', ['a'], 'mydifficultmap', { 'a': r'xyz', 'b': r'\(xyz\)' }),
			('attribute', ['a'], 'ELEMENT', 'hydrogen'),
			('attribute', ['a', 'c'], 'ELEMENT', 'helium'),
			('attribute', ['a'], 'LANGUAGE', ['eng', 'fr']),
			('attribute', ['a'], 'WAVEFORM', { 'a': 'saw', 'b': 'sine' })
		]))
	
	suite.addTest(ManifestTest(
		'testcases/ambiguous_attributes/manifest.mb',
		m2.NoPaths(),
		[
			('attribute', ['a'], 'CANT_DECIDE', error_messages.PriorityError),
			('attribute', ['b'], 'WHICH_ONE', error_messages.PriorityError),
		]))
	
	suite.addTest(ManifestTest(
		'testcases/import/one.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'import')),
		[
			('files', ['a'], ['b', 'm']),
			('files', ['a', 'f'], ['g', 'b', 'm']),
			('files', ['a', 'd'], ['b', 'm']),
			('files', ['c'], []),
			('files', ['c', 'd'], ['e']),
			('files', ['c', 'd', 'k'], ['l', 'e'])]))
	
	suite.addTest(ManifestTest(
		'testcases/add/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'add')),
		[
			('files', ['a'], ['one']),
			('files', ['b'], []),
			('files', ['a', 'b'], ['one']),
			('files', ['a', 'c'], ['three', 'one', 'two']),
			('files', ['b', 'c'], ['two']),
			('files', ['a', 'd'], ['three', 'one']),
			('files', ['a', 'd', 'j'], ['three', 'one', 'four']),
			('files', ['e', 'f', 'b', 'j'], ['one', 'four'])
		]))
	
	suite.addTest(ManifestTest(
		'testcases/doc/manifest.mb', 
		m2.NoPaths(),
		[
			('keyword_doc', 'multi_line', 'A leaf falls.'),
			('keyword_doc', 'raw', 'Patience, Grasshopper.'),
			('keyword_doc', 'one_line', 'The sixth sick sheik\'s sixth sheep\'s sick.'),
			('keyword_doc', 'escape', 'Listen twice, play once.'),
			('keyword_doc', 'raw_multi_line', 'Back to the\nbeginning.'),
		]))
	
	suite.addTest(ManifestTest(
		'testcases/doc_parse_error/doc_parse_error.mb', 
		m2.NoPaths(),
		[
			('keyword_doc', 'no_escape', 'Listen twice, play once.')
		],
		error_messages.ParseError))
	
	# section_header+colon+text
	suite.addTest(ManifestTest(
		'testcases/section_header+colon+text/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'section_header+colon+text')),
		[
			('files', ['bar'], ['B'])]))
	
	# multiple_tags
	suite.addTest(ManifestTest(
		'testcases/multiple_tags/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'multiple_tags')),
		[
			('release_files', ['foo'], ['some_other_file.txt'])]))
	
	# section_tags
	suite.addTest(ManifestTest(
		'testcases/section_tags/manifest.mb', 
		m2.RelativeLocalPath(os.path.join(TESTCASES)),
		[
			('file_tags', ['a'], 'foo.c', [('no_arg_tag', None, os.path.join('section_tags'))]),
			('file_tags', ['b'], 'foo.c', [('one_arg_tag', ['a1'], os.path.join('section_tags')),
			                               ('one_arg_tag2', ['a2'], os.path.join('section_tags'))]),
			('file_tags', ['b'], 'bar.c', [('one_arg_tag', ['a1'], os.path.join('section_tags')),
			                               ('one_arg_tag2', ['a2'], os.path.join('section_tags'))]),
			('file_tags', ['b'], 'sub.c', [('one_arg_tag', ['a1'], os.path.join('section_tags')),
			                               ('one_arg_tag2', ['a2'], os.path.join('section_tags')),
			                               ('subtag', None, os.path.join('section_tags', 'subdir'))]),
			('file_tags', ['c'], 'foo.c', [('two_arg_tag', ['p1', 'p2'], os.path.join('section_tags'))]),
			('file_tags', ['d'], 'foo.c', [('two_arg_tag', ['p1', 'p2'], os.path.join('section_tags')),
			                               ('no_arg_tag', None, os.path.join('section_tags'))]),
			('file_tags', ['d'], 'bar.c', [('two_arg_tag', ['p1', 'p2'], os.path.join('section_tags'))]),
		]))
	
	suite.addTest(ManifestTest(
		'testcases/expression_parse/manifest.mb',
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'expression_parse')),
		[
			('files', [], ([])),
			('files', ['a'], ['a1', 'a2', 'a3', 'a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_or_b_and_c']),
			('files', ['b'], ['a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3']),
			('files', ['c'], ['a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_and_b_or_c']),
			('files', ['a', 'b'], ['a_and_b1', 'a_and_b2', 'a_and_b3', 'a_and_b4', 'a_and_b5', 'a_and_b6', 'a_and_b7', 'a_and_b_or_c', 'a1', 'a2', 'a3', 'a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_or_b_and_c']),
			('files', ['b', 'c'], ['a_or_b_and_c', 'a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_and_b_or_c']),
			('files', ['c', 'a'], ['a1', 'a2', 'a3', 'a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_or_b_and_c', 'a_and_b_or_c']),
			('files', ['a', 'b', 'c'], ['a_and_b_and_c1', 'a_and_b_and_c2', 'a_and_b_and_c3', 'a_and_b1', 'a_and_b2', 'a_and_b3', 'a_and_b4', 'a_and_b5', 'a_and_b6', 'a_and_b7', 'a_and_b_or_c', 'a1', 'a2', 'a3', 'a_or_b1', 'a_or_b2', 'a_or_b3', 'a_or_b4', 'a_or_b5', 'a_or_b6', 'a_or_b7', 'a_or_b_or_c1', 'a_or_b_or_c2', 'a_or_b_or_c3', 'a_or_b_and_c'])
		]))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['a'], 'ATTR', '1')],
		error_messages.PriorityError))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['a', 'c'], 'ATTR', '2')],
		error_messages.PriorityError))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['a', 'd'], 'ATTR', '1')],
		error_messages.PriorityError))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['a', 'c', 'd'], 'ATTR', '1')],
		error_messages.PriorityError))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['a', 'd', 'e'], 'ATTR', '2')],
		error_messages.PriorityError))
	
	suite.addTest(ManifestTest(
		'testcases/priority/manifest.mb',
		m2.NoPaths(),
		[('attribute', ['d', 'e'], 'ATTR', '3')]))
	
	suite.addTest(ManifestTest(
		'testcases/filenames/manifest.mb',
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'filenames')),
		[('files', ['default'], [
			'file name with spaces',
			'tagged file name with spaces',
			'file name with multiple tags and spaces',
			'file name with parameterised tag and spaces',
			'file name with spaces and extension.txt',
			'tagged file name with spaces and extension.txt',
			'file name with multiple tags and spaces and extension.txt',
			'file name with parameterised tag and spaces and extension.txt',
			'filename(with parentheses)',
			'filename(with parentheses, commas, etc)',
			'filename(with unbalanced parentheses',
			'file name(with space and parentheses)',
			'file name(with space, parentheses, commas, etc)',
			'file name(with space and unbalanced parentheses',
			'(file name in parentheses)',
			'.filename_starting_with_dot',
			'.filename starting with dot and with spaces'])]))
	
	suite.addTest(ManifestTest(
		'testcases/whitespace/manifest.mb',
		m2.RelativeLocalPath(os.path.join(TESTCASES, 'whitespace')),
		[('files', ['simple'], [
			'filename_with_unquoted_spaces_at_start.c',
			'filename_with_unquoted_spaces_at_end.c',
			'filename with internal spaces.c',
			'filename with unquoted spaces internally and externally.c',
			'unquoted_spaces.c',
			'unquoted_tabs.c',
			'  filename with quoted spaces.c  ',
			'  filename with alternatively quoted spaces.c  ',
			'  filename with some quoted and some unquoted spaces  ']),
		 ('files', ['tagged'], [
			'tagged_filename_with_spaces_at_start.c',
			'tagged_filename_with_spaces_at_end.c',
			'  tagged_filename_with_quoted_spaces_at_start.c',
			'tagged_filename_with_quoted_spaces_at_end.c  ',
			'  tagged filename with quoted spaces and unquoted spaces  ']),
		 ('files', ['tagged_with_args'], [
			'tagged_filename_with_args_and_spaces_at_start.c',
			'tagged_filename_with_args_and_spaces_at_end.c',
			'  tagged_filename_with_args_and_quoted_spaces_at_start.c',
			'tagged_filename_with_args_and_quoted_spaces_at_end.c  ',
			'  tagged filename with args and quoted spaces and unquoted spaces  ']),
		 ]))
	
	return suite


def main(args):
	
	m2_suite = setup_m2_suite()
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(m2_suite)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
