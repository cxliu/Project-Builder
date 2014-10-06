#-*-makefile-*-

BASE=../../../../

ifndef TI_LINK_COMMAND_FILE
$(error "$${TI_LINK_COMMAND_FILE} is not defined. The file is used to pass options, arguments and memory layout of your target platform to linker.")
endif
CC_debug = cl6x
CC_release = cl6x
CC_ti_simulate = cl6x
CFLAGS_debug = -c --gcc -on2 -pden -pdv --abi=coffabi -mv6600 -g --preproc_with_compile
CFLAGS_release = -c --gcc -on2 -pden -pdv --abi=coffabi -mv6600 -O3 -pm -mf --preproc_with_compile
CFLAGS_ti_simulate = -c --gcc -on2 -pden -pdv --abi=coffabi -mv6600 --optimize_with_debug -g -O3 -pm -mf --preproc_with_compile
DEFINES_release = -DNDEBUG=1
DEFINES_ti_simulate = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_release = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_ti_simulate = -I$(BASE)example-1/include -I$(BASE).
LDFLAGS_debug = $(TI_LINK_COMMAND_FILE)
LDFLAGS_release = $(TI_LINK_COMMAND_FILE)
LDFLAGS_ti_simulate = $(TI_LINK_COMMAND_FILE)
LDLIBS_debug = -lrts6600_coff.lib
LDLIBS_release = -lrts6600_coff.lib
LDLIBS_ti_simulate = -lrts6600_coff.lib
LD_debug = lnk6x
LD_release = lnk6x
LD_ti_simulate = lnk6x

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_ti_simulate = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.o,$(COMMON_FILES))


default: helloworld_as_one_project_debug.out helloworld_as_one_project_release.out helloworld_as_one_project_ti_simulate.out

helloworld_as_one_project_debug.out: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $^  $(LDLIBS_debug)

helloworld_as_one_project_release.out: $(INPUTS_COMMON_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $^  $(LDLIBS_release)

helloworld_as_one_project_ti_simulate.out: $(INPUTS_COMMON_LINK_ti_simulate)
	$(LD_ti_simulate) $(LDFLAGS_ti_simulate) -o $@ $^  $(LDLIBS_ti_simulate)

%.helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.o: %.c
	$(CC_debug) $(CFLAGS_debug) --preproc_dependency=$*.helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.d $(INCLUDES_debug) --output_file=$@ $<

%.helloworld_as_one_project_tisim_coffabi_c66_ccs_release.o: %.c
	$(CC_release) $(CFLAGS_release) --preproc_dependency=$*.helloworld_as_one_project_tisim_coffabi_c66_ccs_release.d $(DEFINES_release) $(INCLUDES_release) --output_file=$@ $<

%.helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.o: %.c
	$(CC_ti_simulate) $(CFLAGS_ti_simulate) --preproc_dependency=$*.helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.d $(DEFINES_ti_simulate) $(INCLUDES_ti_simulate) --output_file=$@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_ti_simulate = $(addsuffix .helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.d,$(COMMON_FILES))

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
	$(RM) helloworld_as_one_project_debug.out
	$(RM) helloworld_as_one_project_release.out
	$(RM) helloworld_as_one_project_ti_simulate.out

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_as_one_project_debug.out"
	@echo " helloworld_as_one_project_release.out"
	@echo " helloworld_as_one_project_ti_simulate.out"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_coffabi_c66_ccs_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_coffabi_c66_ccs_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_coffabi_c66_ccs_release.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_tisim_coffabi_c66_ccs_ti_simulate.d)


