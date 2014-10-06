"""M2 is the library for parsing manifest files. Conceptually, you point it
at a tree containing manifests, and then given a list of keywords it can
answer questions such as:

 - Which files are interesting? (get_files)
 - What is the value of attribute x? (get_attribute)

Using this, you can make programs for generating build files for most (all?)
build environments. 
"""

import os
import fnmatch
import error_messages
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE))

from src.util import path_ex

class PathType(object):
	"""A PathType is an object which converts a path (as used by the os.path
	module) into a path for a different purpose (e.g. writing into a Makefile).
	"""
	def __init__(self, relative_to):
		assert isinstance(relative_to, str)
		self._relative_to = relative_to
	
	def write_path(self, path):
		raise NotImplementedError("This is an abstract class")
		
	def write_path_from_info(self, file_info):
		raise NotImplementedError("This is an abstract class")
	
	def basename(self, path):
		raise NotImplementedError("This is an abstract class")

class WindowsPath(PathType):
	def write_path(self, path):
		import ntpath
		return path_ex.convert_path(path_ex.make_path_relative(path, self._relative_to, os.path), os.path, ntpath)
	
	def write_path_from_info(self, file_info):
		assert isinstance(file_info, FileInfo)
		return self.write_path(file_info.get_filename())
		
	def basename(self, path):
		import ntpath
		return ntpath.basename(path)

class PosixPath(PathType):
	def write_path(self, path):
		import posixpath
		return path_ex.convert_path(path_ex.make_path_relative(path, self._relative_to, os.path), os.path, posixpath)
	
	def write_path_from_info(self, file_info):
		assert isinstance(file_info, FileInfo)
		return self.write_path(file_info.get_filename())
		
	def basename(self, path):
		import posixpath
		return posixpath.basename(path)

class LocalPath(PathType):
	"""A path relative to the current working directory, in the native format.
	"""
	def __init__(self):
		pass
	
	def write_path(self, path):
		return path_ex.make_path_relative(path, os.getcwd(), os.path)
	
	def write_path_from_info(self, file_info):
		assert isinstance(file_info, FileInfo)
		return self.write_path(file_info.get_filename())
		
	def basename(self, path):
		return os.path.basename(path)

class RelativeLocalPath(PathType):
	def write_path(self, path):
		return path_ex.make_path_relative(path, self._relative_to, os.path)
	
	def write_path_from_info(self, file_info):
		assert isinstance(file_info, FileInfo)
		return self.write_path(file_info.get_filename())
		
	def basename(self, path):
		return os.path.basename(path)

class NoPaths(PathType):
	"""If this PathType is used, then any attempts to read paths will result in
	a RequiredPathType exception."""
	def __init__(self):
		pass
	
	def write_path_from_info(self, path):
		raise error_messages.RequiredPathType(path)
	
	def basename(self, path):
		raise error_messages.RequiredPathType(path)

class TransformPath(PathType):
	"""This composes another PathType with some extra logic to allow a user
	specified transform to be applied to the path."""
	def __init__(self, base_path, transform):
		assert isinstance(base_path, PathType)
		assert callable(transform)
		self._base_path = base_path
		self._transform = transform
	
	def write_path(self, path):
		return self._transform(FileInfo(self._base_path.write_path(path), None, None))
		
	def write_path_from_info(self, file_info):
		assert isinstance(file_info, FileInfo)
		new_file_info = FileInfo(self._base_path.write_path_from_info(file_info), file_info.get_keywords(), file_info.get_tags())
		return self._transform(new_file_info)
	
	def basename(self, path):
		return self._base_path.basename(path)

class AttrDict(object):
	"""This emulates a dict, containing all the values of attributes for
	a set of keywords.
	"""
	def __init__(self, m2, keywords, path_type, attr_names):
		assert isinstance(m2, M2)
		assert all([isinstance(k, str) for k in keywords])
		assert isinstance(path_type, PathType)
		assert isinstance(attr_names, list)
		assert all([isinstance(a, str) for a in attr_names])
		self._m2 = m2
		self._keywords = keywords
		self._attr_names = attr_names
		self._path_type = path_type
		self._cache = {}
	
	def __len__(self):
		return len(self._attr_names)
	
	def __contains__(self, key):
		return key in self._attr_names
	
	def __getitem__(self, key):
		if not isinstance(key, str):
			raise TypeError("Expected type 'str', was given '%s'" % repr(key))
		if not key in self._attr_names:
			raise KeyError()
		if not key in self._cache:
			self._cache[key] = self._m2.get_attribute(self._keywords, key, 
			                                          self._path_type,
			                                          allow_unfound=True)
		
		return self._cache[key]
	
	def keys(self):
		return list(self._attr_names)

