#-*-makefile-*-

BASE=../../../../

ifndef TI_LINK_COMMAND_FILE
$(error "$${TI_LINK_COMMAND_FILE} is not defined. The file is used to pass options, arguments and memory layout of your target platform to linker.")
endif
CC_debug = c6runapp-cc
CC_release = c6runapp-cc
CC_ti_simulate = c6runapp-cc
CFLAGS_debug = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 -g --preproc_with_compile
CFLAGS_release = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 -O3 -pm -mf --preproc_with_compile
CFLAGS_ti_simulate = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 --optimize_with_debug -g -O3 -pm -mf --preproc_with_compile
DEFINES_release = -DNDEBUG=1
DEFINES_ti_simulate = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_release = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_ti_simulate = -I$(BASE)example-1/include -I$(BASE).
LDFLAGS_debug = $(TI_LINK_COMMAND_FILE)
LDFLAGS_release = $(TI_LINK_COMMAND_FILE)
LDFLAGS_ti_simulate = $(TI_LINK_COMMAND_FILE)
LD_debug = c6runapp-cc
LD_release = c6runapp-cc
LD_ti_simulate = c6runapp-cc

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_ti_simulate = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.o,$(COMMON_FILES))


default: helloworld_as_one_project_debug.axf helloworld_as_one_project_release.axf helloworld_as_one_project_ti_simulate.axf

helloworld_as_one_project_debug.axf: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $^  

helloworld_as_one_project_release.axf: $(INPUTS_COMMON_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $^  

helloworld_as_one_project_ti_simulate.axf: $(INPUTS_COMMON_LINK_ti_simulate)
	$(LD_ti_simulate) $(LDFLAGS_ti_simulate) -o $@ $^  

%.helloworld_as_one_project_tisim_eabi_c66_c6run_debug.o: %.c
	$(CC_debug) $(CFLAGS_debug) --preproc_dependency=$*.helloworld_as_one_project_tisim_eabi_c66_c6run_debug.d $(INCLUDES_debug) -o$@ $<

%.helloworld_as_one_project_tisim_eabi_c66_c6run_release.o: %.c
	$(CC_release) $(CFLAGS_release) --preproc_dependency=$*.helloworld_as_one_project_tisim_eabi_c66_c6run_release.d $(DEFINES_release) $(INCLUDES_release) -o$@ $<

%.helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.o: %.c
	$(CC_ti_simulate) $(CFLAGS_ti_simulate) --preproc_dependency=$*.helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.d $(DEFINES_ti_simulate) $(INCLUDES_ti_simulate) -o$@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_ti_simulate = $(addsuffix .helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) $(INPUTS_COMMON_LINK_ti_simulate)
	$(RM) helloworld_as_one_project_debug.axf
	$(RM) helloworld_as_one_project_release.axf
	$(RM) helloworld_as_one_project_ti_simulate.axf

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_as_one_project_debug.axf"
	@echo " helloworld_as_one_project_release.axf"
	@echo " helloworld_as_one_project_ti_simulate.axf"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_eabi_c66_c6run_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_eabi_c66_c6run_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_eabi_c66_c6run_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_eabi_c66_c6run_release.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_eabi_c66_c6run_ti_simulate.d)


