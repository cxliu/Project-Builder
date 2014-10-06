import os
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(os.path.join(BASE, 'mbuild'))

from src.build import m2
from src.build import p2
from src.build import plugin_manager

def get_projects(manifest, project_filter, force_dimensions):
	# Load p2 plugin
	try:
		p2_plugin_manager = plugin_manager.PluginManager(manifest, p2, [])
	except plugin_manager.PluginError, err:
		print str(err)
		return 1
	
	# Load projects
	project_loader = p2.ProjectLoader(manifest, p2_plugin_manager, force_dimensions)
	project_files = manifest.find_file_pattern(['default'], m2.LocalPath(), '*.project')
	projects = []
	for project_file in project_files:
		if project_filter(project_file):
			project_name = os.path.basename(project_file)
			base_name = os.path.splitext(project_name)[0]
			project = project_loader.get_project(base_name)
			projects.append(project)
	return projects, project_loader
