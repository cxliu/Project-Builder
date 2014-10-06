#!/usr/bin/env python

"""usage: %prog [OPTIONS] destination keyword1,keyword2...

This will do a perforce integrate from the root manifest directory to the
destination given (as a perforce depot path).

This command will never submit the changelist.

Your root manifest directory must be mapped into the selected p4 workspace.
"""

import optparse
import os
import stat
import sys
import getpass
import socket
import shutil

# Used for manipulating perforce paths where we always want the path
# separator to be a forward slash
import posixpath

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import m2
from src.build import error_messages
from src.p4 import p4_command

class TagError(Exception): pass

def simulate_bulk_copy(copies, verbose):
	assert isinstance(copies, list)
	assert all([len(c) == 2 for c in copies])
	assert all([isinstance(src, str) and isinstance(dest, str) for src, dest in copies])
	assert verbose in (True, False)
	
	for src, dest in copies:
		try:
			if verbose:
				print "cp %s %s" % (src, dest)
			dest_dir = os.path.dirname(dest)
			if not os.path.exists(dest_dir):
				os.makedirs(dest_dir)
			shutil.copy2(src, dest)
		except IOError, e:
			print(str(e))

	return 0

def simulate_branch(manifest, dest_base, keywords, exclude_tags, rename_tags, verbose):
	assert isinstance(dest_base, str)
	assert isinstance(keywords, list)
	assert isinstance(exclude_tags, list)
	assert isinstance(rename_tags, list)
	assert verbose in (True, False)
	
	source_root = os.path.dirname(os.path.realpath(manifest.get_root_manifest()))
	
	all_keywords = ['default'] + keywords
	local_path_info = m2.LocalPath()
	base_path_info = m2.PosixPath(source_root)
	
	copies = []
	for f in manifest.get_file_set(all_keywords, obey_exclusive=False, exclude_tags=exclude_tags):
		source_fs = os.path.realpath(f.get_path(local_path_info))
		source_from_base = f.get_path(base_path_info)
		dest_fs = os.path.join(dest_base, source_from_base)

		# Handle rename tags
		rename_tag = None
		for name, arguments, path in f.get_tags():
			if name in rename_tags:
				if rename_tag is None:
					if len(arguments) != 1:
						raise TagError("File %s has rename tag %s with the wrong number of arguments (expected 1)" % (source_fs, name))
					else:
						rename_tag = (arguments[0], path)
				else:
					raise TagError("File %s has multiple rename tags applied to it" % (source_fs))
		
		if not rename_tag is None:
			# Need to do a rename
			dest_fs = os.path.join(dest_base, base_path_info.write_path(rename_tag[1]), rename_tag[0].replace('*', os.path.relpath(source_fs, rename_tag[1])))
			dest_fs = os.path.normpath(dest_fs)
		copies.append((source_fs, dest_fs))

	return simulate_bulk_copy(copies, verbose)

