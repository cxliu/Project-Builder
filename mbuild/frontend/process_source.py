#!/usr/bin/env python

"""usage: %prog [options] plugin1 plugin2 ...

This will process source files for a given manifest using the specified plugin chain.
At least one plugin must be specified.
"""

import optparse
import os
import sys
import shutil

BASE = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import error_messages
from src.build import m2
from src.build import p2
from src.build import ps
from src.build import plugin_manager
from src.util import path_ex

NO_ERROR = 0
ARG_ERROR = 1
MANIFEST_ERROR = 2

MOVE_TAG_STRING= 'move_to'

class ProcessSource:

	def __init__(self, target_folder, projects=[], dimensions = {}):
		self._projects_to_process = projects
		self._project_keywords = ['project_' + project for project in projects]
		self._dimensions = dimensions
		self._target_folder = target_folder
		
	def _move_keys_match_keywords(self, move_keys, keywords):
		if move_keys:
			return reduce(lambda x, y: x and y, [k in keywords for k in move_keys])
		else:
			return True
			
	def _get_move_keys_from_tag(self, t):
		return t['keywords']

	def _get_applicable_move_tags(self, file_info):
		raw_move_tags = [t for t in file_info.get_tags() if t[0] == MOVE_TAG_STRING]
		move_tags = []
		for t in raw_move_tags:
			tag_dict = {}
			move_spec = t[1]
			tag_dict['relative_dest_dir'] = move_spec[0]
			tag_dict['source_path'] = t[2]
			tag_dict['flatten'] = True
			keyword_index = 1
			rename_index = 2
			if len(move_spec) > keyword_index:
				tag_dict['keywords'] = move_spec[keyword_index].split('.')
			else:
				tag_dict['keywords'] = []
			if len(move_spec) > rename_index:
				tag_dict['rename'] = move_spec[rename_index]
			if self._move_keys_match_keywords(tag_dict['keywords'], file_info.get_keywords()):
				move_tags.append(tag_dict)
		return move_tags
		
	def _get_move_keys(self, file_info):
		applicable_move_tags = self._get_applicable_move_tags(file_info)
		if applicable_move_tags:
			return self._get_move_keys_from_tag(applicable_move_tags[-1])
		else:
			return []
			
	def _get_move_path(self, file_info):
		dest = None
		applicable_move_tags = self._get_applicable_move_tags(file_info)
		if applicable_move_tags:
			dest_tag = applicable_move_tags[-1]
			if dest_tag['flatten']:
				relative_dest_dir = dest_tag['relative_dest_dir']
			else:
				base_dir = os.path.join(dest_tag['source_path'], dest_tag['source_base_dir'])
				relative_path = path_ex.make_path_relative(os.path.abspath(file_info.get_filename()), base_dir, os.path)
				relative_dest_dir = os.path.join(dest_tag['relative_dest_dir'], os.path.dirname(relative_path))
			if 'rename' in dest_tag:
				basename = dest_tag['rename']
			else:
				basename = os.path.basename(file_info.get_filename())
			dest_dir = os.path.normpath(os.path.join(self._target_folder, relative_dest_dir))
			dest = os.path.join(dest_dir, basename)
		return dest
		
	def path_transform(self, file_info):
		move_path = self._get_move_path(file_info)
		if move_path is None:
			return file_info.get_filename()
		else:
			return move_path
		
	def set_target_folder(self, target_folder):
		self._target_folder = target_folder
		
	def _move(self, f, processed_files, verbose, preview):
		dest = self._get_move_path(f)
		move_keys = self._get_move_keys(f)
		report_string = ''
		if dest is not None and not dest in processed_files['move']:
			src = f.get_filename()
			if not preview:
				if not os.path.isdir(os.path.dirname(dest)):
					os.makedirs(os.path.dirname(dest))
				# copyfile instead of copy, so dest is unlocked even if
				# src isn't
				shutil.copyfile(src, dest)
			processed_files['move'].add(dest)
			report_string = "Moved %s to %s" % (os.path.abspath(src), os.path.abspath(dest))
			if verbose:
				print report_string
		return (dest, move_keys, report_string)

	def process(self, manifest, plugins, action_base, verbose, preview, report_loc):

		processed_files = {}
		processed_files['move'] = set()
		for plugin in plugins:
			processed_files[plugin] = set()
		# Load plugins
		try:
			ps_plugin_manager = plugin_manager.PluginManager(manifest, ps, [])
			p2_plugin_manager = plugin_manager.PluginManager(manifest, p2, [])
		except error_messages.ManifestError as e:
			print e
			return MANIFEST_ERROR
			
		project_files = []
		projects = []
		project_loader = p2.ProjectLoader(manifest, p2_plugin_manager)
		if self._projects_to_process:
			for project in self._projects_to_process:
				project_files += manifest.find_file_pattern(['default'], m2.LocalPath(), '*' + project + '.project')
		else:
			project_files = manifest.find_file_pattern(['default'], m2.LocalPath(), '*.project')
		for proj in project_files:
			name = os.path.splitext(os.path.basename(proj))[0]
			project = project_loader.get_project(name)
			projects += project.get_all_dependencies()

		report = ''
		if report_loc is None:
			report_loc_to_use = os.path.join(BASE, 'process_source_report.txt')
		else:
			report_loc_to_use = report_loc
		print "Writing report to %s" % report_loc_to_use
		try:
			report_file = open(report_loc_to_use, 'w')
			for project in projects:
				report_file.write("PROJECT: %s\n" % project.get_name())
				if action_base in project.get_actions():
					#dims = project._get_dimension_values(manifest, project.get_dimensions())
					configurations = p2.Project.get_configurations(project)
					if self._dimensions:
						configurations = [conf for conf in configurations if 
							reduce(lambda x, y: x and y, [key in conf and conf[key] in self._dimensions[key] 
							for key in self._dimensions.keys()])]
					for configuration in configurations:
						report_file.write("%s\n" % str(configuration))
						spec_dict = {}
						keywords = project.get_keywords(configuration)
						for plugin in plugins:
							spec_method = plugin + '_get_spec'
							assert ps_plugin_manager.get_extensions().has_key(spec_method), "Unknown spec method %s" % spec_method
							spec_dict[plugin] = ps_plugin_manager.get_extensions()[spec_method](manifest, keywords)
						for f in manifest.get_file_set(keywords, exclude_tags=['internal']):
							new_loc, move_keys, move_report = self._move(f, processed_files, verbose, preview)
							if move_report:
								report_file.write("%s\n" % move_report)
							if new_loc is not None:
								for plugin in plugins:
									if not new_loc in processed_files[plugin]:
										process_method = ''.join([plugin, '_process_file'])
										# TODO: consider creating Plugin object to hold this kind of metadata
										assert ps_plugin_manager.get_extensions().has_key(process_method), "Unknown process method %s"                                                                   % process_method
										if move_keys:
											plugin_keys = move_keys
										else:
											plugin_keys = keywords
										report = ps_plugin_manager.get_extensions()[process_method](m2, 
											manifest, f, new_loc, plugin_keys,                                                            
											keywords, verbose, preview)
										if report:
											report_file.write("%s\n" % report)
										processed_files[plugin].add(new_loc)
						cleanup_method = ''.join([plugin, '_clean_up'])
						ps_plugin_manager.get_extensions()[cleanup_method](spec_dict[plugin])
				report_file.write("\n")
		finally:
			report_file.close()
		return NO_ERROR
	
