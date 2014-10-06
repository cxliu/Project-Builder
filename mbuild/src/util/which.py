import os

def which(cmd, mode=os.F_OK | os.X_OK, path=None):
	# A clone of shutil.which from python 3.3+
	env = os.environ
	if path is None:
		if 'PATH' in env:
			path = env['PATH']
		else:
			path = os.defpath
	
	pathext = ''
	if 'PATHEXT' in env:
		pathext = env['PATHEXT']

	paths = path.split(os.pathsep)
	if os.name == 'nt':
		paths = ['.'] + paths
	
	pathexts = [''] + pathext.split(os.pathsep)
	
	for p in paths:
		for ext in pathexts:
			this_path = os.path.join(p, cmd + ext)
			if os.access(this_path, mode):
				return this_path
	
	return None

