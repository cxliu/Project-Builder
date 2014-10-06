import error_messages
import m2

class NamingError(ValueError): pass


def get_environment():
	return {'Dimension': Dimension,
		    'Replace': Replace,
		    'Literal': Literal,
		    'Attribute': Attribute,
		    'Null': Null,
		    'Join': Join,
		    'ProjectName': ProjectName}

class PathComponent(object):
	def expand(self, configuration, manifest, project):
		raise NotImplementedError()
	
	def get_dimension_dependencies(self):
		return NotImplementedError()

class Null(PathComponent):
	def expand(self, configuration, manifest, project):
		return None
	
	def get_dimension_dependencies(self):
		return []

class ProjectName(PathComponent):
	def expand(self, configuration, manifest, project):
		return project.get_name()
	
	def get_dimension_dependencies(self):
		return []

class Literal(PathComponent):
	def __init__(self, value):
		self._value = value
	
	def expand(self, configuration, manifest, project):
		return self._value
	
	def get_dimension_dependencies(self):
		return []

class Dimension(PathComponent):
	def __init__(self, dimension):
		self._dimension = dimension
	
	def expand(self, configuration, manifest, project):
		return configuration[self._dimension]
	
	def get_dimension_dependencies(self):
		return [self._dimension]
		
class Replace(PathComponent):
	def __init__(self, dimension, map):
		assert isinstance(map, dict)
		self._dimension = dimension
		self._map = map
		
	def expand(self, configuration, manifest, project):
		raw = configuration[self._dimension]
		for key, value in self._map.iteritems():
			if key == raw:
				return value
		return raw
	
	def get_dimension_dependencies(self):
		return [self._dimension]

class Attribute(PathComponent):
	def __init__(self, attribute):
		self._attribute = attribute
	
	def expand(self, configuration, manifest, project):
		ret = manifest.get_attribute(project.get_keywords(configuration), self._attribute, m2.NoPaths(), allow_unfound=True)
		
		if ret is None:
			raise NamingError("When naming configuration %s of project %s\nHad keywords: %s\n%s" % (
				configuration,
				project.get_name(),
				project.get_keywords(configuration),
				error_messages.unknown_attribute_value(self._attribute, manifest)))
		if not isinstance(ret, str):
			raise NamingError("When naming configuration %s of project %s, expected attribute %s to be a string, but it was a %s" % (configuration, project.get_name(), self._attribute, type(ret)))
		
		return ret
	
	def get_dimension_dependencies(self):
		# Technically, this could depend on any dimension, however we only include
		# direct dependencies
		return []

class Join(PathComponent):
	def __init__(self, joiner, items):
		self._joiner = joiner
		self._items = items
	
	def expand(self, configuration, manifest, project):
		return self._joiner.join([p.expand(configuration, manifest, project) for p in self._items])

	def get_dimension_dependencies(self):
		ret = []
		for item in self._items:
			these_dims = item.get_dimension_dependencies()
			for dim in these_dims:
				if not dim in ret:
					ret.append(dim)
		return ret


