"""Error messages that are useful for different backends"""

import error_helper
import copy
import m2

def warning_about_restricting_projects():
	msg = "WARNING\n"
	msg += "Running M-Build scripts with a restricted set of projects can lead\n"
	msg += "to the generated project files being out of sync with each other.\n"
	msg += "It is recommended that before committing the generated files to\n"
	msg += "version control, you run this script without restricting the projects.\n"
	return msg

def unknown_attribute_value(attribute_name, manifest):
	msg = "Couldn't find value for attribute %r\n" % attribute_name
	msg += "One of these definitions may be useful:\n"
	for outcome in error_helper.what_sets_this_attribute(manifest, attribute_name):
		msg += "# %s\n" % outcome.get_position()
		msg += "[%s]\n" % (outcome.get_keyword_expression().simplify(set(['default'])))
		msg += "@att %s = %s\n\n" % (outcome.get_key(), outcome.get_value())
	
	return msg


class ManifestError(Exception): pass

class ProjectError(ManifestError):
	def __init__(self, project, message):
		self._project = project
		self._message = message
	
	def __str__(self):
		return "[%s]: %s" % (self._project.get_name(), self._message)


# This is a manifest error
class ProjectConfigError(ProjectError):
	def __init__(self, project, config, message):
		self._project  = project
		self._config = config
		self._message = message
	
	def __str__(self):
		return "[%s: %r]: %s" % (self._project.get_name(), self._config, self._message)

class ProjectFileError(ProjectError):
	def __init__(self, filename, parent_names, extra_message=''):
		self._filename  = filename
		self._parent_names = parent_names
		message = "Project file %s is not found." % (self._filename)
		if extra_message:
			message += "\n%s" % (extra_message)
		if parent_names:
			message += "\nIt is required by project(s) %s." % str(self._parent_names)
		self._message = message
	
	def __str__(self):
		return self._message

class RequiredPathType(ManifestError):
	def __init__(self, path):
		self._path = path
	
	def __str__(self):
		return "Was asked to work with path %r, but didn't know what style of path it should be." % (self._path)

class ExclusiveTagError(ManifestError):
	def __init__(self, message, location):
		self._message = message
		self._location = copy.copy(location)
	
	def __str__(self):
		return "[%s: %s]" % (self._location, self._message)

class PriorityError(ManifestError):
	def __init__(self, keywords, outcomes):
		self._outcomes = outcomes
		self._keywords = keywords
	
	def __str__(self):
		new_keyword = lambda keyword: m2.KeywordExpression(m2.Token.DOT, 
		                                                  [m2.KeywordExpression("NEW_KEYWORD", None), keyword])
		simplifed_keyword = lambda outcome: str(outcome.get_keyword_expression().simplify(["default"]))
		simplifed_outcome_str = lambda outcome: str(outcome).split("\n")[0]
		
		relevant_keywords = []
		defined_keywords = []
		ret = "\nCould not decide between %d outcomes:\n\n" % len(self._outcomes)
		for outcome in self._outcomes:
			ret += "%s => %s\n" % (str(outcome.get_keyword_expression().simplify(["default"])), outcome)
			for k in outcome.get_keyword_expression().get_keywords():
				relevant_keywords.append(k)
				if k in self._keywords:
					defined_keywords.append(k)
		
		relevant_keywords = sorted(list(set(relevant_keywords)))
		defined_keywords  = sorted(list(set(defined_keywords)))
		ret += "Relevant keywords : %s\n" % (", ".join([k for k in relevant_keywords]))
		ret += "Defined  keywords : %s\n" % (", ".join([k for k in defined_keywords]))
		
		ret += "\n===========================================================================\n\n"
		ret += "New keywords may help you to break the tie. For example:\n\n"
		outcome_modify = self._outcomes[0]
		outcome_modify._keyword_expression = new_keyword(outcome_modify.get_keyword_expression())
		ret += "[%s]\n%s\n\n" % (simplifed_keyword(outcome_modify), simplifed_outcome_str(outcome_modify))
		
		for outcome in self._outcomes[1:]:
			ret += "[%s]\n%s\n\n" % (simplifed_keyword(outcome), simplifed_outcome_str(outcome))
		ret += "Attribute %s will be enabled when NEW_KEYWORD is defined too.\n" % simplifed_outcome_str(outcome_modify)
		
		return ret


class ParseError(ManifestError):
	def __init__(self, message, location):
		self._message = message
		self._location = copy.copy(location)
	
	def __str__(self):
		return "[%s: %s]" % (self._location, self._message)

class UndefinedAttributeError(ManifestError):
	def __init__(self, name):
		self._name = name
	
	def __str__(self):
		return "Unknown attribute '%s'" % self._name

class UnsetAttributeError(ManifestError):
	def __init__(self, name):
		self._name = name
	
	def get_attribute_name(self):
		return self._name
	
	def __str__(self):
		return "Attribute was not set '%s'" % self._name


class MultipleDefinitionError(ManifestError):
	def __init__(self, def1, def2):
		assert def1.get_name() == def2.get_name()
		self._def1 = def1
		self._def2 = def2
	
	def __str__(self):
		return ("Attribute '%s' has multiple definitions: " +
		       "\n%s at %s\n%s at %s") % (
		        self._def1.get_name(),
		        str(self._def1), str(self._def1.get_position()),
		        str(self._def2), str(self._def2.get_position()))

class MultipleDocumentationError(ManifestError):
	def __init__(self, doc1, doc2):
		assert doc1.get_key() == doc2.get_key() and doc1.get_type() == doc2.get_type()
		self._doc1 = doc1
		self._doc2 = doc2
	
	def __str__(self):
		return ("Documentation element for %s '%s' has multiple documentations: " +
		       "\n%s at %s\n%s at %s") % (
		        self._doc1.get_type(),
		        self._doc1.get_key(),
		        str(self._doc1), str(self._doc1.get_position()),
		        str(self._doc2), str(self._doc2.get_position()))

class UnknownTypeError(ManifestError):
	def __init__(self, type_):
		#assert isinstance(type_, AttributeData)
		self._type = type_
	
	def __str__(self):
		return "Unknown type: %s" % str(self._type)

class UnknownEnumError(ManifestError):
	def __init__(self, type_, key):
		self._type = type_
		self._key = key
	
	def __str__(self):
		return "Couldn't '%s' in %s" % (self._key, str(self._type))

class EnumValueError(ManifestError):
	def __init__(self, enum, value, position):
		self._enum = enum
		self._value = value
		self._position = position
	
	def __str__(self):
		return "%s Illegal value %s in enum %s" % (self._position, self._value, self._enum)

class ManifestIOError(ManifestError):
	def __init__(self, io_err, parent_manifest, parent_position):
		self._io_err = io_err
		self._parent_manifest = parent_manifest
		self._parent_position = parent_position

	def __str__(self):
		ret = "%s\n" % (str(self._io_err))
		n = self._parent_manifest
		pos = self._parent_position
		indent = ' '
		while not n is None:
			ret += "%simported by '%s'\n" % (indent, pos)
			n, pos = n.get_importer()
			indent += ' '
		
		return ret

class MultipleEnumError(ManifestError):
	def __init__(self, enum, key, pos):
		self._enum = enum
		self._key = key
		self._pos = pos
	
	def __str__(self):
		ret = "enum %s = %s is redefined at %s" % (self._enum, self._key, self._pos)
		return ret