class M2(object):
	SEP = ' [+] '
	def __init__(self, root_manifest):
		"""This will parse the set of manifests, giving an object which
		can be queried to get all of the details of it.
		"""
		self._loud = False  # print debug information
		self._defines = {}
		self._docs = {}
		self._enums = {}
		for doc_type in Documentation.valid_types:
			self._docs[doc_type] = {}
		self._clauses = ClauseSet()
		self._solution_cache = {}
		self._manifest_files = set()
		self._root_manifest = root_manifest
		
		reporter = ManifestReport(self._add_define,
		                          self._add_implication,
		                          self._add_attribute,
		                          self._add_file,
		                          self._add_manifest,
		                          self._add_error,
		                          self._add_doc,
		                          self._add_enum_entry,
		                          self.get_enums)
		
		p = os.path.dirname(os.path.normpath(root_manifest))
		if p == '.':
			p = ''
		m = Manifest(root_manifest, None, [], p, reporter, None, None)
	
	def _get_solution(self, keywords):
		# TODO: It might be a good idea to shrink the cache sometimes.
		key_str = self.SEP.join(sorted(keywords))
		if not key_str in self._solution_cache:
			self._solution_cache[key_str] = self._clauses.solve(keywords, ignore_errors=False)
		
		return self._solution_cache[key_str]
	
	def get_root_manifest(self):
		return self._root_manifest
	
	def find_file(self, keywords, path_type, filename):
		assert all([isinstance(k, str) for k in keywords])
		assert isinstance(path_type, PathType)
		assert isinstance(filename, str)
		for f in self.get_file_set(keywords, condition=lambda fo: path_type.basename(fo.get_filename()) == filename):
			return f.get_path(path_type)
	
	def find_file_pattern(self, keywords, path_type, pattern):
		assert all([isinstance(k, str) for k in keywords])
		assert isinstance(path_type, PathType)
		assert isinstance(pattern, str)
		return [f.get_path(path_type) 
		        for f 
		        in self.get_file_set(keywords, condition=lambda fo: fnmatch.fnmatch(fo.get_filename(), pattern))]
	
	def _get_file_outcome_list(self, keywords, tag=None, exclude_tags=[], obey_exclusive=True, condition=lambda fo: True):
		assert all([isinstance(k, str) for k in keywords])
		assert tag is None or isinstance(tag, str)
		assert isinstance(exclude_tags, list)
		assert all([isinstance(k, str) for k in exclude_tags])
		assert obey_exclusive is True or obey_exclusive is False
		
		files, attributes, expanded_keywords = self._get_solution(keywords)
		
		# Told to exclude the same tag we were told to return
		if not tag is None and tag in exclude_tags:
			return []
		
		# Get the initial list of files
		candidates = []
		for f in files:
			if not tag is None:
				if any([tag == t[0] for t in f.get_tags()]):
					candidates.append(f)
			elif len(set(exclude_tags).intersection([t[0] for t in f.get_tags()])) == 0:
				candidates.append(f)
		
		if obey_exclusive:
			# The "exclusive" tag has special meaning.
			# Any files marked with it are given an id. If only one file
			# with this id will be returned. The id for a file will be
			# its filename by default, but if the exlusive tag was given
			# an argument, then the argument is the id.
			# Ties are broken based on keyword precedences
			exclusives = {}
			nonexclusive = []
			while len(candidates) > 0:
				f = candidates.pop()
			
				exclusive_id = f.get_exclusive_id()
				if exclusive_id is None:
					nonexclusive.append(f)
				else:
					if not exclusive_id in exclusives:
						exclusives[exclusive_id] = set()
					exclusives[exclusive_id].add(f)
			
			ret = nonexclusive
			for exclusive_id in exclusives:
				choices = exclusives[exclusive_id]
				poset = OutcomePoset(expanded_keywords)
				for ch in choices:
					poset.add_outcome(ch)
				ret.append(poset.supremum())
		else:
			# Don't need to process exclusivity
			ret = candidates
		
		# Remove files that don't match condition
		old_len = len(ret)
		ret = [fo for fo in ret if condition(fo)]
		
		# Sort files in order
		poset = OutcomePoset(expanded_keywords)
		for file_outcome in ret:
			poset.add_outcome(file_outcome)
		
		return poset.in_order()

	def get_file_set(self, keywords, tag=None, 
	                 exclude_tags=[], obey_exclusive=True,
	                 condition=lambda fo: True):
		file_outcome_list = self._get_file_outcome_list(keywords, tag, exclude_tags, obey_exclusive, condition)
		# The order for the files returned is priority order (as used for attribute resolution).
		assert(isinstance(file_outcome_list, list))
		assert(all([isinstance(f, FileOutcome) for f in file_outcome_list]))
		return [FileInfo(f.get_filename(), keywords, f.get_tags()) for f in file_outcome_list]

	def get_release_files(self, keywords, tag=None):
		"""This will return a set of files to release, this is similar to 
		get_file_set, except we don't remove duplicate versions of source files.
		We also don't include files tagged 'internal', unless specifically asked
		for them.
		"""
		if tag == 'internal':
			exclude = []
		else:
			exclude = ['internal']
		ret = self.get_file_set(keywords, tag, exclude, obey_exclusive=False)
		
		return ret
	
	def get_manifests(self):
		return self._manifest_files
	
	def _get_manifest_set(self):
		return self._manifest_files
	
	def get_all_attributes(self, keywords, path_type):
		"""Returns a dictionary containing all the attributes defined.
		"""
		assert all([isinstance(k, str) for k in keywords])
		assert isinstance(path_type, PathType)
		return AttrDict(self, keywords, path_type, self._defines.keys())
		
	def get_attribute(self, keywords, key, path_type, allow_unfound=False):
		"""Returns a string. For an attribute to be valid, we need to be able
		to determine its type. This is done by assignment syntax: '=' means a
		scalar string value, 'p""' means a path, '+=' means a list of strings
		or paths, '(key)=' means a map from key to a string or path."""
		assert all([isinstance(k, str) for k in keywords])
		assert isinstance(key, str)
		assert isinstance(path_type, PathType), "%r is not a %r (it is a %s)" % (path_type, PathType, type(path_type))
		assert allow_unfound is True or allow_unfound is False
		
		if not key in self._defines:
			return None
		def_ = self._defines[key]
		
		files, attributes, expanded_keywords = self._get_solution(keywords)
		
		choices = set()
		for attr in attributes:
			if attr.get_key() == key:
				choices.add(attr)
		
		poset = OutcomePoset(expanded_keywords)
		for c in choices:
			poset.add_outcome(c)
		
		if key in self._enums:
			enum = set(self._enums[key].keys())
		else:
			enum = None

		ret = def_.get_value(expanded_keywords, path_type, poset, enum)
		if not ret is None:
			return ret
		
		if allow_unfound:
			return None
		
		raise error_messages.UnsetAttributeError(key)
	
	def _get_enum(self, attribute):
		if attribute in self._enums:
			return self._enums[attribute]
		return None
	
	def expand_keywords(self, keywords):
		files, attributes, expanded_keywords = self._get_solution(keywords)
		return expanded_keywords
	
	def _add_define(self, define):
		if define.get_name() in self._defines:
			old_define = self._defines[define.get_name()]
			if old_define.get_data_type() != define.get_data_type():
				raise error_messages.MultipleDefinitionError(old_define, define)
		self._defines[define.get_name()] = define
	
	def _add_doc(self, doc):
		doc_type = doc.get_type()
		doc_key = doc.get_key()
		assert doc_type in self._docs
		if doc_key in self._docs[doc_type]:
			raise error_messages.MultipleDocumentationError(self._docs[doc_type][doc_key], doc)
		self._docs[doc_type][doc_key] = doc
			
	def _add_enum_entry(self, enum, key, value, pos):
		if not enum in self._enums:
			self._enums[enum] = {}
		if key in self._enums[enum]:
			raise error_messages.MultipleEnumError(enum, key, pos)
		self._enums[enum][key] = value
			
	def get_enums(self):
		return self._enums

	def get_doc_text(self, type_, key):
		assert type_ in self._docs
		if key in self._docs[type_]:
			return self._docs[type_][key].get_text()
		else:
			return ''

	def get_docs(self):
		return self._docs
	
	def _add_implication(self, keyword_expression, keyword, position):
		self._clauses[keyword_expression].add_implies(keyword, position)
		
		if self._loud:
			print "%s => %s" % (keyword_expression, keyword)
			print "# Position:%s\n" % (position)
	
	def _add_attribute(self, keyword_expression, attribute_outcome):
		assert isinstance(attribute_outcome, AttributeOutcome)
		self._clauses[keyword_expression].add_attribute(attribute_outcome)
		
		if self._loud:
			print "%s => %s" % (keyword_expression, attribute_outcome)
	
	def _add_file(self, keyword_expression, file_outcome):
		assert isinstance(file_outcome, FileOutcome)
		self._clauses[keyword_expression].add_file(file_outcome)
		
		if self._loud:
			print "%s => %s" % (keyword_expression, file_outcome)
	
	def _add_manifest(self, filename):
		assert(isinstance(filename, str))
		self._manifest_files.add(filename)
	
	def _add_error(self, keyword_expression, message, pos):
		self._clauses[keyword_expression].add_error(message, pos)
		
		if self._loud:
			print "%s => Error: %r" % (keyword_expression, message)

class Token(object):
	(ERROR, EOF, HEADER_KEYWORD_STRING, SECTION_STRING,
	 DIRECTIVE_STRING, DIRECTIVE_KEY, DIRECTIVE_VALUE_PATH, DIRECTIVE_VALUE_STRING,
	 LEFT_BRACKET, RIGHT_BRACKET, EQ, LT, GT, COLON, APPEND_OPERATOR,
	 LEFT_PAREN, RIGHT_PAREN, NEWLINE, DOT, PLUS, COMMA, DIRECTIVE, LEFT_BRACE, RIGHT_BRACE, WHITESPACE,
	) = range(25)
	
	SIMPLE_TOKENS = {
	            '[': LEFT_BRACKET
	            ,']': RIGHT_BRACKET
	            ,'(': LEFT_PAREN
	            ,')': RIGHT_PAREN
	            ,':': COLON
	            ,'=': EQ
	            ,'.': DOT
	            ,',': COMMA
	            ,'>': GT
	            ,'<': LT
	            ,'\n': NEWLINE
	            ,'{': LEFT_BRACE
	            ,'}': RIGHT_BRACE}
	
	def __init__(self, type_, value, position):
		self._type = type_
		self._value = value
		self._position = position
	
	def is_(self, type_):
		return self._type == type_
	
	def get_value(self):
		return self._value
	
	def __str__(self):
		return "[%d: %s (%s)]" % (self._type, repr(self._value), self._position)



