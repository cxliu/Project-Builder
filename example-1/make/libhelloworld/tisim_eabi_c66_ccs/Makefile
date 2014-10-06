#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -ru
ARFLAGS_release = -ru
ARFLAGS_ti_simulate = -ru
AR_debug = ar6x
AR_release = ar6x
AR_ti_simulate = ar6x
CC_debug = cl6x
CC_release = cl6x
CC_ti_simulate = cl6x
CFLAGS_debug = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 -g --preproc_with_compile
CFLAGS_release = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 -O3 -pm -mf --preproc_with_compile
CFLAGS_ti_simulate = -c --gcc -on2 -pden -pdv --abi=eabi --strip_coff_underscore -mv6600 --optimize_with_debug -g -O3 -pm -mf --preproc_with_compile
DEFINES_release = -DNDEBUG=1
DEFINES_ti_simulate = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include
INCLUDES_ti_simulate = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_release.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_ti_simulate = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_ti_simulate.o,$(COMMON_FILES))


default: libhelloworld_debug.lib libhelloworld_release.lib libhelloworld_ti_simulate.lib

libhelloworld_debug.lib: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)   $@ $^

libhelloworld_release.lib: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)   $@ $^

libhelloworld_ti_simulate.lib: $(INPUTS_COMMON_ARCHIVE_ti_simulate)
	$(AR_ti_simulate) $(ARFLAGS_ti_simulate)   $@ $^

%.libhelloworld_tisim_eabi_c66_ccs_debug.o: %.c
	$(CC_debug) $(CFLAGS_debug) --preproc_dependency=$*.libhelloworld_tisim_eabi_c66_ccs_debug.d $(INCLUDES_debug) --output_file=$@ $<

%.libhelloworld_tisim_eabi_c66_ccs_release.o: %.c
	$(CC_release) $(CFLAGS_release) --preproc_dependency=$*.libhelloworld_tisim_eabi_c66_ccs_release.d $(DEFINES_release) $(INCLUDES_release) --output_file=$@ $<

%.libhelloworld_tisim_eabi_c66_ccs_ti_simulate.o: %.c
	$(CC_ti_simulate) $(CFLAGS_ti_simulate) --preproc_dependency=$*.libhelloworld_tisim_eabi_c66_ccs_ti_simulate.d $(DEFINES_ti_simulate) $(INCLUDES_ti_simulate) --output_file=$@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_ti_simulate = $(addsuffix .libhelloworld_tisim_eabi_c66_ccs_ti_simulate.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(CLEAN_COMMON_COMPILE_ti_simulate)
	$(RM) $(INPUTS_COMMON_ARCHIVE_debug)
	$(RM) $(INPUTS_COMMON_ARCHIVE_release)
	$(RM) $(INPUTS_COMMON_ARCHIVE_ti_simulate)
	$(RM) libhelloworld_debug.lib
	$(RM) libhelloworld_release.lib
	$(RM) libhelloworld_ti_simulate.lib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libhelloworld_debug.lib"
	@echo " libhelloworld_release.lib"
	@echo " libhelloworld_ti_simulate.lib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_tisim_eabi_c66_ccs_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_tisim_eabi_c66_ccs_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_tisim_eabi_c66_ccs_ti_simulate.d)


