import os
from src.build import m2
import visual_studio

class VcConfiguration(object):
	"""This wraps an M-Build configuration, and lets us find the Visual Studio
	identifier string for it.
	"""
	def __init__(self, manifest, project, configuration, vs_version):
		self._configuration = configuration
		self._vs_identifier = project.get_identifier(configuration, ['tool', 'toolchain', 'os', 'processor'])
		self._keywords = project.get_keywords(configuration)
		self._vs_platform_identifier = manifest.get_attribute(self._keywords, 'VS%s_PLATFORM_IDENTIFIER' % vs_version, m2.NoPaths(), allow_unfound=True)
		
		if self._vs_platform_identifier is None:
			raise visual_studio.VsError(None, project, configuration, "Couldn't get value for VS%s_PLATFORM_IDENTIFIER" % vs_version)

	def get_configuration(self):
		return self._configuration
	
	def get_vs_identifier(self):
		return self._vs_identifier
	
	def get_vs_platform(self):
		return self._vs_platform_identifier

	def get_vs_full_identifier(self):
		return "%s|%s" % (self._vs_identifier, self._vs_platform_identifier)
	
	def get_keywords(self):
		return self._keywords
	