def p4_branch(manifest, p4, dest_base, keywords, exclude_tags, rename_tags, verbose):
	assert isinstance(dest_base, str)
	assert dest_base.startswith('//')
	assert isinstance(keywords, list)
	assert isinstance(exclude_tags, list)
	assert isinstance(rename_tags, list)
	assert verbose in (True, False)
	
	source_root_where = p4.where(os.path.realpath(manifest.get_root_manifest()))
	
	all_keywords = ['default'] + keywords
	local_path_info = m2.LocalPath()
	base_path_info = m2.PosixPath(os.path.split(source_root_where['client_fs'])[0])
	
	# Work out the base of our source (i.e. the depot path of the root
	# manifest's directory)
	source_base = '/'.join(source_root_where['depot'].split('/')[0:-1])
	
	copies = []
	for f in manifest.get_file_set(all_keywords, obey_exclusive=False, exclude_tags=exclude_tags):
		source_fs = os.path.realpath(f.get_path(local_path_info))
		source_from_base = f.get_path(base_path_info)
		source_p4 = '%s/%s' % (source_base, source_from_base)
		dest_p4 = '%s/%s' % (dest_base, source_from_base)
		
		# Handle rename tags
		rename_tag = None
		for name, arguments, path in f.get_tags():
			if name in rename_tags:
				if rename_tag is None:
					if len(arguments) != 1:
						raise TagError("File %s has rename tag %s with the wrong number of arguments (expected 1)" % (source_fs, name))
					else:
						rename_tag = (arguments[0], path)
				else:
					raise TagError("File %s has multiple rename tags applied to it" % (source_fs))
			
		if not rename_tag is None:
			dest_p4 = '%s/%s/%s' % (dest_base, base_path_info.write_path(rename_tag[1]), rename_tag[0].replace('*', posixpath.relpath(source_fs, rename_tag[1])))
			dest_p4 = posixpath.normpath(dest_p4)
				
		
		if verbose:
			print "p4 integ %s %s" % (source_p4, dest_p4)
		copies.append((source_p4, dest_p4))
	
	changelist = p4.get_changelist_number()
	p4.bulk_copy(changelist, copies)
	
	return changelist

def main(args):
	parser = optparse.OptionParser(__doc__)
	parser.add_option("-m", "--manifest", dest="manifest",
	                  default=os.path.join(BASE, 'manifest.mb'),
	                  help="Choose a root manifest to use")
	
	parser.add_option("-x", "--exclude", dest="exclude",
	                  default=[], action='append',
	                  help="Exclude files with the given tag. This may be passed multiple times.")

	parser.add_option("-s", "--simulate", dest="simulate",
	                  default=False, action='store_true',
	                  help="Simulate a branch action without using p4. Pass a local path as the branch destination.")
	
	parser.add_option("--rename-tag", dest="rename_tags", metavar="TAG",
	                  default=[], action='append',
	                  help="Rename any files tagged with TAG according to the argument to the tag. This may be passed multiple times. If the argument to the tag contains the character '*', it is replaced with the path of the file being renamed, relative to the tag.")
	
	parser.add_option("-v", "--verbose", dest="verbose",
	                  default=False, action='store_true',
	                  help="Display the names of the files being copied.")
	
	default_port = os.getenv('P4PORT', 'corvus.dolby.net:1999')
	default_user = os.getenv('P4USER', getpass.getuser())
	default_password = os.getenv('P4PASSWD', '%s4%s' % (default_user, default_user))
	default_workspace = os.getenv('P4CLIENT', '%s_%s' % (default_user, socket.gethostname()))
	
	parser.add_option("--perforce-port", dest="perforce_port",
	                  default=default_port,
	                  help="Set the server port (default '%s')." % default_port)
	parser.add_option("--perforce-user", dest="perforce_user",
	                  default=default_user,
	                  help="Set the perforce username (default '%s')" % default_user)
	parser.add_option("--perforce-password", dest="perforce_password",
	                  default=default_password,
	                  help="Set the perforce password")
	parser.add_option("--perforce-workspace", dest="perforce_workspace",
	                  default=default_workspace,
	                  help="Set perforce workspace name (default '%s')" % default_workspace)
	
	
	
	(options, args) = parser.parse_args(args=args)
	
	if len(args) != 3:
		parser.error("You must pass the destination depot path and the keywords to use.")
	
	# Load manifest
	try:
		manifest = m2.M2(options.manifest)
	except error_messages.ManifestError, e:
		print(str(e))
		return 1
	
	dest = args[1]
	keywords = args[2].split(',')

	if options.simulate:
		return simulate_branch(manifest, dest, keywords, options.exclude,
		                       options.rename_tags, options.verbose)
	else:
		p4 = p4_command.P4Command(options.perforce_port,
		                          options.perforce_user,
		                          options.perforce_password,
		                          options.perforce_workspace,
		                          loud=False)
	
		changelist_number = p4_branch(manifest, p4, dest, keywords,
		                              options.exclude, options.rename_tags,
		                              options.verbose)
		print changelist_number
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))