class KeywordExpression(object):
	"""This is the recursive type which represents the parse tree of
	a keyword boolean expression.
	An object of this class is either a keyword identifier, or
	a '+' or '.' node with left and right subtrees.
	"""
	def __init__(self, identifier, children):
		self._identifier = identifier
		#if identifier in [Token.PLUS, Token.DOT]:
			#assert all([isinstance(c, KeywordExpression) for c in children]), "One of the children was not a KeywordExpression: %r" % children
		self._children = children
		
		# If we ever convert to sum of products form, then this is generally
		# useful, so we hold on to it
		self._sum_of_products_form = None
		self._canonical_form = None
		
		# Most of the time, we are just a product of things, in these cases
		# we can simplify many of our slowest functions
		# Note that modifying this to also special case out an expression which
		# is just a primary expression actually seems to (marginally) harm
		# the performance. Make sure you profile before doing anything silly.
		self._all_product = None
		if self._identifier == Token.DOT:
			for c in self._children:
				if c._identifier == Token.DOT or c._identifier == Token.PLUS:
					return
			self._all_product = [c._identifier for c in self._children]
	
	def identical_to_allowing_false_negatives(self, other):
		if self._all_product and other._all_product:
			return self._all_product == other._all_product
		return False
	
	def duplicate(self):
		if self._identifier in [Token.PLUS, Token.DOT]:
			return KeywordExpression(self._identifier, [c.duplicate() for c in self._children])
		else:
			return KeywordExpression(self._identifier, None)
	
	def __str__(self):
		if self._is_sum():
			return "(%s)" % '+'.join([str(c) for c in self._children])
		elif self._is_product():
			return "(%s)" % '.'.join([str(c) for c in self._children])
		else:
			return self._identifier
	
	def get_canonical_form(self):
		"""The canonical form for a KeywordExpression is a sum of products
		representation, with each product being sorted with no duplicate 
		predicates. The sum has the products sorted (by python's standard
		sort order for lists of strings), and no duplicate products.
		"""
		if not self._canonical_form is None:
			return self._canonical_form
		sop = self.get_sum_of_products()
		
		# Sort and remove duplicates in products
		products = []
		for p in sop._children:
			prod = sorted(set([c._identifier for c in p._children]))
			products.append(prod)
		
		# Sort and remove duplicates in sum
		products.sort()
		for i in reversed(range(len(products) - 1)):
			if products[i] == products[i + 1]:
				del products[i + 1]
		
		# Convert everything to KeywordExpressions
		eproducts = []
		for prod in products:
			eprod = KeywordExpression(Token.DOT, [KeywordExpression(p, []) for p in prod])
			eproducts.append(eprod)
		self._canonical_form = KeywordExpression(Token.PLUS, eproducts)
		
		# If we just have 1 product, then canonical form leaves out the sum
		if len(products) == 1:
			self._canonical_form = eproducts[0]
		
		return self._canonical_form
	
	def simplify(self, given, true_keyword="default"):
		# This will reduce a keyword expresion to a simpler form
		# assuming that the keywords in "given" are all set.
		if self.satisfied(given):
			return KeywordExpression(true_keyword, [])
		
		if self._is_sum():
			simplified_children = [c.simplify(given) for c in self._children]
			
			if any([c.satisfied(given) for c in simplified_children]):
				return KeywordExpression(true_keyword, [])
			
			# TODO: Check for subsets:
			# e.g. (a)+(a.b) => a
			return KeywordExpression(Token.PLUS, simplified_children)
		if self._is_product():
			simplified_children = [c.simplify(given) for c in self._children]
			
			interesting_children = []
			for c in simplified_children:
				if not c.satisfied(given):
					interesting_children.append(c)
			
			if len(interesting_children) == 0:
				return KeywordExpression(true_keyword, [])
			
			# TODO: Check for equivalence:
			# e.g. (a).(a) => a
			return KeywordExpression(Token.DOT, interesting_children)
		
		return self.duplicate()
	
	def satisfied(self, keywords):
		# These asserts are valid, but too costly for performance
		#assert all([isinstance(k, str) for k in keywords])
		#assert isinstance(keywords, set)
		
		if not self._all_product is None:
			for k in self._all_product:
				if not k in keywords:
					return False
			return True
		
		if self._is_sum():
			ret = any([c.satisfied(keywords) for c in self._children])
		elif self._is_product():
			ret = all([c.satisfied(keywords) for c in self._children])
		else:
			ret = self._identifier in keywords
		
		return ret

	def get_keywords(self):
		"""Returns: Set of all keywords in this expression. This method is intended only for
		use in things like working out which keywords are relevant for displaying in an error
		message."""
		if self._is_primary():
			return set([self._identifier])
		else:
			ret = set([])
			for c in self._children:
				ret = ret | c.get_keywords()
			return ret
	
	def get_sum_of_products_as_list(self):
		"""Like get_sum_of_products() but returns a list of KeywordExpressions
		which are products.
		"""
		if not self._sum_of_products_form is None:
			return self._sum_of_products_form._children
		
		if not self._all_product is None:
			# We are a product of primaries
			ret = [self]
		elif self._is_sum():
			# A sum of sums of products can just be flattened
			# We could simplify it by removing duplicate products.
			child_sums = [c.get_sum_of_products() for c in self._children]
			children = []
			for c in child_sums:
				children += c._children
			ret = children
		elif self._is_product():
			# A product of sums of products requires finding each possible combination
			# of products.
			child_sums = [c.get_sum_of_products() for c in self._children]
			groups = [c._children for c in child_sums]
			
			ret = self._multiply_children(groups)
		else:
			# Trivial case for primary expressions:
			ret = [KeywordExpression(Token.DOT, 
			         [KeywordExpression(self._identifier, [])])]
		
		# Save in the cache
		self._sum_of_products_form = KeywordExpression(Token.PLUS, ret)
		self._sum_of_products_form._sum_of_products_form = self._sum_of_products_form
		
		return ret

	
	@staticmethod
	def is_sum_of_products_as_list(list_):
		if not isinstance(list_, list):
			return False
		for c in list_:
			if not c.is_product_of_primaries():
				return False
		return True
	
	def is_product_of_primaries(self):
		if not self._is_product():
			return False
		for c in self._children:
			if not c._is_primary():
				return False
		return True
	
	def is_sum_of_products(self):
		if not self._is_sum():
			return False
		
		return KeywordExpression.is_sum_of_products_as_list(self._children)
	
	def get_product_keywords(self):
		# This assert is valid, but expensive, so it is commented out 
		#assert self.is_product_of_primaries(), "get_product_keywords() requires product of keywords"
		return frozenset([c._identifier for c in self._children])
		
	
	def get_sum_of_products(self):
		"""Returns a new KeywordExpression with a "sum" node as the root
		and all children being "product" nodes, with "primary" node keys.
		This is not quite a canonical form (e.g. "((a.b)+(b.a))" vs "((a.b))")
		but is a useful step in that direction.
		"""
		if self._sum_of_products_form is None:
			self._sum_of_products_form = KeywordExpression(Token.PLUS, self.get_sum_of_products_as_list())
			# This assert is valid, but expensive, so it is commented out 
			#assert self._sum_of_products_form.is_sum_of_products()
			
			# Make a circular link, since something in sum of products form, is
			# already in sum of products form
			self._sum_of_products_form._sum_of_products_form = self._sum_of_products_form
		
		return self._sum_of_products_form
	
	@staticmethod
	def _pg(groups):
		return str([str(g) for g in groups])
	
	@staticmethod
	def _pgg(groups):
		return str([KeywordExpression._pg(g) for g in groups])
	
	@staticmethod
	def _multiply_children(groups, indent=0):
		if len(groups) == 0:
			return []
		
		if len(groups) == 1:
			return groups[0]
		
		first_group = groups[0]
		rest_groups = groups[1:]
		
		rest_multiplied = KeywordExpression._multiply_children(rest_groups, indent+2)
		ret = []
		for i in first_group:
			for r in rest_multiplied:
				ret.append(KeywordExpression(Token.DOT, i._children + r._children))
		
		return ret
	
	def _is_primary(self):
		if self._identifier in [Token.PLUS, Token.DOT]:
			return False
		return True
	
	def _is_sum(self):
		return self._identifier == Token.PLUS
	
	def _is_product(self):
		return self._identifier == Token.DOT


class Clause(object):
	def __init__(self, keyword_expression):
		assert isinstance(keyword_expression, KeywordExpression)
		
		self._keyword_expression = keyword_expression
		self._implies = set()
		self._files = []
		self._values = {}
		self._errors = []
	
	def add_implies(self, keyword, position):
		assert isinstance(keyword, str)
		self._implies.add((keyword, position))
	
	def add_attribute(self, attribute_outcome):
		assert isinstance(attribute_outcome, AttributeOutcome)
		key = attribute_outcome.get_key()
		value = attribute_outcome.get_value()
		if not key in self._values:
			self._values[key] = []
		self._values[key].append(attribute_outcome)
	
	def add_file(self, file_outcome):
		assert isinstance(file_outcome, FileOutcome)
		self._files.append(file_outcome)
	
	def add_error(self, message, pos):
		self._errors.append((message, pos))
	
	def get_implies(self, ignore_errors):
		if not ignore_errors:
			self._handle_errors()
		return self._implies
	
	def get_files(self, ignore_errors):
		if not ignore_errors:
			self._handle_errors()
		return self._files
	
	def get_attribute_dict(self, ignore_errors):
		if not ignore_errors:
			self._handle_errors()
		return self._values
	
	def get_keyword_expression(self):
		return self._keyword_expression
	
	def _handle_errors(self):
		if len(self._errors) > 0:
			message = ""
			for e in self._errors:
				message += '%s: @error %r' % (e[1], e[0])
			
			raise error_messages.ManifestError(message)
	
	def satisfied(self, keywords):
		# These asserts are valid, but expensive
		#assert all([isinstance(k, str) for k in keywords])
		#assert isinstance(keywords, set)

		return self._keyword_expression.satisfied(keywords)
	
	def __str__(self):
		return "[[%s]: %d files. %d implications. %d values]" % (
		       self._keyword_expression, len(self._files), len(self._implies), 
		       len(self._values))


