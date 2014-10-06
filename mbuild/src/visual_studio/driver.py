import sys
import os
BASE = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(os.path.join(BASE, 'script'))


from src.build import plugin_manager
from src.build import p2
from src.build import m2
from src.visual_studio import vc_project
from src.visual_studio import solution
from src.visual_studio import vc_configuration
from src.util import try_write
from src.util import path_ex
import visual_studio


class CouldntWriteFileError(Exception):
	def __init__(self, vc_proj):
		self.vc_proj = vc_proj


def make(verbose_listing, output_dir, skip_non_writeable, manifest, path_transform, all_projects, project_filter, dimensions, newlines):

	failures_found = False

	total_failed = 0
	total_attempted = 0
	total_updated = 0
	all_vc_projects = {}
	all_failed_projects = []
	all_failed_solutions = []
	
	for vs_version in visual_studio.SUPPORTED_VS_VERSIONS:
		
		# Create visual studio objects
		vc_projects  = create_vc_projects(manifest, all_projects, vs_version, output_dir, dimensions, verbose_listing)
		vc_solutions = create_vc_solutions(manifest, vc_projects, vs_version, output_dir, dimensions, verbose_listing, newlines)
		
		failed_projects  = write_vc_projects(vc_projects, manifest, path_transform, project_filter)
		failed_solutions = write_vc_solutions(vc_solutions, manifest, path_transform, project_filter)
		
		if not skip_non_writeable:
			all_vc_projects.update(vc_projects)
			all_failed_projects  += failed_projects
			all_failed_solutions += failed_solutions

		# Display summary of files produced
		failed = 0
		attempted = 0
		updated = 0
		for vcIdx in vc_projects:
			failed += vc_projects[vcIdx].projects_failed
			attempted += vc_projects[vcIdx].projects_attempted
			updated += vc_projects[vcIdx].projects_updated

		total_failed += failed
		total_attempted += attempted
		total_updated += updated
		print("\nStudio %s projects checked: %d, updated: %d, failed: %d" % (vs_version, attempted, updated, failed))
		
		failed = 0
		attempted = 0
		updated = 0
		for vcIdx in vc_solutions:
			failed += vc_solutions[vcIdx].projects_failed
			attempted += vc_solutions[vcIdx].projects_attempted
			updated += vc_solutions[vcIdx].projects_updated
		
		total_failed += failed
		total_attempted += attempted
		total_updated += updated
		
		print("\nStudio %s solutions checked: %d, updated: %d, failed: %d" % (vs_version, attempted, updated, failed))
	
	if (len(all_failed_projects) > 0 or len(all_failed_solutions) > 0) and not skip_non_writeable:
		updated_num = process_failed_vc_project_files(all_vc_projects, all_failed_projects, all_failed_solutions, manifest, path_transform)
		total_failed -= updated_num
		total_updated += updated_num
		
	print("\n---\n")
	print("All files checked: %d, updated: %d, failed: %d" % (total_attempted, total_updated, total_failed))

	if total_failed > 0:
		print("\nWARNING: Some files could not be updated!")

def process_failed_vc_project_files(vc_projects, failed_projects, failed_solutions, manifest, path_transform):
	updated_num = 0
	while failed_solutions or failed_projects:
		print "\nWARNING: The following VS project files have changed, but are not updated"
		for vc_prject in failed_projects:
			print "\t%s" % (vc_prject.get_filename())
		for vc_solution in failed_solutions:
			print "\t%s" % (vc_solution.get_filename())
		rewrite = raw_input("\nDo you want to try again? (Y/N) ")
		if rewrite.lower() in ['y', 'yes']:
			updated_projects = []
			for vc_project in failed_projects:
				result = vc_project.write_out(path_transform, vc_projects)
				if result == try_write.CHANGED:
					updated_projects.append(vc_project)
					updated_num += 1
			for vc_project in updated_projects:
				failed_projects.remove(vc_project)
			
			updated_solutions = []
			for vc_solution in failed_solutions:
				result = vc_solution.write_out(manifest, path_transform)
				if result == try_write.CHANGED:
					updated_solutions.append(vc_solution)
					updated_num += 1
			for vc_solution in updated_solutions:
				failed_solutions.remove(vc_solution)
		else:
			break
	return updated_num


def _get_filtered_configurations(configurations, dimensions, vs_version):
		filtered_configurations = [c for c in configurations if c['tool'] == 'msvs%s' % vs_version]
		if dimensions:
			filtered_configurations = [conf for conf in filtered_configurations if 
			   reduce(lambda x, y: x and y, [conf[key] in dimensions[key] for key in dimensions.keys()])]
		
		return filtered_configurations

