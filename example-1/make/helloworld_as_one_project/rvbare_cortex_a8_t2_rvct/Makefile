#-*-makefile-*-

BASE=../../../../
CCDEP_arm_simulate = armcc
CCDEP_debug = armcc
CCDEP_release = armcc
CC_arm_simulate = armcc
CC_debug = armcc
CC_release = armcc
CFLAGS_arm_simulate = --cpu=Cortex-A8.no_neon --fpu=VFPv3_D16 --thumb -g -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_debug = --cpu=Cortex-A8.no_neon --fpu=VFPv3_D16 --thumb -g -O0 --apcs=/interwork -c --c99
CFLAGS_release = --cpu=Cortex-A8.no_neon --fpu=VFPv3_D16 --thumb -O3 -Otime --apcs=/interwork -c --c99
DEFINES_arm_simulate = -DNDEBUG=1
DEFINES_release = -DNDEBUG=1
INCLUDES_arm_simulate = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_debug = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_release = -I$(BASE)example-1/include -I$(BASE).
LDFLAGS_arm_simulate = -L--cpu=Cortex-A8.no_neon -L--fpu=VFPv3_D16 -L--bestdebug
LDFLAGS_debug = -L--cpu=Cortex-A8.no_neon -L--fpu=VFPv3_D16
LDFLAGS_release = -L--cpu=Cortex-A8.no_neon -L--fpu=VFPv3_D16
LD_arm_simulate = armcc
LD_debug = armcc
LD_release = armcc

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_arm_simulate = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.o,$(COMMON_FILES))


default: helloworld_as_one_project_arm_simulate.axf helloworld_as_one_project_debug.axf helloworld_as_one_project_release.axf

helloworld_as_one_project_arm_simulate.axf: $(INPUTS_COMMON_LINK_arm_simulate)
	$(LD_arm_simulate) $(LDFLAGS_arm_simulate) -o $@ $+ 

helloworld_as_one_project_debug.axf: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $+ 

helloworld_as_one_project_release.axf: $(INPUTS_COMMON_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $+ 

%.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.o: %.c
	$(CCDEP_arm_simulate) --cpu=Cortex-A8.no_neon --mm $(DEFINES_arm_simulate) $(INCLUDES_arm_simulate) -o $@ > $*.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.d $<
	$(CC_arm_simulate) $(CFLAGS_arm_simulate) $(DEFINES_arm_simulate) $(INCLUDES_arm_simulate) -o $@ $<

%.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.o: %.c
	$(CCDEP_debug) --cpu=Cortex-A8.no_neon --mm $(INCLUDES_debug) -o $@ > $*.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.o: %.c
	$(CCDEP_release) --cpu=Cortex-A8.no_neon --mm $(DEFINES_release) $(INCLUDES_release) -o $@ > $*.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_arm_simulate = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_arm_simulate)
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_arm_simulate)
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_arm_simulate)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_as_one_project_arm_simulate.axf
	$(RM) helloworld_as_one_project_debug.axf
	$(RM) helloworld_as_one_project_release.axf

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_as_one_project_arm_simulate.axf"
	@echo " helloworld_as_one_project_debug.axf"
	@echo " helloworld_as_one_project_release.axf"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_arm_simulate.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_rvbare_cortex_a8_t2_rvct_release.d)


