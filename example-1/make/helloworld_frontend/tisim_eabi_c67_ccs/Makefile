#-*-makefile-*-

BASE=../../../../

ifndef TI_LINK_COMMAND_FILE
$(error "$${TI_LINK_COMMAND_FILE} is not defined. The file is used to pass options, arguments and memory layout of your target platform to linker.")
endif
CC_debug = cl6x
CC_release = cl6x
CC_ti_simulate = cl6x
CFLAGS_debug = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6700 -g --preproc_with_compile
CFLAGS_release = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6700 -O3 -pm -mf --preproc_with_compile
CFLAGS_ti_simulate = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6700 --optimize_with_debug -g -O3 -pm -mf --preproc_with_compile
DEFINES_release = -DNDEBUG=1
DEFINES_ti_simulate = -DNDEBUG=1
INCLUDES_debug = -I$(BASE).
INCLUDES_release = -I$(BASE).
INCLUDES_ti_simulate = -I$(BASE).
LDFLAGS_debug = $(TI_LINK_COMMAND_FILE)
LDFLAGS_release = $(TI_LINK_COMMAND_FILE)
LDFLAGS_ti_simulate = $(TI_LINK_COMMAND_FILE)
LD_debug = lnk6x
LD_release = lnk6x
LD_ti_simulate = lnk6x

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_ti_simulate = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_ti_simulate.o,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/tisim_eabi_c67_ccs/libhelloworld_debug.lib
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/tisim_eabi_c67_ccs/libhelloworld_release.lib
DEP_PROJ_LINK_ti_simulate = $(BASE)example-1/make/libhelloworld/tisim_eabi_c67_ccs/libhelloworld_ti_simulate.lib

default: helloworld_frontend_debug.out helloworld_frontend_release.out helloworld_frontend_ti_simulate.out

helloworld_frontend_debug.out: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $^  

helloworld_frontend_release.out: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $^  

helloworld_frontend_ti_simulate.out: $(INPUTS_COMMON_LINK_ti_simulate) $(DEP_PROJ_LINK_ti_simulate)
	$(LD_ti_simulate) $(LDFLAGS_ti_simulate) -o $@ $^  

%.helloworld_frontend_tisim_eabi_c67_ccs_debug.o: %.c
	$(CC_debug) $(CFLAGS_debug) --preproc_dependency=$*.helloworld_frontend_tisim_eabi_c67_ccs_debug.d $(INCLUDES_debug) --output_file=$@ $<

%.helloworld_frontend_tisim_eabi_c67_ccs_release.o: %.c
	$(CC_release) $(CFLAGS_release) --preproc_dependency=$*.helloworld_frontend_tisim_eabi_c67_ccs_release.d $(DEFINES_release) $(INCLUDES_release) --output_file=$@ $<

%.helloworld_frontend_tisim_eabi_c67_ccs_ti_simulate.o: %.c
	$(CC_ti_simulate) $(CFLAGS_ti_simulate) --preproc_dependency=$*.helloworld_frontend_tisim_eabi_c67_ccs_ti_simulate.d $(DEFINES_ti_simulate) $(INCLUDES_ti_simulate) --output_file=$@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_ti_simulate = $(addsuffix .helloworld_frontend_tisim_eabi_c67_ccs_ti_simulate.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)

clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/tisim_eabi_c67_ccs cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) $(INPUTS_COMMON_LINK_ti_simulate)
	$(RM) helloworld_frontend_debug.out
	$(RM) helloworld_frontend_release.out
	$(RM) helloworld_frontend_ti_simulate.out

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_frontend_debug.out"
	@echo " helloworld_frontend_release.out"
	@echo " helloworld_frontend_ti_simulate.out"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_tisim_eabi_c67_ccs_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_tisim_eabi_c67_ccs_release.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_tisim_eabi_c67_ccs_ti_simulate.d)

%.lib: FORCE
	$(MAKE) -C $(@D) $(@F)


