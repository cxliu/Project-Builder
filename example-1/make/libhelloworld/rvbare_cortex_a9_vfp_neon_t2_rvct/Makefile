#-*-makefile-*-

BASE=../../../../
ARFLAGS_arm_simulate = -rc
ARFLAGS_debug = -rc
ARFLAGS_release = -rc
AR_arm_simulate = armar
AR_debug = armar
AR_release = armar
CCDEP_arm_simulate = armcc
CCDEP_debug = armcc
CCDEP_release = armcc
CC_arm_simulate = armcc
CC_debug = armcc
CC_release = armcc
CFLAGS_arm_simulate = --cpu=Cortex-A9 --fpu=VFPv3 --thumb -g -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_debug = --cpu=Cortex-A9 --fpu=VFPv3 --thumb -g -O0 --apcs=/interwork -c --c99
CFLAGS_release = --cpu=Cortex-A9 --fpu=VFPv3 --thumb -O3 -Otime --apcs=/interwork -c --c99
DEFINES_arm_simulate = -DNDEBUG=1
DEFINES_release = -DNDEBUG=1
INCLUDES_arm_simulate = -I$(BASE)example-1/include
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_arm_simulate = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_arm_simulate.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_release.o,$(COMMON_FILES))


default: libhelloworld_arm_simulate.lib libhelloworld_debug.lib libhelloworld_release.lib

libhelloworld_arm_simulate.lib: $(INPUTS_COMMON_ARCHIVE_arm_simulate)
	$(AR_arm_simulate) $(ARFLAGS_arm_simulate)   $@ $^

libhelloworld_debug.lib: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)   $@ $^

libhelloworld_release.lib: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)   $@ $^

%.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_arm_simulate.o: %.c
	$(CCDEP_arm_simulate) --cpu=Cortex-A9 --mm $(DEFINES_arm_simulate) $(INCLUDES_arm_simulate) -o $@ > $*.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_arm_simulate.d $<
	$(CC_arm_simulate) $(CFLAGS_arm_simulate) $(DEFINES_arm_simulate) $(INCLUDES_arm_simulate) -o $@ $<

%.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_debug.o: %.c
	$(CCDEP_debug) --cpu=Cortex-A9 --mm $(INCLUDES_debug) -o $@ > $*.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_release.o: %.c
	$(CCDEP_release) --cpu=Cortex-A9 --mm $(DEFINES_release) $(INCLUDES_release) -o $@ > $*.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_arm_simulate = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_arm_simulate.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_arm_simulate)
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_arm_simulate)
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_ARCHIVE_arm_simulate)
	$(RM) $(INPUTS_COMMON_ARCHIVE_debug)
	$(RM) $(INPUTS_COMMON_ARCHIVE_release)
	$(RM) libhelloworld_arm_simulate.lib
	$(RM) libhelloworld_debug.lib
	$(RM) libhelloworld_release.lib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libhelloworld_arm_simulate.lib"
	@echo " libhelloworld_debug.lib"
	@echo " libhelloworld_release.lib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_arm_simulate.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_rvbare_cortex_a9_vfp_neon_t2_rvct_release.d)


