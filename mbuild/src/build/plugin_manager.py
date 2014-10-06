import m2

# This exception can be thrown by a plugin when it is being loaded if it
# requires symbols which are given by another plugin. There is no guarantee
# about the order that plugins will be loaded in, and if two plugins depend
# on each other, then everything will break
class MissingPrerequisiteError(Exception):
	def __init__(self, plugin_name, symbol):
		self._plugin_name = plugin_name
		self._symbol = symbol
	
	def get_symbol(self):
		return self._symbol
	
	def __str__(self):
		return "%s expected symbol %r to be available" % (self._plugin_name, self._symbol)


class PluginError(Exception): pass

class PluginIOError(PluginError):
	def __init__(self, filename):
		self._filename = filename
	
	def __str__(self):
		return "Couldn't read plugin from file %r" % self._filename

class PluginDependencyError(PluginError):
	def __init__(self, dependency_mapping):
		self._dependency_mapping = dependency_mapping
	
	def __str__(self):
		ret = "Couldn't load plugins due to missing dependencies:\n"
		for d in sorted(self._dependency_mapping.keys()):
			ret += '%s: Requires %r\n' % (d, self._dependency_mapping[d])
		return ret

class PluginInvalidError(PluginError):
	def __init__(self, filename, message):
		self._filename = filename
		self._message = message
	
	def __str__(self):
		return "%s: Plugin is invalid: %s" % (self._filename, self._message)

class PluginManager(object):
	def __init__(self, manifest, module, keywords):
		self._module = module
		
		plugins = manifest.find_file_pattern(['default'] + keywords, m2.LocalPath(), module.get_plugin_pattern())
		
		self._extensions = {}
		
		# Keep on trying to load plugins in a loop until either
		# 1) They are all loaded OR
		# 2) There is no progress being made in loading them
		err = None
		not_loaded = plugins
		while len(not_loaded) > 0:
			old_size = len(not_loaded)
			try_loading = not_loaded
			not_loaded = []
			dependencies = {}
			for p in try_loading:
				try:
					self._extensions.update(self._load_plugin(p))
				except MissingPrerequisiteError, err:
					dependencies[p] = err.get_symbol()
					not_loaded.append(p)
					last_err = err
			
			if old_size == len(not_loaded):
				raise PluginDependencyError(dependencies)
		
	
	def get_extensions(self):
		return self._extensions
	
	@staticmethod
	def _require_symbol(prerequisites, plugin_name, symbol):
		if not symbol in prerequisites:
			raise MissingPrerequisiteError(plugin_name, symbol)
	
	def _load_plugin(self, filename):
		env = {}
		env.update(self._module.get_plugin_environment())
		env.update(self._extensions)
		env['require'] = lambda sym: self._require_symbol(self._extensions, filename, sym)
		try:
			execfile(filename, env)
		except IOError:
			raise PluginIOError(filename)
		
		if "get_symbols" not in env:
			raise PluginInvalidError(filename, "Expected to find a 'get_symbols' variable.")
		
		if not callable(env['get_symbols']):
			raise PluginInvalidError(filename, "Expected 'get_symbols' to be callable.")
		
		try:
			ret = env['get_symbols']()
		except TypeError:
			raise PluginInvalidError(filename, "Expected 'get_symbols' to be callable with no arguments.")
		
		if not isinstance(ret, dict):
			raise PluginInvalidError(filename, "Expected 'get_symbols' to return a dict.")
		
		return ret