class OutcomePoset(object):
	"""Strictly speaking, an outcome poset is an outcome strict poset, in that
	the relation is a '<' rather than a '<='. This class works out the ordering
	between outcomes, for a given set of keywords.
	"""
	def __init__(self, keywords):
		# These asserts are valid, but expensive
		#assert all([isinstance(k, str) for k in keywords])
		
		self._keywords = keywords
		self._outcomes = []
	
	def duplicate(self):
		ret = OutcomePoset(list(self._keywords))
		ret._outcomes = [o.duplicate() for o in self._outcomes]
		return ret
	
	def add_outcome(self, outcome):
		assert isinstance(outcome, Outcome)
		self._outcomes.append(outcome)
	
	def supremum(self):
		# Special cases for performance
		if len(self._outcomes) == 1:
			return self._outcomes[0].duplicate()
		if len(self._outcomes) == 2:
			result = self._higher_priority(self._outcomes[0], self._outcomes[1])
			if not result is None:
				return result.duplicate()
		
		remaining = [c.duplicate() for c in self._outcomes]
		if len(remaining) == 0:
			return None
		
		while len(remaining) > 1:
			break_out = False
			for i, i_obj in enumerate(remaining):
				for j, j_obj in enumerate(remaining):
					if i < j:
						winner = self._higher_priority(i_obj, j_obj)
						if not winner is None:
							remaining[j] = winner
							del remaining[i]
							break_out = True
							break
				if break_out:
					break
				
			if not break_out:
				raise error_messages.PriorityError(self._keywords, remaining)
		
		return remaining[0]
	
	def in_order(self):
		# TODO: We should just keep the outcomes sorted in file order
		remaining = [o.duplicate() for o in self._outcomes]
		
		# Sort outcomes according to file position
		remaining.sort(cmp=self._file_order_cmp)
		
		# Sort according to priorities (this could be made faster)
		ret = []
		while len(remaining) > 0:
			top = self._pop_top(remaining)
			ret.append(top)
		
		return ret
	
	def _pop_top(self, items):
		assert len(items) > 0
		top = items[0]
		top_index = 0
		i = 1
		while i < len(items):
			if self._higher_priority(top, items[i]) is items[i]:
				top_index = i
				top = items[i]
			i += 1
		
		del items[top_index]
		return top
	
	def _higher_priority(self, choice1, choice2):
		"""This returns choice1, choice2 or None.
		depending on which choice is higher priority (or None if undefined).
		"""
		# These asserts are valid, but expensive
		#assert isinstance(choice1, Outcome)
		#assert isinstance(choice2, Outcome)
		
		if choice1.is_default and choice2.is_default:
			return None
		
		# This is a simple case which we can handle very quickly
		if choice1.get_keyword_expression().identical_to_allowing_false_negatives(choice2.get_keyword_expression()):
			return None
		
		# TODO: This should work on expanded keywords, not raw keywords
		# however that is too slow at the moment.
		k1 = choice1.get_keyword_expression().get_sum_of_products_as_list()
		k2 = choice2.get_keyword_expression().get_sum_of_products_as_list()
		
		# Drop out bits that aren't satisfied
		k1 = [k for k in k1 if k.satisfied(self._keywords)]
		k2 = [k for k in k2 if k.satisfied(self._keywords)]
		
		# Check for a product in k1/k2 which beats everything in k2/k1
		foo = None
		all_k2_wins = [True] * len(k2)
		for kk1 in k1:
			all_k1_wins = True
			for i in xrange(len(k2)):
				kk2 = k2[i]
				winner = self._higher_priority_product(kk1, kk2)
				if not winner is kk1:
					all_k1_wins = False
				
				if not winner is kk2:
					all_k2_wins[i] = False
			
			if all_k1_wins:
				return choice1
		
		if any(all_k2_wins):
			return choice2
		
		return None
	
	def _higher_priority_product(self, choice1, choice2):
		k1 = choice1.get_product_keywords()
		k2 = choice2.get_product_keywords()
		
		# Get keywords that aren't shared between the two choices
		distinct = k1 ^ k2
		
		# Narrow down to just the keywords we have
		distinct &= set(self._keywords)
		
		# If one choice has keyword(s) that the other doesn't have, then it
		# has a higher priority. If both have distinct keywords, then we
		# can't make a decision yet.
		if len(distinct & k1) > 0 and len(distinct & k2) == 0:
			return choice1
		elif len(distinct & k2) > 0 and len(distinct & k1) == 0:
			return choice2
		
		return None
	
	def _file_order_cmp(self, choice1, choice2):
		# Valid, but in performance critical code
		#assert isinstance(choice1, Outcome)
		#assert isinstance(choice2, Outcome)
		
		if choice1 > choice2:
			return -1
		elif choice2 > choice1:
			return 1
		else:
			return 0
	
	def pop_supremum(self):
		ret = self.supremum()
		if ret is None:
			return ret
		
		old_len = len(self._outcomes)
		self._outcomes = [o for o in self._outcomes if not o == ret]
		assert old_len - 1 == len(self._outcomes), "Removed %d items in pop" % (old_len - len(self._outcomes))
		
		return ret
	
	def __len__(self):
		return len(self._outcomes)

class Outcome(object):
	"""An outcome can be thought of as a side effect of a clause. If that
	clause is active (i.e. its keyword expression is true) then an outcome
	is also active.
	"""
	
	# Cache this value for speeding up some operations
	__default = KeywordExpression(Token.DOT, [KeywordExpression("default", None)])
	
	def __init__(self, keyword_expression, position):
		assert isinstance(keyword_expression, KeywordExpression)
		assert isinstance(position, Position)
		
		self._keyword_expression = keyword_expression
		self._position = position
		
		if keyword_expression.identical_to_allowing_false_negatives(self.__default):
			self.is_default = True
		else:
			self.is_default = False
	
	def duplicate(self):
		return Outcome(self._keyword_expression.duplicate(), self._position.duplicate())
		
	
	def get_position(self):
		return self._position
	
	def __str__(self):
		simplified_keyword = self._keyword_expression.simplify(set(['default']))
		return "# Position: %s\n# Simplified keyword:%s\n" % (self._position, simplified_keyword)
	
	def get_keyword_expression(self):
		return self._keyword_expression
	
	def __cmp__(self, other):
		return cmp(other._position, self._position)

class FileInfo(object):
	def __init__(self, filename, keywords, tags):
		assert filename is not None
		self._filename = filename
		
		if tags is None:
			self._tags = None
		else:
			self._tags = list(tags)
		
		if keywords is None:
			self._keywords = None
		else:
			self._keywords = list(keywords)

	def get_path(self, path_type):
		assert isinstance(path_type, PathType)
		return path_type.write_path_from_info(self)
		
	def get_filename(self):
		return self._filename
		
	def get_tags(self):
		if self._tags is not None:
			return self._tags
		else:
			return []
		
	def get_keywords(self):
		if self._keywords is not None:
			return self._keywords
		else:
			return []
			
	def __str__(self):
		return "[FileInfo: %s]" % (self._filename)

class FileOutcome(Outcome):
	def __init__(self, keyword_expression, position, filename, tags):
		assert isinstance(filename, str)
		assert isinstance(tags, list)
		assert all([self._well_formed_tag(t) for t in tags])
		
		Outcome.__init__(self, keyword_expression, position)
		self._tags = tags
		self._filename = filename
	
	def duplicate(self):
		tag_dup = list(self._tags)
		
		return FileOutcome(self._keyword_expression.duplicate(), 
		                   self._position.duplicate(),
		                   self._filename,
		                   tag_dup)
	
	@staticmethod
	def _well_formed_tag(t):
		name, args, path = t
		if not isinstance(name, str):
			return False
		if args is None:
			pass
		elif not all([isinstance(arg, str) for arg in args]):
			return False
		if not isinstance(path, str):
			return False
		return True
	
	def get_tags(self):
		return self._tags
			
	def get_filename(self):
		return self._filename
	
	def get_exclusive_id(self):
		for t in self._tags:
			if t[0] == 'exclusive':
				if t[1] is None or len(t[1]) == 0:
					return os.path.basename(self._filename)
				elif len(t[1]) == 1:
					return t[1][0]
				else:
					raise error_messages.ExclusiveTagError("Too many arguments.", self._position)
			elif t[0] == 'internal':
				return None
		return os.path.basename(self._filename)
	
	def __str__(self):
		ret = ""
		if len(self._tags) == 0:
			ret += "%s\n" % (self._filename)
		else:
			tags = []
			for t in self._tags:
				this_tag = t[0]
				if not t[1] is None:
					this_tag += '(' + ','.join(t[1]) + ')'
				
			ret += "%s:%s\n" % (' '.join(tags), self._filename)
		ret += super(FileOutcome, self).__str__()
		return ret

class AttributeOutcome(Outcome):
	def __init__(self, keyword_expression, position, key, value, path):
		Outcome.__init__(self, keyword_expression, position)
		self._key = key
		self._value = value
		self._path = path

	def duplicate(self):
		return AttributeOutcome(self._keyword_expression.duplicate(),
		                        self._position.duplicate(),
		                        self._key,
		                        self._value,
		                        self._path)
	
	def get_key(self):
		return self._key
	
	def get_value(self):
		return self._value
	
	def get_path(self):
		return self._path
		
	def __str__(self):
		ret = "@att %s=%s\n" % (self._key, self._value)
		ret += super(AttributeOutcome, self).__str__()
		return ret
	