def create_vc_projects(manifest, projects, vs_version, output_dir, dimensions, verbose_listing):
	assert vs_version in visual_studio.SUPPORTED_VS_VERSIONS
	
	# Get constructor for our version
	cons = {'2005': vc_project.Vc2005Project,
	        '2008': vc_project.Vc2008Project,
	        '2010': vc_project.Vc2010Project,
	        '2012': vc_project.Vc2012Project,
	        '2013': vc_project.Vc2013Project}[vs_version]
	
	# And file extension
	ext = {'2005': '.vcproj',
	       '2008': '.vcproj',
	       '2010': '.vcxproj',
	       '2012': '.vcxproj',
	       '2013': '.vcxproj'}[vs_version]
	
	ret = {}
	for p in projects:
		configs = _get_filtered_configurations(p2.Project.get_configurations(p), dimensions, vs_version)
		project_configs = {}
		for c in configs:
			name = p.get_output_name('compile', c)
			assert name[-1] is None, "Didn't expect a filename for a compile step"
			
			name[-1] = '_'.join([p.get_name(), vs_version])
			vc_proj_filename_base = os.path.join(*name)
			
			if not vc_proj_filename_base in project_configs:
				project_configs[vc_proj_filename_base] = []
			
			project_configs[vc_proj_filename_base].append(vc_configuration.VcConfiguration(manifest, p, c, vs_version))
			
		for filename, configs in project_configs.iteritems():
			output_file_base = _get_output_file(p, filename, manifest, output_dir)
			output_file = output_file_base + ext
			ret[filename] = cons(p, output_file, manifest, configs, verbose_listing)
	
	return ret

def create_vc_solutions(manifest, vc_projects, vs_version, output_dir, dimensions, verbose_listing, newlines):
	assert vs_version in visual_studio.SUPPORTED_VS_VERSIONS
	
	ext = '.sln'
	
	ret = {}
	for vc_proj in vc_projects.values():
		# Only make solutions for projects that require linking
		p = vc_proj.get_project()
		if 'link' in p.get_actions():
			configs = _get_filtered_configurations(p2.Project.get_configurations(p), dimensions, vs_version)
			project_configs = {}
			for c in configs:
				name = p.get_output_name('link', c)
				assert not name[-1] is None, "Expected a filename for a link step"
				
				name[-1] = '_'.join([p.get_name(), vs_version])
				vc_sln_filename_base = os.path.join(*name)
				
				if not vc_sln_filename_base in project_configs:
					project_configs[vc_sln_filename_base] = []
				
				project_configs[vc_sln_filename_base].append(vc_configuration.VcConfiguration(manifest, p, c, vs_version))
			
			for filename, configs in project_configs.iteritems():
				output_file_base = _get_output_file(p, filename, manifest, output_dir)
				output_file = output_file_base + '.sln'
				ret[filename] = solution.VcSolution(p, output_file, manifest, configs, vc_projects, verbose_listing, newlines, vs_version)
	
	return ret

def write_vc_projects(vc_projects, manifest, path_transform, project_filter):
	failed_projects = []
	for name in sorted(vc_projects.keys()):
		vc_proj = vc_projects[name]
		
		if not project_filter(vc_proj.get_project().get_project_filename()):
			continue
		
		try:
			if vc_proj.write_out(path_transform, vc_projects) == try_write.COULDNT_CHANGE:
				failed_filename = vc_proj.get_filename()
				raise CouldntWriteFileError(failed_filename)
		except CouldntWriteFileError, err:
			failed_projects.append(vc_proj)
	return failed_projects

def write_vc_solutions(vc_solutions, manifest, path_transform, project_filter):
	failed_solutions = []
	for name in sorted(vc_solutions.keys()):
		vc_sol = vc_solutions[name]
		try:
			if not project_filter(vc_sol.get_project().get_project_filename()):
				continue
			if vc_sol.write_out(manifest, path_transform) == try_write.COULDNT_CHANGE:
				failed_filename = vc_sol.get_filename()
				raise CouldntWriteFileError(failed_filename)
		except CouldntWriteFileError, err:
			failed_solutions.append(vc_sol)
	
	return failed_solutions

def _get_output_file(project, filename, manifest, output_dir):
	if output_dir is None:
		return os.path.join(os.path.dirname(project.get_project_filename()), filename)
	else:
		project_dir = os.path.dirname(project.get_project_filename())
		rel_project_dir = path_ex.make_path_relative(project_dir, 
		                                             os.path.dirname(manifest.get_root_manifest()), os.path)
		return os.path.join(output_dir, rel_project_dir, filename)
