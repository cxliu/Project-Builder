#!/usr/bin/env python
import unittest
import os
import sys

THIS_DIR = os.path.join(os.path.dirname(__file__))
BASE = os.path.join(THIS_DIR, '..', '..')
sys.path.append(os.path.join(BASE, "src", "build"))
sys.path.append(os.path.join(BASE, "src", "visual_studio"))
import m2
import p2
import plugin_manager
import error_messages
import vc_configuration

TESTCASES = os.path.join(BASE, "src", "test", "testcases")

class ProjectTest(unittest.TestCase):
	def __init__(self, root_manifest):
		unittest.TestCase.__init__(self)
		self._root_manifest = root_manifest
	
	def _diff(self, reference, other):
		"""File diff. 
		Also handles DOS/UNIX line endings.
		"""
		
		try:
			f0 = open(reference, "rU")
		except IOError, err:
			assert False, "Error opening reference file: %s" % err
		try:
			f1 = open(other, "rU")
		except IOError, err:
			assert False, "Error opening file: %s" % err

		line_no = 1
		for line_0 in f0:
			line_1 = f1.readline()
			assert line_0 == line_1, \
				"%s and %s differ at line number %d (\n%s\n%s\n)" % (reference, other, line_no, line_0, line_1)
			
			line_no += 1

		assert not f1.readline(), "File %s is longer than %s" % (other, reference)
		
	def shortDescription(self):
		return "project test"
	
	def runTest(self):
		manifest = m2.M2(self._root_manifest)
		p2_plugin_manager = plugin_manager.PluginManager(manifest, p2, [])
		project_loader = p2.ProjectLoader(manifest, p2_plugin_manager)
		project_files = manifest.find_file_pattern(['default'], m2.LocalPath(), '*.project')
		projects_obj = {}
		for project_file in project_files:
			project_name = os.path.splitext(os.path.basename(project_file))[0]
			projects_obj.update({project_name:project_loader.get_project(project_name)})
		
		for project_name in sorted(projects_obj.keys()):
			# find project obj
			project = projects_obj[project_name]
			target = os.path.join(TESTCASES, "backend", "output", project_name, project_name+"_info.txt")
			ref = os.path.join(TESTCASES, "backend", "reference", project_name, project_name+"_info.txt")
			
			# dependencies
			dependency_info = ["# Project immediate dependencies:"]
			for depend in sorted(project.get_dependencies()):
				dependency_info.append(depend)
			dependency_info.append("\n# Project all dependencies:")
			depends = project.get_all_dependencies()
			for depend in depends:
				base_name = os.path.basename(depend.get_project_filename())
				dependency_info.append(os.path.splitext(base_name)[0])
			dependency_info.append("")
			
			# actions
			actions_info = ["# Project actions:"]
			actions_info.append(str(sorted(project.get_actions())))
			actions_info.append("")
			
			# dimensions
			dimensions_info = ["# Project dimensions:"]
			dimensions_info.append(str(project.get_dimensions()))
			dimensions_info.append("")
			
			# configurations
			configurations_info = generate_build_info(project)
			
			# join all info sections together
			contents = []
			contents.extend(dependency_info)
			contents.extend(actions_info)
			contents.extend(dimensions_info)
			contents.extend(configurations_info)
			
			# write info to output file
			target_handle = open(target, "w")
			target_handle.write("\n".join(contents))
			target_handle.close()
			
			self._diff(ref, target)
			
def str_ordered(dictionary):
	"""Returns the equivalent to repr(dictionary), but with the keys in sorted
	order"""
	ret = "{%s}" % ", ".join(['%r: %r' % (k, dictionary[k]) for k in sorted(dictionary.keys())])
	return ret
	
def generate_build_info(project):
	configurations = p2.Project.get_configurations(project)
	out = []
	out.append("# Project configurations (total:%d):" % len(configurations))
	for config in configurations:
		out.append(str_ordered(config))
	out.append("")
	return out
	
def setup_p2_suite():
	p2_suite = unittest.TestSuite()
	
	p2_suite.addTest \
		(ProjectTest \
		    ("testcases/backend/input/manifest.mb"
		    )
		)
	
	return p2_suite
	
def main(args):
	
	p2_suite = setup_p2_suite()
	unittest.TextTestRunner(descriptions=True, verbosity=2).run(p2_suite)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
