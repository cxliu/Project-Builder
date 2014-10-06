import fnmatch
import posixpath
from src.build import p2
from src.build import m2
import os


def get_plugin_pattern():
	return "*.t3_plugin"

def get_plugin_environment():
	return {'T3PluginError': T3PluginError}

class T3PluginError(Exception):
	def __init__(self, message):
		self._message = message
	
	def __str__(self):
		return "Makefile plugin error: %s" % (self._message)

# Variables which will be exported to the output Makefile
class MakeVar(object):
	INTERMEDIATE_OBJECT = 0
	RULE_VAR = 1
	COMMON_FILE_VAR = 2
	DEPENDENT_PROJECT_OUTPUT = 3 # e.g. libraries from dependent makefiles
	SIDE_PRODUCT = 4 # e.g. dependency files
	def __init__(self, value, name_basis, rule, separator):
		self.value = value                  # will result in the right side of equal sign
		self.name_basis = name_basis        # basis for the variable name, not including dimensions
		self.separator = separator          # if a variable follows this one, use this separator	
		self.var_configs = [rule.config]
		self.name = None                    # final constructed variable string, left of equal sign
		self.rule_name = rule.name          # name for the rule, if needed to generalize variables
		self.makevar_type = None
	
	def __str__(self):
		return "%s = %s" % (self.name_basis, self.value)

# A chunk of a step within a make target
# e.g. gcc can be one chunk, include directories can be another chunk
class StepChunk(object):
	TYPE_NAME = 0
	TYPE_REF = 1
	def __init__(self, value, name, condense):
		self.value = value
		self.name = name
		self.condense = condense  # Mark to find value in common variables
		self.separator = ''       # Use this separator between values
		self.type = self.TYPE_NAME
	
	def __str__(self):
		return "%s = %s" % (self.name, self.value)
	
	def duplicate(self):
		new_chunk = StepChunk(self.value, self.name, self.condense)
		new_chunk.type = self.type
		new_chunk.separator = self.separator
		return new_chunk
	
	def __eq__(self, other):
		if type(self) != type(other):
			raise T3PluginError("StepChunk comparison between objects of different types")
		else:
			ret = True
			if self.value != other.value:
				ret = False
			if self.name != other.name:
				ret = False
			if self.condense != other.condense:
				ret = False
			if self.separator != other.separator:
				ret = False
			if self.type != other.type:
				ret = False
			return ret

class MakeStep(object):
	def __init__(self):
		self.chunks = []
		
	def duplicate(self):
		new_step = MakeStep()
		for chunk in self.chunks:
			new_step.chunks.append(chunk.duplicate())
		return new_step
	
	def get_text(self, variables):
		step_line = []
		for chunk in self.chunks:
			if chunk.type == chunk.TYPE_REF:
				if variables[chunk.value].value != '':
					chunk_text = "$(%s)" % (variables[chunk.value].name)
					step_line.append(chunk_text + chunk.separator)
			elif chunk.type == chunk.TYPE_NAME:
				chunk_text = chunk.value
				step_line.append(chunk_text + chunk.separator)
			else:
				raise T3PluginError("Unrecognized stepchunk type %s found." % (chunk.type))
		return "".join(step_line)
	
	def set_step_chunks(self, names, values, condense, separators):
		if len(values) == len(names) and len(names) == len(condense) and len(condense) == len(separators):
			self.chunks = []
			for i in range(len(values)):
				chunk = StepChunk(values[i], names[i], condense[i])
				chunk.separator = separators[i]
				self.chunks.append(chunk)
		else:
			raise T3PluginError("Number of step chunks and suggested makefile variable names don't match")
	
	def __eq__(self, other):
		ret = True
		for element1,element2 in zip(self.chunks, other.chunks):
			if element1 != element2:
				ret = False
		return ret
	
	# if a rule contains a "$*" variable, the suffix needs to be changed to 
	# reflect the config specific filename
	def rename_suffix_auto_variable(self, config_string, changed_suffixes):
		for suf in changed_suffixes:
			for chunk in self.chunks:
				if isinstance(chunk.value, str):
					start = '$*' + suf
					renamed = '$*' + '.' + config_string + suf
					chunk.value = chunk.value.replace(start, renamed)