class ClauseSet(object):
	def __init__(self):
		self._clauses = {}
		self._solve_called = False
		self._impl_clauses = []
		self._other_clauses = []
	
	def __getitem__(self, key):
		if not isinstance(key, KeywordExpression):
			raise TypeError()
		
		canonical_key = key.get_canonical_form()
		full_name = str(canonical_key)
		if not full_name in self._clauses:
			# adding Clauses is only expected until first solve() call
			assert self._solve_called is False
			self._clauses[full_name] = Clause(canonical_key)
		return self._clauses[full_name]
	
	def __iter__(self):
		return self._clauses.itervalues()
	
	def solve(self, seed, ignore_errors):
		"""This will take a set of keywords, which are taken as facts, and
		use them to give a tuple containing files, attribute values and
		keywords.
		"""
		assert all([isinstance(k, str) for k in seed])

		if not self._solve_called:
			# initialize _impl_clauses and _other_clauses
			for c in self._clauses.values():
				if c.get_implies(ignore_errors=True):
					self._impl_clauses.append(c)
				else:
					self._other_clauses.append(c)
			self._solve_called = True
		
		# only clauses with implications may contribute to truth updates
		leftover = self._impl_clauses[:]

		files = set()
		attribute_values = set()
		attribute_dict = {}
		
		truth = set(seed)
		num_facts = -1
		while len(truth) != num_facts:
			clauses = leftover
			leftover = []
			num_facts = len(truth)
			while len(clauses) > 0:
				c = clauses.pop()
				if c.satisfied(truth):
					truth.update([imp[0] for imp in c.get_implies(ignore_errors)])
					files.update(c.get_files(ignore_errors))
					new_values = c.get_attribute_dict(ignore_errors)
					for v in new_values.itervalues():
						attribute_values.update(set(v))
				else:
					leftover.append(c)
		
		# check other clauses (i.e. without implications) with expanded truth
		for c in self._other_clauses:
			if c.satisfied(truth):
				files.update(c.get_files(ignore_errors))
				new_values = c.get_attribute_dict(ignore_errors)
				for v in new_values.itervalues():
					attribute_values.update(set(v))
		
		return (files, attribute_values, truth)
	
	def __str__(self):
		ret = ''
		for k in sorted(self._clauses.keys()):
			ret += str(self._clauses[k]) + '\n'
		ret += "(%d clauses)\n" % len(self._clauses)
		return ret

class ManifestReport(object):
	def __init__(self, add_define, add_implication, add_directive_value, add_file, add_manifest, 
	             add_error, add_doc, add_enum_entry, get_enums):
		self.add_define = add_define
		self.add_implication = add_implication
		self.add_directive_value = add_directive_value
		self.add_file = add_file
		self.add_manifest = add_manifest
		self.add_error = add_error
		self.add_doc = add_doc
		self.add_enum_entry = add_enum_entry
		self.get_enums = get_enums


