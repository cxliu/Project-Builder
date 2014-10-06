import uuid
import os
import errno
import re
import stat

from xml.parsers.expat import ExpatError

# We have to use a dirty self-implementation of the ElementTree
# which does not escape XML attributes and texts because of
# conflicts in VC2010 project files
import non_strict_element_tree as ElementTree


SUPPORTED_VS_VERSIONS = ('2005', '2008', '2010', '2012', '2013')


BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..')

class VsError(Exception):
	def __init__(self, solution, project, config, message):
		self._solution = solution
		self._project = project
		self._config = config
		self._message = message
	
	def __str__(self):
		name = []
		if not self._solution is None:
			name.append(self._solution.get_filename())
		if not self._project is None:
			name.append(self._project.get_name())
		name = ':'.join(name)
		if len(name) == 0:
			name = '(unknown)'
		
		if self._config is None:
			return "Couldn't generate Visual Studio files for %s: %s" % (name, self._message)
		else:
			return "Couldn't generate Visual Studio files for %s (config %r): %s" % (name, self._config, self._message)

def _indent(amount):
	return '\t' * amount

def deterministic_guid(identifier_string):
	our_namespace = uuid.UUID('422b00dc-9f1f-11e1-9dd1-0019d1e7bace')
	return str(uuid.uuid3(our_namespace, identifier_string)).upper()


def get_output_file(module_definition_file, configuration_type, ext, separator):
	if configuration_type == 'application':
		ret = '$(OutDir)%s$(ProjectName)%s' % (separator, ext)
	elif configuration_type == 'dynamic_library':
		ret = '$(OutDir)%s$(ProjectName)%s' % (separator, ext)
	elif configuration_type == 'static_library':
		ret = '$(OutDir)%s$(ProjectName)%s' % (separator, ext)
	else:
		raise ValueError("Unknown configuration type '%s'" % configuration_type)
	
	if module_definition_file != '':
		# When we have a module definition file, we are building a .dll,
		# We only support .def files which have "LIBRARY" on the first line
		# and don't specify a base address
		# See http://msdn.microsoft.com/en-us/library/28d6s79h%28v=vs.80%29.aspx
		# for details of this file format.
		
		def_file = open(module_definition_file)
		
		# The first line of the def file should be
		# LIBRARY [<something>]
		line = def_file.readline()
		
		def_file.close()
		line = line.strip()
		if not line.startswith('LIBRARY'):
			raise ValueError("Couldn't parse .def file to determine output name")
		
		line = line.replace("LIBRARY", "", 1)
		line = line.strip()
		if len(line) > 0:
			ret = '$(OutDir)%s%s.dll' % (separator, line)

	return ret

# There are some hardcoded guids inside visual studio projects and solutions
# This is where we store them (you can google for them to see that they
# aren't unique in our projects).
def solution_guid():
	return "8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942"

