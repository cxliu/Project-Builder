import os
import ntpath
import sys

import visual_studio
import vc_configuration

from src.util import path_ex
from src.util import try_write

# The indent function
tab = visual_studio._indent


class VcSolution(object):
	def __init__(self, project, filename, manifest, configs, vc_projects, verbose_listing, newline, vs_version):
		assert all([isinstance(c, vc_configuration.VcConfiguration) for c in configs])
		self._project = project
		self._filename = filename
		self._manifest = manifest
		self._configurations = configs
		self._verbose = verbose_listing
		self.projects_updated = 0 
		self.projects_failed = 0 
		self.projects_attempted = 0 
		self._newline = newline
		self._vs_version = vs_version
		assert(newline in ['\n', '\r\n'])
		
		# Work out our dependencies... 
		# TODO: this looks a little bit backwards
		self._depends = {}
		for d in project.get_all_dependencies():
			for name, vc_proj in vc_projects.iteritems():
				if vc_proj.get_project().get_name() == d.get_name():
					if vc_proj.has_any_configuration(configs):
						self._depends[vc_proj.get_project().get_name()] = vc_proj
		
	
	def get_project(self):
		return self._project
	
	def get_filename(self):
		return self._filename
	
	def sorted_configurations(self):
		return sorted(self._configurations, key=lambda a: a.get_vs_identifier())
	
	@staticmethod
	def _project_sort_order(main_project, a, b):
		"""When sorting the projects, we always want the first project to be
		the one with the same name as this solution so it is chosen as the
		startup project. This defines that sort order.
		"""
		if a.get_project().get_project_filename() == b.get_project().get_project_filename():
			return 0
		if a.get_project().get_project_filename() == main_project.get_project_filename():
			return -1
		if b.get_project().get_project_filename() == main_project.get_project_filename():
			return 1
		return cmp(a.get_project().get_project_filename(), b.get_project().get_project_filename())

	def _projects_wanting_config(self, config):
		"""Returns a list of all projects that want this build config
		"""
		ret = []
		for p in self.vc_projects.values():
			if p.name in self.config_projects:
				if config in p.sorted_configurations():
					ret.append(p)
		return ret

	def write_out(self, manifest, path_getter):

		path_ex.makedirs(os.path.dirname(self._filename))

		contents  = ["Microsoft Visual Studio Solution File, Format Version %s" % {'2005':'9.00', '2008':'10.00', '2010':'11.00', '2012':'12.00', '2013':'12.00'}[self._vs_version]]
		contents.append("# Visual Studio %s" % self._vs_version)
		contents += self._write_projects()
		contents.append("Global")
		contents.append("	GlobalSection(SolutionConfigurationPlatforms) = preSolution")
		contents += self._write_solution_configuration(manifest)
		contents.append("	EndGlobalSection")
		contents.append("	GlobalSection(ProjectConfigurationPlatforms) = postSolution")
		contents += self._write_project_configuration(manifest)
		contents.append("	EndGlobalSection")
		contents.append("	GlobalSection(SolutionProperties) = preSolution")
		contents.append("		HideSolutionNode = FALSE")
		contents.append("	EndGlobalSection")
		contents.append("EndGlobal")
		
		# Use the correct newline
		contents_str = self._newline.join(contents) + self._newline

		result = try_write.try_write(self._filename, contents_str, text_mode=False, overwrite=True)
		self.projects_attempted += 1 
		self.notify_write_out(result)
		return result

	def _write_projects(self, indent=0):
		
		ret = []
		for vc_proj in sorted(self._depends.values(), cmp=lambda a, b: self._project_sort_order(self._project, a, b)):
			p = vc_proj.get_project()
			ret.append(tab(indent) + 'Project("{%s}") = "%s", "%s", "{%s}"' % \
				(visual_studio.solution_guid(), 
				 p.get_name(), 
				 path_ex.make_path_relative(vc_proj.get_filename(), os.path.dirname(self._filename), ntpath),
				 vc_proj.get_guid()))
			if len(p.get_dependencies()) > 0:
				ret.append(tab(indent + 1) + 'ProjectSection(ProjectDependencies) = postProject')
				for d in p.get_dependencies():
					dep_vc_proj = self._depends[d]
					ret.append(tab(indent + 2) + '{%s} = {%s}' % (dep_vc_proj.get_guid(), dep_vc_proj.get_guid()))
				ret.append(tab(indent + 1) + 'EndProjectSection')
			ret.append(tab(indent) + 'EndProject')
		return ret

	def _write_solution_configuration(self, manifest, indent=2):
		ret = []
		
		for c in self.sorted_configurations():
			ret.append(tab(indent) + "%s = %s" % (c.get_vs_full_identifier(), c.get_vs_full_identifier()))
		
		return ret

	def _write_project_configuration(self, manifest, indent=2):
		ret = []
		for c in self.sorted_configurations():
			for p in sorted(self._depends.values(), key=lambda a: a.get_project().get_project_filename()):
				project_config = vc_configuration.VcConfiguration(manifest, p.get_project(), c.get_configuration(), self._vs_version)	
				
				ret.append(tab(indent) + "{%s}.%s.ActiveCfg = %s" % (p.get_guid(), c.get_vs_full_identifier(), project_config.get_vs_full_identifier()))
				ret.append(tab(indent) + "{%s}.%s.Build.0 = %s" % (p.get_guid(), c.get_vs_full_identifier(),  project_config.get_vs_full_identifier()))
		return ret

	def notify_write_out(self, result):
		if result == try_write.CHANGED:
			print("Writing VS%s solution: %s ..." % (self._vs_version, self._filename)),
			print(" ok (updated)")
			self.projects_updated += 1
		elif result == try_write.NO_CHANGE:
			if self._verbose:
				print("Writing VS%s solution: %s ..." % (self._vs_version, self._filename)),
				print(" ok")
		elif result == try_write.COULDNT_CHANGE:
			print("Writing VS%s solution: %s ..." % (self._vs_version, self._filename)),
			print(" couldn't update")
			self.projects_failed += 1 
		
