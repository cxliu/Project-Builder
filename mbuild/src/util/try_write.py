"""This is for trying to write to a file without actually doing any write operations if the file
already contains the contents we want. This is useful for integrating with workflows that involve
readonly files.
"""

import os

NO_CHANGE=0
CHANGED=1
COULDNT_CHANGE=2

def try_write(filename, string, text_mode, overwrite):
	if text_mode:
		mode = 't'
	else:
		mode = 'b'
	
	# Read the file we are writing to (always as a binary file
	# so if the line endings are wrong, we correct them)
	try:
		f = open(filename, "rb")
		try:
			contents = f.read()
		except IOError, err:
			contents = None
		finally:
			f.close()
	except IOError, err:
		contents = None
	
	# Don't bother writing if we aren't going to change the file.
	compare_string = string
	if text_mode:
		compare_string = string.replace('\n', os.linesep)
	if contents == compare_string:
		return NO_CHANGE
	
	# Don't overwrite unless we are given permission
	if not contents is None and not overwrite:
		return COULDNT_CHANGE
	
	try:
		f = open(filename, "w" + mode)
		try:
			f.write(string)
			return CHANGED
		finally:
			f.close()
	except IOError, err:
		# File wasn't writable.
		return COULDNT_CHANGE