class Rule(object):
	TYPE_INPUTS_TO_OUTPUTS = 1
	TYPE_INPUTS_TO_OUTPUT  = 2
	
	def __init__(self, config, toolchain, name):
		self.toolchain = toolchain
		self.name = name
		self.config = config
		self.generic_rule = False
		self.steps = []
		self.input_suffixes = []
		self.output_suffixes = []
		self.input_files = [] 
		self.output_files = []
		self.prereq_vars = [] # MakeVar variables which hold pre-requisites
		self.rule_type = None  # see the list of constants above
		self.is_archive_rule = False
		self.identifier = None # identifies a configuration uniquely within this Makefile
		self.full_identifier = None # identifies a configuration uniquely (e.g. for making filenames unique across multiple Makefiles)
	
	def duplicate(self):
		new_rule = Rule(self.config, self.toolchain, self.name)
		new_rule.generic_rule = self.generic_rule = False
		new_rule.steps = list(self.steps)
		new_rule.input_suffixes = list(self.input_suffixes)
		new_rule.output_suffixes = list(self.output_suffixes)
		for this_file in self.input_files:
			new_rule.input_files.append(this_file.duplicate())
		for this_file in self.output_files:
			new_rule.output_files.append(this_file.duplicate())
		new_rule.prereq_vars = list(self.prereq_vars)
		new_rule.rule_type = self.rule_type
		new_rule.is_archive_rule = self.is_archive_rule
		new_rule.identifier = self.identifier
		new_rule.full_identifier = self.full_identifier
		return new_rule
	
	def add_step(self, names, values, condense, separators):
		step = MakeStep()
		step.set_step_chunks(names, values, condense, separators)
		self.steps.append(step)
	
	def set_file_types(self):
		archive_extensions = []
		for infile in self.input_files:
			infile.file_type = infile.TYPE_INPUT
		for outfile in self.output_files:
			outfile.file_type = outfile.TYPE_OUTPUT
			if self.is_archive_rule and outfile.suffix not in archive_extensions:
				archive_extensions.append(outfile.suffix)
		return archive_extensions

	def get_text(self, variables):
		step_lines = ''
		for step in self.steps:
			step_lines += "\t%s\n" % (step.get_text(variables))
		
		if self.generic_rule:
			assert (len(self.input_suffixes) == 1 and len(self.output_suffixes) == 1)
			input_suffix = self.input_suffixes[0]
			output_suffix = self.output_suffixes[0]
			first_line = "%%%s: %%%s\n" % (output_suffix, input_suffix)
			rule_text = first_line + step_lines + '\n'
		
		elif self.rule_type == self.TYPE_INPUTS_TO_OUTPUT:
			rule_text = ''
			
			depend_vars = []
			for prereq_var in self.prereq_vars:
				# if archive_rule and DEP_PROJ_ARCHIVE_ in prereq_var.name, don't add
				# the prereq_var in depend file list.
				if not self.is_archive_rule or "DEP_PROJ_ARCHIVE_" not in prereq_var.name:
					depend_vars.append("$(%s)" % prereq_var.name)
			depend_vars = " ".join(depend_vars)
			
			first_line = "%s: %s\n" % (self.output_files[0].get_fname(), depend_vars)
			rule_text += first_line + step_lines + '\n'
		
		elif self.rule_type == self.TYPE_INPUTS_TO_OUTPUTS:
			# need a rule for each output file for anything not covered by generic rules
			rule_text = ''
			for outfile in self.output_files:
				for insuffix in self.input_suffixes:
					first_line = outfile.get_fname() + ': ' + outfile.name + insuffix + '\n'
					rule_text += first_line + step_lines + '\n'
				rule_text += '\n'
		else:
			raise T3PluginError("Undefined rule type specified")
		return rule_text

	def rename_intermediate_files(self):
		# renames intermediate files based on the config 
		changed_input_suffixes = []
		changed_output_suffixes = []
		config_string = self.full_identifier
		
		for infile in self.input_files:
			if infile.file_type == infile.TYPE_INTERMEDIATE:
				if infile.suffix not in changed_input_suffixes:
					self.input_suffixes.remove(infile.suffix)
					self.input_suffixes.append('.' + config_string + infile.suffix)
					changed_input_suffixes.append(infile.suffix)
				infile.suffix = '.' + config_string + infile.suffix 
		
		for outfile in self.output_files:
			if outfile.file_type == outfile.TYPE_INTERMEDIATE:
				if outfile.suffix not in changed_output_suffixes:
					self.output_suffixes.remove(outfile.suffix)
					self.output_suffixes.append('.' + config_string + outfile.suffix)
					changed_output_suffixes.append(outfile.suffix)
				outfile.suffix = '.' + config_string + outfile.suffix
		
		# We need to look for any renaming of suffixes within the rule steps
		changed_suffixes = list(set(changed_input_suffixes + changed_output_suffixes))
		for step in self.steps:
			step.rename_suffix_auto_variable(config_string, changed_suffixes)


