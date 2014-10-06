#!/usr/bin/env python

"""%prog [options] COMMANDS

Where COMMANDS can be:
	attribute-setters <attribute name>
		Print out all clauses that set the given attribute, and what 
		they set it to.

	keyword-adders <keyword name>
		Print out all clauses that @add the given keyword.

	list-all-attributes <starting_keywords>
		Print out the (alphabetically sorted) list of all attributes
		and their values derived from the <starting_keywords>.
		The 'default' keyword is assumed.

	list-all-files <starting_keywords>
		Print out the list of files and their tags derived from the
		<starting_keywords>. The 'default' keyword is assumed.

	expanded-keywords <starting_keywords>
		Print out the list of the expanded keywords derived from the
		<starting_keywords>. The 'default' keyword is assumed.

	why-is-keyword-set <keyword> <starting_keywords>
		Give a derivation from <starting_keywords> which ends up with
		keyword being set. The 'default' keyword is assumed.

	how-did-this-attribute-get-its-value <attribute> <starting_keywords>
		Show all of the clauses that were considered for the value of
		this attribute. The 'default' keyword is assumed.
		
When giving multiple keywords, you should separate them with commas and no
whitespace.
"""

import os
import sys
import optparse

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import m2
from src.build import error_helper

def main(argv):
	parser = optparse.OptionParser()
	
	parser.usage = __doc__
	parser.add_option("-m", "--manifest", action="store", dest="manifest",
	                  default=os.path.join(BASE, 'manifest.mb'),
	                  help="Select the root manifest file to use")
	
	(options, args) = parser.parse_args(argv)
	
	manifest = m2.M2(options.manifest)
	
	args.reverse()
	while len(args) > 0:
		cmd = args.pop()
		if cmd == 'attribute-setters':
			attribute = args.pop()
			for outcome in error_helper.what_sets_this_attribute(manifest, attribute):
				print "# %s" % outcome.get_position()
				print "[%s]" % (outcome.get_keyword_expression().simplify(set(['default'])))
				print "@att %s = %s\n" % (outcome.get_key(), outcome.get_value())

		if cmd == 'keyword-adders':
			keyword = args.pop()
			for c, pos in error_helper.what_adds_this_keyword(manifest, keyword):
				print "# %s" % pos
				print "[%s]" % (c.get_keyword_expression().simplify(set(['default'])))
				print "@add %s\n" % (keyword)
		
		if cmd == 'how-did-this-attribute-get-its-value':
			attribute = args.pop()
			starting_keywords = args.pop().split(',')
			starting_keywords.append("default")
			for outcome in error_helper.how_did_this_attribute_get_its_value(manifest, attribute, starting_keywords):
				print "# %s" % outcome.get_position()
				print "[%s]" % (outcome.get_keyword_expression().simplify(set(['default'])))
				print "@att %s = %s\n" % (outcome.get_key(), outcome.get_value())

		if cmd == 'list-all-attributes':
			starting_keywords = args.pop().split(',')
			starting_keywords.append("default")
			all_attribs = manifest.get_all_attributes(starting_keywords, m2.LocalPath())
			akeys = sorted(all_attribs.keys())
			for k in akeys:
				print "%-35s\t%s" % (k, all_attribs.__getitem__(k))
		
		if cmd == 'list-all-files':
			starting_keywords = args.pop().split(',')
			starting_keywords.append("default")
			all_files = manifest.get_file_set(starting_keywords, obey_exclusive=False)
			for f in all_files:
				assert isinstance(f, m2.FileInfo)
				tags = f.get_tags()
				prefix = ''
				if len(tags) > 0:
					tag_text = []
					for t in tags:
						tag_name, tag_args, tag_path = t  #@UnusedVariable warning suppression
						if tag_args is None:
							tag_text.append('%s' % (tag_name))
						else:
							tag_text.append('%s(%s)' % (tag_name, ', '.join(tag_args)))
						
					prefix = '%s:' % (' '.join(tag_text))
					
				print prefix + f.get_filename()
		
		if cmd == 'why-is-keyword-set':
			keyword = args.pop()
			args.reverse()
			starting_keywords = args
			starting_keywords.append("default")
			for reason, kw, c, pos in error_helper.why_is_this_keyword_set(manifest, keyword, starting_keywords):
				if reason:
					print "Error: %s" % reason
				else:
					print "# %s" % pos
					print "[%s]" % (c.get_keyword_expression().simplify(set(['default'])))
					print "@add %s\n" % (kw)

		if cmd == 'expanded-keywords':
			starting_keywords = args.pop().split(',')
			print "starting_keywords: [%s %s]" % ("(default)", ' '.join(sorted(starting_keywords)))
			starting_keywords.append("default")
			expanded_keywords = error_helper.get_expanded_keywords(manifest, starting_keywords)
			exp_keywords_set = set(expanded_keywords) - frozenset(['default'])
			print "expanded_keywords: [%s %s]" % ("(default)", ' '.join(sorted(exp_keywords_set)))

			# all args are treated as starting keywords - no more commands
			break

if __name__ == '__main__':
	sys.exit(main(sys.argv))