class Manifest(object):
	def __init__(self, f, implied_condition, implied_tags, path, reporter, parent, parent_pos):
		"""implied_condition: A keyword expression which will be ANDed with
		the keyword expression of each section header in the manifest file."""
		assert isinstance(f, str)
		assert isinstance(reporter, ManifestReport)
		assert implied_condition == None or \
		       isinstance(implied_condition, KeywordExpression)
		
		self._parent = parent
		self._parent_pos = parent_pos
		self._reporter = reporter
		self._reporter.add_manifest(f)
		self._filename = f
		try:
			tok = Tokeniser(f)
		except IOError, err:
			raise error_messages.ManifestIOError(err, parent, parent_pos)
		try:
			self._parse_globals(tok)
			self._parse_sections(tok, implied_condition, implied_tags, path)
			tok.expect(Token.EOF)
		finally:
			tok.close()
	
	def get_importer(self):
		return (self._parent, self._parent_pos)
	
	def get_filename(self):
		return os.path.normpath(self._filename)
	
	def _parse_globals(self, tok):
		while True:
			self._eat_whitespace(tok)
			t = tok.peek()
			if not t.is_(Token.DIRECTIVE):
				return
			if t.get_value() == '@doc':
				self._parse_doc(tok)
			elif t.get_value() == '@enum':
				self._parse_enum(tok)
			else:
				raise error_messages.ParseError("Read '%s' in global section (these must appear in sections)" % t.get_value(), tok.position)
	
	def _parse_doc(self, tok):
		# Read 
		pos = tok.position.duplicate()
		t = tok.expect(Token.DIRECTIVE)
		tok.allow_whitespace()
		doc_type_str = tok.expect(Token.DIRECTIVE_STRING, "doc spec").get_value()
		tok.allow_whitespace()
		doc_key = tok.expect(Token.DIRECTIVE_KEY, "doc key").get_value()
		tok.allow_whitespace()
		tok.expect(Token.EQ, "doc value assignment")
		tok.allow_whitespace()
		doc_text = tok.expect(Token.DIRECTIVE_VALUE_STRING, "doc_text").get_value()
		doc_type = Documentation.get_type_from_string(doc_type_str, pos)
		self._reporter.add_doc(Documentation(type_=doc_type, 
		                                     key=doc_key,
		                                     text=doc_text,
		                                     position=pos))
	 
	def _parse_enum(self, tok):
		pos = tok.position.duplicate()
		t = tok.expect(Token.DIRECTIVE)
		assert t.get_value() == '@enum'
		enum_spec = tok.expect(Token.DIRECTIVE_STRING, "enum spec").get_value()
		try:
			enum, entry = enum_spec.split('.')
		except ValueError:
			raise error_messages.ParseError("Invalid enum spec: %s" % enum_spec, pos)
		tok.allow_whitespace()
		tok.expect(Token.EQ, "enum assignment")
		tok.allow_whitespace()
		description = tok.expect(Token.DIRECTIVE_VALUE_STRING, "enum description").get_value()
		self._reporter.add_enum_entry(enum, entry, description, pos)
	
	def _parse_sections(self, tok, implied_condition, implied_tags, path):
		while not tok.peek().is_(Token.EOF):
			header = self._parse_section_header(tok, implied_condition, path)
			self._parse_section_contents(tok, header, implied_tags, path)
	
	def _parse_section_header(self, tok, implied_condition, path):
		"""Returns: Keyword expression for this header"""
		tok.expect(Token.LEFT_BRACKET, "section heading")

		# Read keywords
		keyword_expression = self._parse_keyword_expression(tok)
		
		if implied_condition != None:
			keyword_expression = KeywordExpression(Token.DOT,
			                                       [implied_condition, keyword_expression])
			keyword_expression = keyword_expression.get_canonical_form()
		
		tok.expect(Token.RIGHT_BRACKET, "end of section heading")
		return keyword_expression

	def _parse_keyword_expression(self, tok):
		"""Parses a boolean expression according to the grammar
		Expr := Term
		Expr := Term '+' Expr
		Term := Factor
		Term := Factor '.' Term
		Factor := '(' Expr ')'
		Factor := Identifier

		Returns: KeywordExpression
		"""
		term = self._parse_keyword_term(tok)
		if tok.peek().is_(Token.PLUS):
			tok.expect(Token.PLUS)
			expression = self._parse_keyword_expression(tok)
			return KeywordExpression(Token.PLUS, [term, expression])
		else:
			return term
			
	def _parse_keyword_term(self, tok):
		factor = self._parse_keyword_factor(tok)
       		if tok.peek().is_(Token.DOT):
			tok.expect(Token.DOT)
			term = self._parse_keyword_term(tok)
			return KeywordExpression(Token.DOT, [factor, term])
		else:
			return factor

	def _parse_keyword_factor(self, tok):
		if tok.peek().is_(Token.LEFT_PAREN):
			tok.expect(Token.LEFT_PAREN)
			expression = self._parse_keyword_expression(tok)
			tok.expect(Token.RIGHT_PAREN, "')'")
			return expression
		else:
			identifier = tok.expect(Token.HEADER_KEYWORD_STRING, "identifier").get_value()
			return KeywordExpression(identifier, [])
		
	def _parse_section_tags(self, tok, header, implied_tags, path):
		tok.expect(Token.COLON, "section tags")
		
		# Read tags
		pos = tok.position.duplicate()
		tags = list(implied_tags)
		while True:
			t = tok.peek()
			if t.is_(Token.NEWLINE):
				# This must be the end of the tags
				tok.expect(Token.NEWLINE)
				break
			t = tok.expect(Token.SECTION_STRING, "tag").get_value()
			
			if tok.peek().is_(Token.LEFT_PAREN):
				args, unused_text = self._parse_tag_arguments(tok)
			else:
				args = None
			
			if len(tok.allow_whitespace()) > 0:
				tags.append((t, args, path))
			elif tok.peek().is_(Token.NEWLINE):
				# This gets eaten next run through the loop
				tags.append((t, args, path))
			else:
				# Tag must be followed whitespace or left paren
				raise error_messages.ParseError("Unexpected token after section tags: %s, '%s'." % (tok.peek(), tok.peek().get_value()), pos)
		
		return tags

	def _parse_section_contents(self, tok, header, implied_tags, path):
		t = tok.peek()
		section_tags = implied_tags
		if t.is_(Token.COLON):
			# if a colon follows the right bracket of the section heading, we expect section_tags
			section_tags = self._parse_section_tags(tok, header, implied_tags, path)
		while True:
			tok.allow_whitespace()
			t = tok.peek()
			if t.is_(Token.LEFT_BRACKET) or t.is_(Token.EOF):
				return
			if t.is_(Token.DIRECTIVE):
				# Directive
				self._parse_section_content_directive(tok, header, section_tags, path)
			elif not t.is_(Token.NEWLINE):
				# Filename
				self._parse_section_content_filename(tok, header, path, section_tags)
			else:
				# Blank line
				tok.expect(Token.NEWLINE)
	
	def _parse_section_content_directive(self, tok, header, section_tags, path):
		global_only_directives = ['@define']
		pos = tok.position.duplicate()
		t = tok.expect(Token.DIRECTIVE)
		if t.get_value() == '@add':
			while tok.peek().is_(Token.DIRECTIVE_STRING):
				t = tok.expect(Token.DIRECTIVE_STRING)
				self._reporter.add_implication(header, t.get_value(), pos)
		elif t.get_value() == '@att':
			self._parse_attribute(tok, header, path)
		elif t.get_value() == '@import':
			import_filename = self._parse_import_filename(tok)
			filename = os.path.join(os.path.dirname(self._filename), import_filename)
			new_path = os.path.join(path, os.path.dirname(import_filename))
			m = Manifest(filename, header, section_tags, new_path, self._reporter, self, pos)
		elif t.get_value() == '@error':
			str_list = []
			while tok.peek().is_(Token.DIRECTIVE_STRING):
				str_list.append(tok.expect(Token.DIRECTIVE_STRING, "error string").get_value())
			str_ = ' '.join(str_list)
			self._reporter.add_error(header, str_, pos)
		elif t.get_value() in global_only_directives:
			raise error_messages.ParseError("%s directive cannot appear in section." % t.get_value(), pos)
		else:
			raise error_messages.ParseError("Unknown directive '%s'." % t.get_value(), pos)
		
		if tok.peek().is_(Token.EOF):
			return
		tok.allow_whitespace()
		tok.expect(Token.NEWLINE, "end of directive")

	def _parse_attribute(self, tok, header, path):
		pos = tok.position.duplicate()
		attr_name = tok.expect(Token.DIRECTIVE_STRING, "attr name").get_value()
		attr_type = AttributeData.STRING
		is_list = False
		tok.allow_whitespace()
		if tok.peek().is_(Token.APPEND_OPERATOR):
			tok.expect(Token.APPEND_OPERATOR, 'list attribute')
			is_list = True
		elif tok.peek().is_(Token.EQ):
			tok.expect(Token.EQ, 'scalar attribute')
		else:
			raise error_messages.ParseError("Invalid attribute assignment operator %s" % tok.peek(), pos)
		
		tok.allow_whitespace()
		if tok.peek().is_(Token.DIRECTIVE_VALUE_PATH):
			attr_val = tok.expect(Token.DIRECTIVE_VALUE_PATH, 'attribute path').get_value()
			attr_data = AttributeData(AttributeData.PATH, attr_val, pos)
		elif tok.peek().is_(Token.DIRECTIVE_VALUE_STRING):
			attr_val = tok.expect(Token.DIRECTIVE_VALUE_STRING, 'attribute string').get_value()
			attr_data = AttributeData(AttributeData.STRING, attr_val, pos)
		else:
			raise error_messages.ParseError("String or path required in attribute assignment: %s" % tok.peek(), pos)
			
		if is_list:
			attr_data = AttributeData(AttributeData.LIST, [attr_data], [pos])
		key_list = attr_name.split('.')
		if len(key_list) > 1:
			attr_name = key_list[0]
			keys = key_list[1:]
			for key in reversed(keys):
				attr_data = AttributeData(AttributeData.MAP, { key: attr_data }, [pos])
		attr_type = attr_data.get_type()
		
		spec = AttributeSpec(data_type=attr_type, default=None)

		self._reporter.add_define(AttributeDefinition(name=attr_name,
		                                              spec=spec,
		                                              position=pos))
		attr_outcome = AttributeOutcome(header, pos, attr_name, attr_data, path)
		
		self._reporter.add_directive_value(header, attr_outcome)
	
	def _parse_import_filename(self, tok):
		# TODO: This might be better if it just expects a DIRECTIVE_STRING.
		filename = ''
		while True:
			t = tok.peek()
			if t.is_(Token.EOF) or t.is_(Token.NEWLINE):
				return filename
			elif t.is_(Token.DIRECTIVE_STRING):
				filename += tok.expect(Token.DIRECTIVE_STRING).get_value()
				if tok.peek().is_(Token.DIRECTIVE_STRING):
					return filename
			else:
				filename += tok.next().get_value()
	
	def _parse_section_content_filename(self, tok, header, path, section_tags):
		# A filename can be optionally tagged. A tag can optionally take
		# a number of parameters.
		# e.g
		# <tag> ( <param> , <param> ) ' ' <tag> ( <param> ) : <filename>
		# <filename>
		# <tag> : <filename>
		# : <filename>
		# etc
		
		# Could be nothing
		if tok.peek().is_(Token.NEWLINE):
			return
		if tok.peek().is_(Token.EOF):
			return
		
		pos = tok.position.duplicate()
		
		# Parse tags - and possibly a bit of filename
		tags = list(section_tags)
		
		# This loop takes place before we know if we have a file or a tagged
		# file. When we break out of this loop we will have one of these
		# cases:
		# 1) extra_tags contains the tags, filename is '', tokeniser is
		#     pointing at a Token.COLON
		# 2) extra_tags contains the tags, filename is the name of the
		#     file, tokeniser is pointing at a Token.NEWLINE or Token.EOF.
		# 3) extra_tags contains the tags, filename is the first
		#     part of the filename, tokeniser is pointing at some tokens
		#     other than Token.NEWLINE or Token.EOF (containing the rest of
		#     the filename)
		
		filename = ''
		
		# If there was whitespace being added through a dedicated WHITESPACE
		# token, then we keep track of the last part of it separetely. Any
		# appearing at the end of the filename is stripped out.
		trailing_whitespace = ''
		
		# extra_tags holds the tags applied on this line
		# tags holds the tags applied to the section we are in
		extra_tags = []
		while True:
			t = tok.peek()
			if t.is_(Token.COLON):
				filename = ''
				break
			elif t.is_(Token.EOF):
				extra_tags = []
				break
			elif t.is_(Token.NEWLINE):
				extra_tags = []
				break
			
			t = tok.next()
			filename += trailing_whitespace
			trailing_whitespace = ''
			filename += t.get_value()
			
			if t.is_(Token.SECTION_STRING):
				# This might be a tag, parse the arguments
				args = None
				might_be_tagged = False
				tag_name = t.get_value()
				if tok.peek().is_(Token.LEFT_PAREN):
					args, text = self._parse_tag_arguments(tok)
					filename += text
					if args is None:
						# Argument list was wrong - must be a filename
						extra_tags = []
						break
					else:
						assert isinstance(args, list)
						might_be_tagged = True
				elif tok.peek().is_(Token.WHITESPACE):
					might_be_tagged = True
				elif tok.peek().is_(Token.COLON):
					# actually, it is tagged, but we can lock that in on the
					# next run through the loop
					might_be_tagged = True 
				
				if might_be_tagged:
					trailing_whitespace = tok.allow_whitespace()
					assert isinstance(args, list) or args is None
					assert isinstance(tag_name, str)
					assert isinstance(path, str)
					extra_tags.append((tag_name, args, path))
					
				
			else:
				# If the token is not a Token.SECTION_STRING then we don't
				# have a tag.
				break
		
		t = tok.peek()
		read_filename = False
		if t.is_(Token.COLON):
			# Case 1
			tok.expect(Token.COLON)
			tok.allow_whitespace()
			read_filename = True
		elif t.is_(Token.NEWLINE):
			# Case 2
			tok.expect(Token.NEWLINE)
		elif t.is_(Token.EOF):
			# Case 2
			pass
		else:
			# Case 3
			read_filename = True
		
		if read_filename:
			while True:
				t = tok.peek()
				if t.is_(Token.EOF):
					break
				elif t.is_(Token.NEWLINE):
					tok.expect(Token.NEWLINE)
					break
				elif t.is_(Token.WHITESPACE):
					# Track separately, so we don't add it if it is the last
					# thing
					trailing_whitespace += tok.next().get_value()
				else:
					filename += trailing_whitespace
					trailing_whitespace = ''
					filename += tok.next().get_value()
		
		file_outcome = FileOutcome(header, pos, 
		                           os.path.join(path, filename), 
		                           tags + extra_tags)
		self._reporter.add_file(header, file_outcome)
	
	def _parse_tag_arguments(self, tok):
		# This returns a tuple containing the tag arguments (if valid)
		# and the plain text which was consumed.
		args = []
		value = ''
		text = tok.expect(Token.LEFT_PAREN).get_value()
		text += tok.allow_whitespace()
		while True:
			t = tok.peek()
			if t.is_(Token.COMMA):
				text += t.get_value()
				tok.expect(Token.COMMA)
				text += tok.allow_whitespace()
				args.append(value)
				value = ''
			elif t.is_(Token.SECTION_STRING):
				text += t.get_value()
				value += tok.expect(Token.SECTION_STRING).get_value()
				text += tok.allow_whitespace()
			else:
				break
		
		args.append(value)
		t = tok.peek()
		if t.is_(Token.RIGHT_PAREN):
			return args, text + tok.expect(Token.RIGHT_PAREN).get_value()
		else:
			# No closing ')' - return just the text
			return None, text
	
	def _eat_whitespace(self, tok):
		while True:
			t = tok.peek()
			if t.is_(Token.NEWLINE):
				tok.expect(Token.NEWLINE)
			else:
				return
	