class IOFile(object):
	"""File object with prefix and suffix separate and classified as input/output/intermediate"""
	TYPE_INPUT = 1
	TYPE_OUTPUT = 2
	TYPE_INTERMEDIATE = 3
	def __init__(self, fname):
		self.file_type = None
		self.common_file = False
		(self.name, self.suffix) = self._split_fname(fname)

	# split a file name into suffix and prefix
	@staticmethod
	def _split_fname(fname):
		if (fname.split(".") == [fname]):
			name = fname
			suffix = ''
		else:
			name = '.'.join(fname.split(".")[0:-1])
			suffix = "." + fname.split(".")[-1] 
		return (name, suffix)
	
	def __eq__(self,other):
		if type(self) != type(other):
			raise T3PluginError("IOFile comparison between objects of different types")
			return False
		else:
			if self.name == other.name and \
			   self.suffix == other.suffix and \
			   self.file_type == other.file_type:
				return True
			else:
				return False
	
	def duplicate(self):
		new_iofile = IOFile(self.name + self.suffix)
		new_iofile.common_file = self.common_file
		new_iofile.file_type = self.file_type
		return new_iofile
	
	def get_fname(self):
		return self.name + self.suffix


class Makefile(object):
	def __init__(self, makefile_path, project, project_loader):
		self.rules = []
		self.include_extensions = []  # file extensions to 'include' in the makefile
		self.variables = []
		self.makefile_configs = []
		self.sub_makefile_rules = [] # rules for making sub-projects
		self.extra_clean_rules = []
		self.archive_extensions = []
		self.project_loader = project_loader
		self.attributes = None
		self.fquery = None
		self.environment_variables = None
		self.makefile_flags = {}
		self._project = project
		self.project_id = project.get_name()
		self.all_dependencies = [p.get_name() for p in project.get_all_dependencies()]
		
		# We would like the makefile to have a $(BASE) variable which all files are given relative to.
		# Function for converting a path from M-Build into a makefile suitable one
		code_root_makefile, code_root_python = project.find_code_root(makefile_path)
		self.code_root_makefile = code_root_makefile
		fix_path = lambda f: "$(BASE)%s" % f.get_filename()
		self.makefile_path = m2.TransformPath(m2.PosixPath(code_root_python), fix_path)
	
	def io_file(self, fname):
		return IOFile(fname)
	
	def set_attributes(self, manifest, config):
		project_keywords = self._project.get_keywords(config)
		self.attributes = manifest.get_all_attributes(project_keywords, self.makefile_path)
	
	def set_fquery(self, manifest, config):
		project_keywords = self._project.get_keywords(config)
		self.fquery = FileQuery(manifest, self.makefile_path, project_keywords)
	
	# get the names of all end-product targets
	def get_end_targets(self):
		targets = []
		for rule in self.rules:
			if rule.generic_rule == False:
				for outfile in rule.output_files:
					if outfile.file_type == outfile.TYPE_OUTPUT:
						targets.append(outfile.get_fname())
		return targets
	
	# indicate that dependency files need to be included into the makefile
	def include_dependencies(self,extensions):
		for ext in extensions:
			if ext not in self.include_extensions:
				self.include_extensions.append(ext)
	
	def get_files_to_include(self):
		inlcude_files = []
		for rule in self.rules:
			for outfile in rule.output_files:
				if outfile.suffix in self.include_extensions:
					inlcude_files.append(outfile.get_fname())
		return inlcude_files
	
	def get_all_output_files(self):
		files = []
		for rule in self.rules:
			for outfile in rule.output_files:
				fname = outfile.get_fname()
				if fname not in files and outfile.file_type == outfile.TYPE_OUTPUT:
					files.append(fname)  
			for infile in rule.input_files:
				fname = infile.get_fname()
				if fname not in files and infile.file_type == infile.TYPE_OUTPUT:
					files.append(fname)  
		return files
	
	def add_config(self, config):
		if config not in self.makefile_configs:
			self.makefile_configs.append(config)
	
	def add_rule(self, config, toolchain,name):
		make_rule = Rule(config, toolchain,name)
		self.rules.append(make_rule)
		return make_rule
	
	def rule_exists(self, toolchain, name):
		exists = False
		for	rule in self.rules:
			if toolchain == rule.toolchain and name == rule.name:
				exists = True
		return exists
	
	def get_environment_check_text(self):
		text = [""]
		if self.environment_variables:
			for (var_name, var_text) in self.environment_variables.iteritems():
				text.append("\nifndef %s\n$(error \"$${%s} is not defined. %s\")\nendif\n" % \
				            (var_name, var_name, var_text))
		return text
	
	def get_variable_names(self,var_type):
		names = []
		# TODO: should changed to self.sorted_variables
		for variable in self.variables:
			if variable.makevar_type == var_type:
				names.append(variable.name)
		return names
	
	def get_variable_text(self, max_line_length, var_type):
		text = ['']
		for variable in self.sorted_variables:
			if variable.makevar_type == var_type:
				if isinstance(variable.value, list):
					# if not empty list
					if ''.join(variable.value) != '':
						text.extend([variable.name,' =']) 
						# position of new line variables
						new_line_pos = len(variable.name + ' = ')
						line_length = new_line_pos-1
						for val in variable.value:
							if isinstance(val, MakeVar): # TODO: be sure this would never happen and remove
								text.append(variable.separator + val.value)
								line_length += len(text[-1])
							elif isinstance(val, str): # string
								text.append(variable.separator + val)
								line_length += len(text[-1])
							else:
								raise T3PluginError("Invalid variable type in get_variable_text")
							if line_length >= max_line_length and val != variable.value[-1]:
								text.append("\\\n" + " " * (new_line_pos-1))
								line_length = new_line_pos
						text.append('\n') 
				elif isinstance(variable.value, str):
					# if not empty string
					if variable.value != '':
						text.append("%s = %s\n" % (variable.name, variable.value)) 
				else:
					raise T3PluginError("Invalid variable value type in get_variable_text")
		variable_text = ''.join(text)
		return variable_text
	
	def _set_up_files(self):
		# collect list of all 'real' inputs and outputs, as opposed to derived files
		for rule in self.rules:
			archive_extensions = rule.set_file_types()
			self.archive_extensions.extend(archive_extensions)
		self.archive_extensions = list(set(self.archive_extensions))
		
		# get common set of files for all rules
		self.common_filenames = []
		for infile in self.rules[0].input_files:
			self.common_filenames.append(infile.name) 
		for rule in self.rules[1:len(self.rules)]:
			if len(rule.input_files) > 0:
				names = []
				for infile in rule.input_files:
					names.append(infile.name)
				self.common_filenames = list(set(self.common_filenames) & set(names))
		# mark common file of input files of all rules
		for rule in self.rules:
			for infile in rule.input_files:
				if infile.name in self.common_filenames:
					infile.common_file = True
		self.common_filenames.sort()
		
		# set up which rules map files to other rules
		rule_maps = []
		outer_rule_index = -1
		for outer_rule in self.rules:
			outer_rule_index += 1
			inner_rule_index = -1
			for inner_rule in self.rules:
				inner_rule_index += 1
				if inner_rule_index != outer_rule_index:
					for insuf in inner_rule.input_suffixes:
						if insuf in outer_rule.output_suffixes:
							if outer_rule.config == inner_rule.config and \
							   len(outer_rule.config) == len(inner_rule.config):
								rule_maps.append([outer_rule_index, inner_rule_index])
		
		ordered_rule_map = []
		while len(rule_maps):
			# Find the rules which maps to other rules while no rules maps to them.
			outers = set([rule_map[0] for rule_map in rule_maps])
			inners = set([rule_map[1] for rule_map in rule_maps])
			pop_maps = outers - inners
			if pop_maps:
				for pop_map in pop_maps:
					for rule_map in rule_maps:
						if rule_map[0] == pop_map:
							ordered_rule_map.append(rule_map)
							rule_maps.remove(rule_map)
			else:
				raise T3PluginError("There are circles in rule maps.")
		
		for rule_map in ordered_rule_map:
			new_outputs = []
			outer_rule = self.rules[rule_map[0]]
			if len(outer_rule.input_files) > 0 and \
			   len(outer_rule.output_files) == 0 and \
			   len(outer_rule.output_suffixes) > 0:
				for out_suffix in outer_rule.output_suffixes:
					for infile in outer_rule.input_files:
						# change input suffix to output suffix
						outfile = infile.duplicate()
						outfile.suffix = out_suffix
						outfile.file_type = outfile.TYPE_INTERMEDIATE
						outer_rule.output_files.append(outfile)
						new_outputs.append(outfile) 
			
			# map outputs from inner rule to outer rule
			inner_rule = self.rules[rule_map[1]]
			for new_output in new_outputs:
				if new_output.suffix in inner_rule.input_suffixes:
					infile = new_output.duplicate()
					inner_rule.input_files.append(infile)
		
		# This handles the unusual situation where a makefile is only compiling, not linking or archiving
		# If a rule doesn't map to any other rule and has multiple output suffixes, try to guess what is
		# the primary output suffix which only serves to give the rule an output name.
		unmaped_rule_indices = list(set(range(len(self.rules))) - set([rule_map[0] for rule_map in ordered_rule_map]))
		for unmaped_rule_index in sorted(unmaped_rule_indices):
			unmaped_rule = self.rules[unmaped_rule_index]
			if len(unmaped_rule.output_suffixes) > 1:
				primary_suffix = unmaped_rule.output_suffixes[0]
				for outsuf in unmaped_rule.output_suffixes:
					final_suffix = "." + outsuf.split(".")[-1] 
					if final_suffix not in self.include_extensions:
						primary_suffix = outsuf
				unmaped_rule.output_suffixes = [primary_suffix]
				for output_file in unmaped_rule.output_files:
					if output_file.suffix == primary_suffix:
						output_file.file_type = output_file.TYPE_OUTPUT
		
		# remove irrelevant rules, the rule_maps will be invalid.
		removed = []
		for rule in self.rules:
			if rule.rule_type == rule.TYPE_INPUTS_TO_OUTPUTS or \
			   rule.rule_type == rule.TYPE_INPUTS_TO_OUTPUT:
				if len(rule.input_files) == 0:
					removed.append(rule)
		for rule in removed:
			self.rules.remove(rule)
		
		# give config specific names to intermediate files
		for rule in self.rules:
			rule.rename_intermediate_files()
		
		input_suffixes = []
		for rule in self.rules:
			for insuffix in rule.input_suffixes:
				if insuffix not in input_suffixes:
					input_suffixes.append(insuffix)
		
		# Get a list of suffixes which have no corresponding input to another rule, normally they
		# are the side product in build process, like dependency files.
		for rule in self.rules:
			rule._unused_suffixes = []
			for outsuffix in rule.output_suffixes:
				if outsuffix not in input_suffixes:
					final_output_suffix = False
					for ofile in rule.output_files:
						if ofile.file_type == ofile.TYPE_OUTPUT and ofile.suffix == outsuffix:
							final_output_suffix = True
					if final_output_suffix == False:
						rule._unused_suffixes.append(outsuffix)
						rule.output_suffixes.remove(outsuffix)
			# Finally there should be only one output suffix for each rule, thus means 
			# one rule has only one suffix map like (%.o: %.c). If still multiple output 
			# suffixes, throw an error.
			# Notes that one rule can still generate output files with multipy suffixes.
			if len(rule.output_suffixes) != 1:
				raise T3PluginError("Rule with unresolved suffixes found.")
			
			# if INPUTS_TO_OUTPUTS rule has more than one input, separate into several rules
			new_rules = []
			for rule in self.rules:
				if rule.rule_type == rule.TYPE_INPUTS_TO_OUTPUTS:
					suffixes_removed = []
					for insuf in rule.input_suffixes[1:len(rule.input_suffixes)]:
						new_rule = rule.duplicate()
						new_rule.input_suffixes = [insuf]
						suffixes_removed.append(insuf)
						removed_files = []
						for ifile in new_rule.input_files:
							if ifile.suffix != insuf:
								removed_files.append(ifile)
						for rfile in removed_files:
							new_rule.input_files.remove(rfile)
						removed_files = []
						for ifile in rule.input_files:
							if ifile.suffix == insuf:
								removed_files.append(ifile)
						for rfile in removed_files:
							rule.input_files.remove(rfile)
						new_rules.append(new_rule)
					for insuf in suffixes_removed:
						rule.input_suffixes.remove(insuf)
			self.rules.extend(new_rules)
	
	def _find_generic_rules(self):
		# if all files of a single suffix have the same rule 
		# unless the other rules have the same input files and steps
		# at this point each rule has only one output suffix (though there may be output files
		# with other suffixes which are not targets)
		suffix_rules = {}
		for rule in self.rules:
			if rule.rule_type == rule.TYPE_INPUTS_TO_OUTPUTS:
				outsuf = rule.output_suffixes[0] 
				insuf = rule.input_suffixes[0]
				name = outsuf + insuf
				if name not in suffix_rules:
					suffix_rules[name] = Rule(rule.config, rule.toolchain,rule.name)
					suffix_rules[name].identifier = rule.identifier
					for this_file in rule.input_files:
						suffix_rules[name].input_files.append(this_file.duplicate())
					for this_file in rule.output_files:
						suffix_rules[name].output_files.append(this_file.duplicate())
					for this_step in rule.steps:
						suffix_rules[name].steps.append(this_step.duplicate())
					suffix_rules[name].generic_rule = True
					suffix_rules[name].input_suffixes = [insuf]
					suffix_rules[name].output_suffixes = [outsuf]
					suffix_rules[name].rule_type = rule.rule_type
				else: # suffix rule exists
					# if rules for the two identical output suffixes are not the same, not general rule
					if suffix_rules[name].steps != rule.steps:
						suffix_rules[name].generic_rule = False
					else:
						for outfile in rule.output_files:
							if outfile not in suffix_rules[name].output_files:
								suffix_rules[name].output_files.append(outfile.duplicate())
						for infile in rule.input_files:
							if infile not in suffix_rules[outsuf].input_files:
								suffix_rules[outsuf].input_files.append(infile.duplicate())

		# remove suffix rules which turned out not to be general enough
		remove_rules = []
		for rule in suffix_rules:
			if suffix_rules[rule].generic_rule == False:
				remove_rules.append(rule)
		for rule in remove_rules:
			del suffix_rules[rule]
		
		# remove files from rules covered by generic rules 
		# and remove redundant rules
		remove_rules = []
		for srule in sorted(suffix_rules.keys()):
			for rule in self.rules:
				if suffix_rules[srule].output_suffixes[0] in rule.output_suffixes:
					file_removed = False
					removed_files = []
					for infile in rule.input_files:
						if infile.suffix == suffix_rules[srule].input_suffixes[0]:
							removed_files.append(infile)
							file_removed = True
					for rfile in removed_files:
						rule.input_files.remove(rfile)
					removed_files = []
					for outfile in rule.output_files:
						if outfile.suffix == suffix_rules[srule].output_suffixes[0]:
							removed_files.append(outfile)
							file_removed = True
					for rfile in removed_files:
						rule.output_files.remove(rfile)
					if (rule.input_files == []) and file_removed and \
					  rule.rule_type == rule.TYPE_INPUTS_TO_OUTPUTS:
						remove_rules.append(rule)
		
		for rule in remove_rules:
			if len(rule.output_files) > 0:
				self.extra_clean_rules.append(rule)
			self.rules.remove(rule)
		
		for srule in sorted(suffix_rules.keys()):
			self.rules.append(suffix_rules[srule])
	
	def _get_config_str(self, config, dimensions):
		config_str = ''
		num_dim = len(dimensions)
		if num_dim <= 0:
			return ''
		else:
			for dim in dimensions[0:num_dim-1]:
				config_str += config[dim] + '_' 
			config_str += config[dimensions[-1]]
			return config_str

	def _create_environment_variables(self, environment_vars):
		if environment_vars:
			for (var_name, var_text) in environment_vars.iteritems():
				var = MakeVar(var_text, var_name, None, "")
				var.makevar_type = var.ENVIRONMENT_VAR
				var.identifier = ""
				self.environment_variables.append(var)

	def _create_step_variables(self):
		for rule in self.rules:
			for step in rule.steps:
				for step_chunk in step.chunks:
					step_chunk.identifier = rule.identifier
		
		# construct list of rule-oriented variables to be sent to the makefile
		i = 0               # condensed variable index
		for rule in self.rules:
			for step in rule.steps:
				for step_chunk in step.chunks:
					if step_chunk.type != step_chunk.TYPE_REF and step_chunk.condense == True:
						var = MakeVar(step_chunk.value,step_chunk.name,rule,step_chunk.separator)
						var.identifier = rule.identifier
						var.makevar_type = var.RULE_VAR
						step_chunk.type = step_chunk.TYPE_REF
						step_chunk.value = i
						self.variables.append(var)
						# look for duplicates
						for inner_rule in self.rules:
							for inner_step in inner_rule.steps:
								for inner_step_chunk in inner_step.chunks:
									if inner_step_chunk.type != inner_step_chunk.TYPE_REF and \
									var.name_basis == inner_step_chunk.name and \
									var.value == inner_step_chunk.value and \
									var.separator == inner_step_chunk.separator and \
									var.identifier == inner_step_chunk.identifier and \
									inner_step_chunk.condense:
										inner_step_chunk.type = inner_step_chunk.TYPE_REF
										inner_step_chunk.value = i
										# need to know all configs a variable is valid for
										# avoid duplication
										duplicate = False
										for config in var.var_configs:
											if inner_rule.config == config:
												duplicate = True
										if duplicate == False:
											var.var_configs.append(inner_rule.config)
						i += 1
	
	def _create_file_variables(self):
		# Set up makefile variables for files. If the file is in every rule 
		# create a common variable, otherwise create a rule specific variable
		
		for rule in self.rules:
			var = None
			com_var = None
			if rule.generic_rule == False:
				for infile in rule.input_files:
					if infile.name not in self.common_filenames:
						if var is None:
							var = MakeVar([],'INPUTS_'+rule.name,rule,' ')
							var.identifier = rule.identifier
							var.makevar_type = var.INTERMEDIATE_OBJECT
						var.value.append(infile.get_fname())
					elif com_var is None:
						com_var = MakeVar([],'INPUTS_COMMON_'+rule.name,rule,' ')
						com_var.identifier = rule.identifier
						com_var.value = '$(addsuffix '
						com_var.value += infile.suffix
						com_var.value += ',$(COMMON_FILES))'
						com_var.makevar_type = com_var.INTERMEDIATE_OBJECT
						self.variables.append(com_var)
						rule.prereq_vars.append(com_var)
				
				if not var is None:
					# pointers set up
					self.variables.append(var)
					rule.prereq_vars.append(var)

				# get dependent project files
				dependent_project_prereqs = self.depend_names(rule.config)
				if dependent_project_prereqs:
					var = MakeVar([],'DEP_PROJ_'+rule.name,rule,' ')
					var.identifier = rule.identifier
					var.makevar_type = var.DEPENDENT_PROJECT_OUTPUT
					var.value = dependent_project_prereqs
					self.variables.append(var)
					rule.prereq_vars.append(var)
		
		for var in self.variables:
			var.name = self._construct_variable_name(var.name_basis,var.identifier)
		
		
		# set up variables for cleaning files not included in other rules
		# e.g. dependency files
		cleaning_variables = []
		
		for rule in self.extra_clean_rules:
			for outfile in rule.output_files:
				if outfile.name in self.common_filenames:
					clean_var_name = self._construct_variable_name('CLEAN_COMMON_'+rule.name,rule.identifier)
					var_exists = False
					for testvar in cleaning_variables:
						if testvar.name == clean_var_name:
							var_exists = True
					if var_exists == False:
						com_var = MakeVar([],'CLEAN_COMMON_'+rule.name,rule,' ')
						com_var.identifier = rule.identifier
						com_var.value = '$(addsuffix '
						com_var.value += outfile.suffix
						com_var.value += ',$(COMMON_FILES))'
						com_var.name = self._construct_variable_name('CLEAN_COMMON_'+rule.name,rule.identifier)
						com_var.makevar_type = com_var.SIDE_PRODUCT
						cleaning_variables.append(com_var)
				else:		
					clean_var_name = self._construct_variable_name('CLEAN_'+rule.name,rule.identifier)
					var_exists = False
					for testvar in cleaning_variables:
						if testvar.name == clean_var_name:
							var_exists = True
							testvar.value.append(outfile.get_fname())
					if var_exists == False:
						var = MakeVar([],'CLEAN_'+rule.name,rule,' ')
						var.identifier = rule.identifier
						var.makevar_type = var.SIDE_PRODUCT
						var.name = self._construct_variable_name('CLEAN_'+rule.name,rule.identifier)
						var.value.append(outfile.get_fname())
						cleaning_variables.append(var)
						
		self.variables.extend(cleaning_variables)
		
		# set up makefile variable for common files
		if len(self.rules) > 0:
			var = MakeVar([], 'COMMON_FILES', self.rules[0], ' ')
			var.makevar_type = var.COMMON_FILE_VAR
			var.name = 'COMMON_FILES'
			if self.common_filenames:
				for name in self.common_filenames:
					var.value.append(name)
				self.variables.append(var) # make sure common files is first
		
		self.sorted_variables = sorted(self.variables, key=lambda mvar: mvar.name)
	
	def depend_names(self, configuration):
		names = []
		for proj in self.all_dependencies:
			project = self.project_loader.get_project(proj)
			pname = project.get_name()
			if 'use' in project.get_actions() and pname != self.project_id:
				project_relative_filename = os.path.join(*project.get_output_name('use', configuration))
				project_dir = os.path.dirname(project.get_project_filename())
				makefile_relative_filename = self.makefile_path.write_path(os.path.join(project_dir, project_relative_filename))
				names.append(makefile_relative_filename)

		# Remove duplicate names, but keep the last mention, not the first.
		unique_names = []
		for n in names:
			unique_names = [u for u in unique_names if not u == n] + [n]
		return ' '.join(unique_names)
	
	def get_sub_library_info(self):
		# sub-makefile rules
		all_exts = []
		all_clean = []
		for rule in self.rules:
			if rule.generic_rule == False:
				(clean_lines,out_exts) = self.depend_rules(rule.config)
				all_exts.extend(out_exts)
				all_clean.extend(clean_lines)
		all_exts = sorted(set(all_exts)) # remove duplicates
		all_clean = sorted(set(all_clean)) # remove duplicates
		return (all_clean, all_exts)
	
	def depend_rules(self, configuration):
		clean_lines = []
		extensions = []
		for proj in self.all_dependencies:
			project = self.project_loader.get_project(proj)
			if 'use' in project.get_actions() and project.get_name() != self.project_id:
				project_name = project.get_output_name('use', configuration)
				project_relative_filename = os.path.join(*project_name)
				project_dir = os.path.dirname(project.get_project_filename())
			
				makefile_relative_filename = self.makefile_path.write_path(os.path.join(project_dir, project_relative_filename))
				makefile_relative_directory = self.makefile_path.write_path(os.path.join(project_dir, os.path.dirname(project_relative_filename)))
			
				var_name = 'BUILD_%s_%s' % (project.get_name(), project.get_identifier(configuration, []))
				if not var_name in self.makefile_flags:
					self.makefile_flags[var_name] = True
					ext = "." + makefile_relative_filename.split(".")[-1]
					extensions.append(ext)
					clean_lines.append('$(MAKE) -C %s cleanself\n' % (makefile_relative_directory))
		return (clean_lines,extensions)
	
	
	def _construct_variable_name(self,basis,identifier):
		name = [x.upper() for x in [basis]][0]
		name += '_' + identifier
		return name
	
	def condense(self):
		self._set_up_files()
		self._find_generic_rules()
		self._create_step_variables()
		self._create_file_variables()
		return 

	def get_all_rules_text(self):
		text = ''
		for rule in self.rules:
			text += rule.get_text(self.variables)
		return text

	def get_single_rule_text(self, rule_name):
		rule_text = None
		for rule in self.rules:
			if rule.name == rule_name:
				if rule_text == None:
					rule_text = rule.get_text(self.variables)
				else:
					raise T3PluginError("Multiple rules with identical names exist")
		
		if rule_text == None:
			raise T3PluginError("Named rule does not exist")
		else:
			return rule_text


class FileQuery(object):
	def __init__(self,  manifest, path_type, keywords):
		self._path_type = path_type
		self._keywords = list(keywords)
		self._manifest = manifest
		self._cache = {}
	
	def get_file_pattern(self, pattern):
		if not pattern in self._cache:
			self._cache[pattern] = self._manifest.find_file_pattern(self._keywords, self._path_type, pattern)
		return self._cache[pattern]
