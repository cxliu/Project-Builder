#!/usr/bin/env python

"""usage: %prog [options]

This script will create documentation for a manifest (and its
submanifests) based on its @doc tags. 
"""

import optparse
import os
import sys
import re

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import m2
from src.build import error_messages
from src.util import path_ex

class HTMLData:

	def __init__(self, title):
		self._html = []
		self._generate_header(title)
		self._complete = False
		
	def _generate_header(self, title):
		self._html.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">')
		self._html.append('<html>')
		self._html.append('<head>')
		# strip tags from title
		self._html.append('<title>%s</title>' % re.sub('<.*?>', '', title))
		self._html.append('</head>')
		self._html.append('<body>')
		self._html.append('<h2>%s</h2>' % title)
	
	def begin_table(self, header):
		self._html.append('<table width="100%" border="1">')
		self._html.append('<h4><strong>%s</strong></h4>' % header)
		
	def end_table(self):
		self._html.append('</table>')
		self._html.append('<br/>')
		
	def add_row(self, key, text):
		assert not self._complete
		self._html.append('<tr valign="top" halign="left">')
		# format string doesn't like percent sign literal
		self._html.append(''.join(['<td width="20%">', key, '</td>']))
		self._html.append(''.join(['<td width="80\=%">', text, '</td>']))
		self._html.append('</tr>')
	
	def finish(self):
		self._html.append("</table>\n</body>")
		self._complete = True
		
	def __str__(self):
		assert self._complete
		return '\n'.join(self._html)

def main(args):
	parser = optparse.OptionParser(__doc__)
	parser.add_option("-m", "--manifest", dest="manifest_path",
	                  action="store", default=os.path.join(BASE, 'manifest.mb'),
	                  help='Set the root manifest file to use.')
	parser.add_option("-f", "--file", dest="doc_file_path",
	                  action="store", default=os.path.join(BASE, 'doc.html'),
					  help='Set the location to write doc file.')
	parser.add_option("-p", "--project", dest="project_name",
                      action="store", default='',
					  help='Set the name of the project for titling purposes.')

	options, args = parser.parse_args(args[1:])
	if len(args) > 0:
		parser.error("unexpected arguments %s" % args)
	
	try:
		m = m2.M2(options.manifest_path)
	except error_messages.ManifestError as err:
		print()
		print(err)
		return 1
	
	
	if options.project_name == '':
		doc_dir = os.path.dirname(os.path.abspath(options.doc_file_path))
		project_name = os.path.basename(doc_dir)
	else:
		project_name = options.project_name
	title = "M-Build Metadata for <em>%s</em>" % project_name
	
	html = HTMLData(title)
	
	html.begin_table("Enums")
	enums = m.get_enums()
	for enum_name, enum_map in sorted(enums.items()):
		for enum_key, enum_doc in sorted(enum_map.items()):
			html.add_row('%s.%s' % (enum_name, enum_key), enum_doc)
	html.end_table()
	

	docs = m.get_docs()
	for doc_type, doc_type_map in sorted(docs.items()):
		html.begin_table(m2.Documentation.get_display_string(doc_type))
		for doc_key, doc_obj in sorted(doc_type_map.items()):
			html.add_row(doc_obj.get_key(), doc_obj.get_text())
		html.end_table()
	
	html.finish()
	
	try:
		path_ex.makedirs(os.path.dirname(options.doc_file_path))
		doc_file = open(options.doc_file_path, 'w')
		doc_file.write(str(html))
		doc_file.close()
	except IOError as err:
		print()
		print(err)
		return 2
			
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