class AttributeData(object):
	(STRING, PATH, LIST, MAP) = range(4)
	
	type_to_string = {
		STRING: 'String',
		PATH: 'Path',
		LIST: 'List',
		MAP: 'Map',
	}
	
	default_values = {
		STRING: None,
		PATH: None,
		LIST: [],
		MAP: {},
	}
	
	types = {
		STRING: str,
		PATH: str,
		LIST: list,
		MAP: dict,
	}
	
	container_types = set([MAP, LIST])
	
	def __init__(self, data_type, data, positions):
		if data_type in self.container_types:
			assert isinstance(positions, list)
			assert all([isinstance(p, Position) for p in positions])
		elif data_type in (self.STRING, self.PATH):
			if not data is None:
				assert isinstance(positions, Position)
		else:
			assert False, "Unrecognised data type"
		
		self._type = data_type
		self._positions = positions
		if data is not None:
			assert isinstance(data, AttributeData.types[self._type])
			self._data = data
		else:
			self._data = AttributeData.default_values[self._type]
	
	def duplicate(self):
		if self._data is None:
			data_copy = None
		elif isinstance(self._data, str):
			data_copy = self._data
		elif isinstance(self._data, list):
			data_copy = [ad.duplicate() for ad in self._data]
		elif isinstance(self._data, dict):
			data_copy = dict(self._data)
		else:
			assert False, "Unknown data"
		
		if isinstance(self._positions, Position):
			position_copy = self._positions
		elif self._positions is None:
			position_copy = None
		else:
			position_copy = list(self._positions)
		
		return AttributeData(self._type, data_copy, position_copy)
	
	def get_type(self):
		return self._type
		
	def get_type_str(self):
		return AttributeData.type_to_string[self._type]
	
	def get_value(self, path_type, enum):
		assert isinstance(path_type, PathType)
		assert isinstance(enum, set) or enum is None
		if self._type == AttributeData.STRING:
			if enum is not None and not self._data in enum:
				raise error_messages.EnumValueError(enum, self._data, self._positions)
			return self._data
		elif self._type == AttributeData.PATH:
			return path_type.write_path(self._data)
		elif self._type == AttributeData.LIST:
			return [attr_data.get_value(path_type, enum) for attr_data in self._data]
		elif self._type == AttributeData.MAP:
			value = {}
			for key, attr_data in self._data.items():
				value[key] = attr_data.get_value(path_type, enum)
			return value
		else:
			raise error_messages.UnknownTypeError(self._type)

	def is_container(self):
		return self._type in container_types

	def get_data(self):
		return self._data
	
	def get_position(self):
		return self._positions
	
	def set_data(self, data):
		assert isinstance(data, AttributeData.types[self._type])
		self._data = data
		
	def __str__(self):
		if self._type == AttributeData.STRING or self._type == AttributeData.PATH:
			data_string = self._data
		elif self._type == AttributeData.LIST:
			data_string = [str(x) for x in self._data]
		elif self._type == AttributeData.MAP:
			data_string = ["%s: %s" % (x, y) for x, y in self._data.items()]
		else:
			raise error_messages.UnknownTypeError(self._type)
		return "[%s: %s]" % (self.get_type_str(), data_string)
	
	def __eq__(self, other):
		return self._type == other.get_type() and self._data == other.get_data()
		
	def matches_type(self, att_data):
		if self._type != att_data.get_type():
			return False
		if self._type == AttributeData.STRING or self._type == AttributeData.PATH:
			return True
		if not self._data or not att_data.get_data():
			# at least one container is empty, which should always match
			return True
		if self._type == AttributeData.LIST:
			return self._data[0].matches_type(att_data.get_data()[0])
		elif self._type == AttributeData.MAP:
			return self._data.values()[0].matches_type(att_data.get_data().values()[0])
		else:
			raise error_messages.UnknownTypeError(self._type)
			
	def merge(self, att_data, path=''):
		assert isinstance(att_data, AttributeData)
		
		new_data = self.duplicate()
		if self._type == AttributeData.STRING:
			new_data._positions = att_data._positions
			new_data.set_data(att_data.get_data())
		elif self._type == AttributeData.PATH:
			new_data._positions = att_data._positions
			new_data.set_data(os.path.join(path, att_data.get_data()))
		elif self._type == AttributeData.LIST:
			new_data._positions = self._positions + att_data._positions
			for item in att_data.get_data():
				if item.get_type() == AttributeData.PATH:
					new_data._data.append(AttributeData(AttributeData.PATH, 
					                      os.path.join(path, item.get_data()),
					                      item.get_position()))
				else:
					new_data._data.append(item)
		elif self._type == AttributeData.MAP:
			new_data._positions = self._positions + att_data._positions
			for key, raw_val in att_data.get_data().items():
				if key in new_data._data:
					new_data._data[key] = new_data._data[key].merge(raw_val, path)
				else:
					if raw_val.get_type() == AttributeData.PATH:
						new_item = AttributeData(AttributeData.PATH,
						                         os.path.join(path, raw_val.get_data()),
						                         raw_val.get_position())
					else:
						new_item = raw_val.duplicate()
					new_data._data[key] = new_item
		else:
			raise error_messages.UnknownTypeError(self._type)
		return new_data


class AttributeSpec(object):
	def __init__(self, data_type, default):
		self._data_type = data_type
		self._default = default

	def __str__(self):
		
		ret = "[%s" % AttributeData.type_to_string[self._data_type]
		if self._default:
			ret += '=' + self._default
		
		return ret + ']'
			
	def get_data_type(self):
		return self._data_type
	
	def get_default(self):
		return self._default
	
	def get_value(self, keywords, path_type, choices, enum_map):
		assert isinstance(choices, OutcomePoset)
		assert isinstance(path_type, PathType)
		
		if self._data_type in AttributeData.container_types:
			seed = AttributeData(self._data_type, None, [])
			
			if len(choices) == 0:
				return AttributeData.default_values[self._data_type]
			
			for c in choices.in_order():
				seed = seed.merge(c.get_value(), c.get_path())
			
			return seed.get_value(path_type, enum_map)
		else:
			force_tie_break = False
			
			if len(choices) == 0:
				return AttributeData.default_values[self._data_type]
			value = choices.supremum()
			
			seed = AttributeData(self._data_type, None, None)
			seed = seed.merge(value.get_value(), value.get_path())
			
			return seed.get_value(path_type, enum_map)


class AttributeDefinition(object):
	def __init__(self, name, spec, position):
		self._name = name
		self._spec = spec
		self._position = position
	
	def get_name(self):
		return self._name
	
	def get_value(self, keywords, path_type, choices, enum_map):
		assert isinstance(choices, OutcomePoset)
		assert isinstance(path_type, PathType)
		
		return self._spec.get_value(keywords, path_type, choices, enum_map)
	
	def get_data_type(self):
		return self._spec.get_data_type()
		
	def get_spec(self):
		return self._spec
		
	def get_position(self):
		return self._position
	
	def __str__(self):
		return "[%s: %s]" % (self._name, self._spec)

class Documentation(object):
	(KEYWORD, ATTRIBUTE, TAG, DIMENSION) = range(4)
	valid_types = set([KEYWORD, ATTRIBUTE, TAG, DIMENSION])

	@classmethod
	def get_type_from_string(cls, doc_type_str, pos):
		type_key = doc_type_str.lower()
		if type_key == 'keyword':
			return cls.KEYWORD
		elif type_key == 'attribute':
			return cls.ATTRIBUTE
		elif type_key == 'tag':
			return cls.TAG
		elif type_key == 'dimension':
			return cls.DIMENSION
		else:
			raise error_messages.ParseError("Unknown documentation type %s" % doc_type_str, pos)

	def __init__(self, type_, key, text, position):
		self._key = key
		self._type = type_
		assert type_ in Documentation.valid_types
		self._text = text
		self._position = position

	def get_type(self):
		return self._type

	def get_key(self):
		return self._key

	def get_text(self):
		return self._text

	def get_position(self):
		return self._position

	@classmethod
	def get_display_string(cls, type_):
		return {
			cls.KEYWORD: 'Keywords',
			cls.ATTRIBUTE: 'Attributes',
			cls.TAG: 'Tags',
			cls.DIMENSION: 'Dimensions',
		}[type_]
		
	def __str__(self):
		return "[Documentation for %s %s: %s]" % (self._type, self._key, self._text)

