import os
import errno
import shutil

def makedirs(path):
	"""os.makedirs throws an exception if the leaf directory exists. This is a
	bit of an antifeature, as the big reason you use the recursive form is so
	you can ensure that a directory exists before writing a file to it.
	"""
	if path == '':
		path = '.'
	
	try:
		os.makedirs(path)
	except OSError, e:
		if e.errno == errno.EEXIST:
			return
		else:
			raise e

def removedirs(path):
	"""Remove a directory recursively"""
	if path == '':
		return
	try:
		shutil.rmtree(path)
	except OSError, e:
		if e.errno == errno.ENOENT:
			return
		else:
			raise e

def sane_abspath(path, path_module):
	"""Some versions of python have an ntpath implementation of abspath which drops trailing 
	whitespace. 
	Known bad versions are 2.6.5 and 2.7.2 (under Windows)
	Known good versions are 2.6.6 and 3.1.2 (under Linux)
	This suggests to me that it is a python under windows issue, but there isn't enough data.
	"""
	trailing_space = ''
	while path[-1] == ' ':
		trailing_space += ' '
		path = path[:-1]

	return path_module.abspath(path) + trailing_space

def os_independent_path(path):
	"""Takes a path encoded as a native path, and converts it to a path
	which uses '/' as a directory separator, and doesn't have any leading ./"""
	ret = '/'.join(split_path(path, os.path))
	while ret.startswith('./'):
		ret = ret[2:]
	return ret

def make_path_relative(path, relative_to, path_module):
	"""This takes a path (either absolute, or relative to os.getcwd) and
	returns a path relative to "relative_to".
	"""
	rel_to = split_path(sane_abspath(relative_to, path_module), path_module)
	p = split_path(sane_abspath(path, path_module), path_module)
	
	if ':' in rel_to[0]:
		del(rel_to[0])
	if ':' in p[0]:
		del(p[0])
	
	# TODO: This should be case sensitive for posix paths.
	compare = lambda a, b: a.lower() == b.lower()
	
	# Drop common prefix
	while len(rel_to) > 0 and len(p) > 0 and compare(rel_to[0], p[0]):
		rel_to = rel_to[1:]
		p = p[1:]
	
	ret = [path_module.pardir] * len(rel_to) + p
	
	if len(ret) == 0:
		return '.'
	
	return path_module.join(*ret)

def split_path(path, path_module):
	"""This will take a path, and split it into sections, where each section
	is either a drive specifier, a directory name or the file name
	"""
	ret = []
	drive, path = path_module.splitdrive(path)
	
	if drive != '':
		ret.append(drive)
	
	ret += [d for d in path.replace('\\', '/').split('/') if d != '']
	return ret

def convert_path(path, from_module, to_module):
	assert not from_module.isabs(path), 'Path "%s" is absolute' % (path)
	
	ret = path.replace(from_module.sep, to_module.sep)
	if not from_module.altsep is None:
		ret = ret.replace(from_module.altsep, to_module.sep)
	
	return ret


def read_file(filename):
	ret = None
	f = open(filename)
	try:
		ret = f.read()
	finally:
		f.close()
	
	return ret

def read_only(filename):
	if not os.path.exists(filename):
		return False
	if stat.S_IMODE(os.stat(filename)[stat.ST_MODE]) & 0200:
		return False
	return True

def set_read_only(filename, writable=False):
	mode = os.stat(filename).st_mode
	if mode & 0200:
		mode ^= 0200
	if writable:
		mode |= 0200
	os.chmod(filename, mode)

def read_only_copy(source, dest):
	"""This creates a read only copy of source
	because it is read only, we can make it a link
	"""
	shutil.copy(source, dest)
	set_read_only(dest)

def make_read_only_copy_writable(filename):
	"""Files created with read_only_copy can be made writable with this
	"""
	if hasattr(os, 'symlink'):
		# Check if we have already de-link-ified it
		if os.path.islink(filename):
			real_path = os.readlink(filename)
			os.unlink(filename)
			shutil.copy(real_path, filename)
			set_read_only(filename, writable=True)
 		elif read_only(filename):
			# Ensure set to writable, file system not supporting simlinks may have been RO.
			set_read_only(filename, writable=True)
	else:
		set_read_only(filename, writable=True)