# flat list of strings
class Tokeniser(object):
	(_HEADER_KEYWORDS, _DIRECTIVE_KEY, _DIRECTIVE_VALUE, _SECTION, _DIRECTIVE) = range(5)
	
	def __init__(self, filename):
		self.position = Position(filename)
		self._file = open(filename, "r")
		
		self._next_token = None
		self._char_buffer = None
		self._raw_buffer = None
		self._raw_position = Position(filename)
		
		self._expected_char = None
		
		self._state = self._SECTION
	
	def close(self):
		self._file.close()
	
	def peek(self):
		if self._next_token is None:
			# Read a token
			self._next_token = self.next()
		return self._next_token
	
	def expect(self, type_, meaning=None):
		t = self.peek()
		if t.is_(type_):
			return self.next()
		else:
			# Meaning should only be None if we are sure the type will be
			# correct.
			assert(not meaning is None)
			raise error_messages.ParseError("Expected %s. Found %s instead." % (meaning, t), self.position)
	
	def next(self):
		ret = self._next()
		return ret
	
	def allow_whitespace(self):
		ret = ''
		while self.peek().is_(Token.WHITESPACE):
			ret += self.next().get_value()
		return ret

	def _next(self):
		# Do we have a token already queued up?
		if self._next_token:
			ret = self._next_token
			self._next_token = None
			return ret
		
		# Move past whitespace and comments
		whitespace = ''
		whitespace_pos = self.position.duplicate()
		while True:
			ch = self._peek_char(allow_escape=True)
			# Eat whitespace
			while ch.isspace() and ch != '\n':
				whitespace += self._get_char(allow_escape=True)
				ch = self._peek_char(allow_escape=True)
			
			# Eat comments
			end_of_comment = lambda c: c == '\n' or c == ''
			if ch == '#':
				while not end_of_comment(self._peek_char(allow_escape=True)):
					self._get_char(allow_escape=True)
					ch = self._peek_char(allow_escape=True)
			else:
				break
		
		if len(whitespace) > 0:
			return Token(Token.WHITESPACE, whitespace, whitespace_pos)
		
		pos = self.position.duplicate()
		ch = self._get_char(allow_escape=True)
		
		if ch == '':
			return Token(Token.EOF, None, pos)
		
		if ch in Token.SIMPLE_TOKENS:
			if ch == '.' and self._state != self._HEADER_KEYWORDS:
				# Treat "." as a token, only when parsing
				# the keyword expression. In other context
				# '.' could be part of a path string
				pass
			else:
				self._handle_simple_state_transition(ch)
				return Token(Token.SIMPLE_TOKENS[ch], ch, pos)
		
		# A directive (like @add), terminates by non-alphabetic character
		if ch == '@':
			ident = '@'
			self._state = self._DIRECTIVE
			while True:
				ch = self._get_char(allow_escape=True)
				if ch.isalpha():
					ident += ch
				else:
					return Token(Token.DIRECTIVE, ident, pos)
		
		# Assignment operator for attributes
		if ch == '+':
			if self._peek_char(allow_escape=True) == '=':
				self._get_char(allow_escape=True)
				return Token(Token.APPEND_OPERATOR, '+=', pos)
			else:
				return Token(Token.PLUS, '+', pos)
		
		string = ''
		allow_escape = True
		is_path = False
		terminal = None
		if len(string) == 0 and (ch == '"' or ch == "'"):
			# Quoted string
			terminal = ch
			eat_terminal = True
			error_on = '\n'
		elif (ch == 'r' or ch == 'p') and self._peek_char(allow_escape=True) in ['"', "'"]:
			# Raw quoted string
			terminal = self._get_char(allow_escape=True)
			string = ''
			eat_terminal = True
			# This doesn't actually match python raw strings as newlines are
			# not allowed in a python raw string. Python is pretty weird here
			# though:
			# >>> a = r'\
			# ... '
			# >>> print(repr(a))
			# '\\\n'
			error_on = '' 
			allow_escape = False
			is_path = (ch == 'p')
		else:
			# Unquoted string
			if self._state == self._DIRECTIVE:
				terminal = ' \t\n,=<+('
			if self._state == self._DIRECTIVE_KEY:
				terminal = ')'
			elif self._state == self._HEADER_KEYWORDS:
				terminal = ' \t]+.()'
			elif self._state == self._DIRECTIVE_VALUE:
				terminal = ' \t\n'
			elif self._state == self._SECTION:
				terminal = '()\n:, \t'
			string = ch
			eat_terminal = False
			error_on = ''
		
		assert not terminal is None
		
		while True:
			ch = self._peek_char(allow_escape)
			if ch in terminal:
				if eat_terminal:
					self._get_char(allow_escape)
				
				if self._state == self._DIRECTIVE:
					token_type = Token.DIRECTIVE_STRING
					while self._peek_char(allow_escape).isspace() and not self._peek_char(allow_escape) == '\n':
						self._get_char(allow_escape)
					switch_ch = self._peek_char(allow_escape)
					if switch_ch == '=' or switch_ch == '+' or switch_ch == '<':
						self._state = self._DIRECTIVE_VALUE
					elif switch_ch == '(':
						self._state = self._DIRECTIVE_KEY
						self._get_char(allow_escape)
				elif self._state == self._DIRECTIVE_KEY:
					token_type = Token.DIRECTIVE_KEY
					self._state = self._DIRECTIVE_VALUE
					self._get_char(allow_escape)
				elif self._state == self._HEADER_KEYWORDS:
					token_type = Token.HEADER_KEYWORD_STRING
				elif self._state == self._DIRECTIVE_VALUE:
					token_type = (is_path and Token.DIRECTIVE_VALUE_PATH 
					                      or Token.DIRECTIVE_VALUE_STRING)
				elif self._state == self._SECTION:
					token_type = Token.SECTION_STRING
				return Token(token_type, string, pos)
			if ch in error_on:
				raise error_messages.ParseError("Unexpected characted %s in string."%repr(ch), self.position)
			else:
				string += self._get_char(allow_escape)
	
	def _handle_simple_state_transition(self, char):
		# A newline always puts us into section mode
		if char == '\n':
			self._state = self._SECTION
			
		if self._state == self._SECTION:
			# If we read a '[', then we are up to reading header keywords
			if char == '[':
				self._state = self._HEADER_KEYWORDS
		elif self._state == self._HEADER_KEYWORDS:
			# Once we read the ']' we are in the section (i.e. do the same as for _ATTRIBUTE_VALUE)
			if char == ']':
				self._state = self._SECTION
	
	def _peek_char(self, allow_escape):
		if self._char_buffer is None:
			self._char_buffer = self._get_char(allow_escape)
			self._char_buffer_position = self._get_position
			self._char_buffer_allow_escape = allow_escape
		
		return self._char_buffer
	
	def _get_char(self, allow_escape):
		if not self._char_buffer is None:
			assert allow_escape == self._char_buffer_allow_escape
			ch = self._char_buffer
			self.position = self._char_buffer_position
			self._char_buffer = None
			self._char_buffer_position = None
			return ch
		
		ch1 = self._get_char_raw()
		self._get_position = self._raw_position.duplicate()
		if ch1 == '\\' and allow_escape:
			ch2 = self._get_char_raw()
			if ch2 == 'n':
				return '\n'
			elif ch2 == 't':
				return '\t'
			elif ch2 == '\n':
				return self._get_char(allow_escape)
			elif ch2 == '':
				raise error_messages.ParseError("Unexpected EOF.", self._raw_position)
			# This could potentially be an error case, in which case
			# we should allow "\\" to work
			return ch2
		
		return ch1
	
	def _get_char_raw(self):
		CR = '\r'
		LF = '\n'
		
		ch1 = None
		if self._raw_buffer:
			ch1 = self._raw_buffer
			self._raw_buffer = None
		else:
			ch1 = self._file.read(1)
		
		if ch1 == CR:
			self._raw_position.update('\n')
			ch2 = self._file.read(1)
			if ch2 != LF:
				self._raw_buffer = ch2
			return '\n'
		
		if ch1 == LF:
			self._raw_position.update('\n')
			return '\n'
		
		self._raw_position.update(ch1)
		return ch1


class Position(object):
	def __init__(self, filename):
		self._filename = filename
		self._norm_filename = None
		self._line = 1
		self._column = 1
	
	def duplicate(self):
		ret = Position(self._filename)
		ret._line = self._line
		ret._column = self._column
		ret._norm_filename = self._norm_filename
		return ret
	
	def get_filename(self):
		return self._filename
		
	def update(self, ch):
		if ch == '\n':
			self._line += 1
			self._column = 1
		else:
			self._column += 1
	
	def _ensure_has_norm_filename(self):
		if self._norm_filename is None:
			self._norm_filename = os.path.normpath(self._filename)
	
	def __str__(self):
		self._ensure_has_norm_filename()
		return '%s:%d:%d' % (self._norm_filename, self._line, self._column)
	
	def __cmp__(self, other):
		assert isinstance(other, Position)
		
		self._ensure_has_norm_filename()
		other._ensure_has_norm_filename()
		
		# TODO: Make sure we give the same results on all operating systems
		# (e.g. remove possibility of directory separators changing the order)
		return cmp(self._norm_filename, other._norm_filename) or \
		       cmp(self._line, other._line) or \
		       cmp(self._column, other._column)

