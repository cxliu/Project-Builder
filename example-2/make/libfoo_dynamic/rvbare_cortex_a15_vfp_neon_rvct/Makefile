#-*-makefile-*-

BASE=../../../../
CCDEP_add1_arm_simulate = armcc
CCDEP_add1_debug = armcc
CCDEP_add1_release = armcc
CCDEP_add2_arm_simulate = armcc
CCDEP_add2_debug = armcc
CCDEP_add2_release = armcc
CC_add1_arm_simulate = armcc
CC_add1_debug = armcc
CC_add1_release = armcc
CC_add2_arm_simulate = armcc
CC_add2_debug = armcc
CC_add2_release = armcc
CFLAGS_add1_arm_simulate = --cpu=Cortex-A15 --fpu=VFPv4 -g -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_add1_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_add1_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_add2_arm_simulate = --cpu=Cortex-A15 --fpu=VFPv4 -g -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_add2_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_add2_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
CXXFLAGS_add1_arm_simulate = --cpu=Cortex-A15 --fpu=VFPv4 -g -O3 -Otime --apcs=/interwork -c
CXXFLAGS_add1_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c
CXXFLAGS_add1_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c
CXXFLAGS_add2_arm_simulate = --cpu=Cortex-A15 --fpu=VFPv4 -g -O3 -Otime --apcs=/interwork -c
CXXFLAGS_add2_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c
CXXFLAGS_add2_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c
CXX_add1_arm_simulate = armcc
CXX_add1_debug = armcc
CXX_add1_release = armcc
CXX_add2_arm_simulate = armcc
CXX_add2_debug = armcc
CXX_add2_release = armcc
DEFINES_add1_arm_simulate = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add1_debug = -DADD_THIS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add2_arm_simulate = -DADD_THIS=2 -DNDEBUG=1
DEFINES_add2_debug = -DADD_THIS=2
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1
INCLUDES_add1_arm_simulate = -I$(BASE).
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_arm_simulate = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).
LDFLAGS_add1_arm_simulate = -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--bestdebug
LDFLAGS_add1_debug = -L--cpu=Cortex-A15 -L--fpu=VFPv4
LDFLAGS_add1_release = -L--cpu=Cortex-A15 -L--fpu=VFPv4
LDFLAGS_add2_arm_simulate = -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--bestdebug
LDFLAGS_add2_debug = -L--cpu=Cortex-A15 -L--fpu=VFPv4
LDFLAGS_add2_release = -L--cpu=Cortex-A15 -L--fpu=VFPv4
LD_add1_arm_simulate = armcc
LD_add1_debug = armcc
LD_add1_release = armcc
LD_add2_arm_simulate = armcc
LD_add2_debug = armcc
LD_add2_release = armcc


INPUTS_LINK_add1_arm_simulate = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.o\
                                $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.o\
                                $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.o
INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.o
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.o
INPUTS_LINK_add2_arm_simulate = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.o\
                                $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.o\
                                $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.o
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.o
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.o


default: libfoo_dynamic_add1_arm_simulate.so libfoo_dynamic_add2_arm_simulate.so libfoo_dynamic_add1_debug.so libfoo_dynamic_add2_debug.so libfoo_dynamic_add1_release.so libfoo_dynamic_add2_release.so

libfoo_dynamic_add1_arm_simulate.so: $(INPUTS_LINK_add1_arm_simulate)
	$(LD_add1_arm_simulate) $(LDFLAGS_add1_arm_simulate) -o $@ $+ 

libfoo_dynamic_add2_arm_simulate.so: $(INPUTS_LINK_add2_arm_simulate)
	$(LD_add2_arm_simulate) $(LDFLAGS_add2_arm_simulate) -o $@ $+ 

libfoo_dynamic_add1_debug.so: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) -o $@ $+ 

libfoo_dynamic_add2_debug.so: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) -o $@ $+ 

libfoo_dynamic_add1_release.so: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) -o $@ $+ 

libfoo_dynamic_add2_release.so: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) -o $@ $+ 

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.o: %.c
	$(CCDEP_add1_arm_simulate) --cpu=Cortex-A15 --mm $(DEFINES_add1_arm_simulate) $(INCLUDES_add1_arm_simulate) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d $<
	$(CC_add1_arm_simulate) $(CFLAGS_add1_arm_simulate) $(DEFINES_add1_arm_simulate) $(INCLUDES_add1_arm_simulate) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.o: %.cpp
	$(CCDEP_add1_arm_simulate) --cpu=Cortex-A15 --mm $(DEFINES_add1_arm_simulate) $(INCLUDES_add1_arm_simulate) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d $<
	$(CXX_add1_arm_simulate) $(CXXFLAGS_add1_arm_simulate) $(DEFINES_add1_arm_simulate) $(INCLUDES_add1_arm_simulate) -o  $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.o: %.c
	$(CCDEP_add1_debug) --cpu=Cortex-A15 --mm $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) --cpu=Cortex-A15 --mm $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.o: %.c
	$(CCDEP_add1_release) --cpu=Cortex-A15 --mm $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.o: %.cpp
	$(CCDEP_add1_release) --cpu=Cortex-A15 --mm $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.o: %.c
	$(CCDEP_add2_arm_simulate) --cpu=Cortex-A15 --mm $(DEFINES_add2_arm_simulate) $(INCLUDES_add2_arm_simulate) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d $<
	$(CC_add2_arm_simulate) $(CFLAGS_add2_arm_simulate) $(DEFINES_add2_arm_simulate) $(INCLUDES_add2_arm_simulate) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.o: %.cpp
	$(CCDEP_add2_arm_simulate) --cpu=Cortex-A15 --mm $(DEFINES_add2_arm_simulate) $(INCLUDES_add2_arm_simulate) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d $<
	$(CXX_add2_arm_simulate) $(CXXFLAGS_add2_arm_simulate) $(DEFINES_add2_arm_simulate) $(INCLUDES_add2_arm_simulate) -o  $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.o: %.c
	$(CCDEP_add2_debug) --cpu=Cortex-A15 --mm $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) --cpu=Cortex-A15 --mm $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.o: %.c
	$(CCDEP_add2_release) --cpu=Cortex-A15 --mm $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.o: %.cpp
	$(CCDEP_add2_release) --cpu=Cortex-A15 --mm $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ > $*.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<

CLEAN_COMPILE_add1_arm_simulate = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d\
                                  $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d\
                                  $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d
CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d
CLEAN_COMPILE_add2_arm_simulate = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d\
                                  $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d\
                                  $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d

cleandeps:
	$(RM) $(CLEAN_COMPILE_add1_arm_simulate)
	$(RM) $(CLEAN_COMPILE_add1_debug)
	$(RM) $(CLEAN_COMPILE_add1_release)
	$(RM) $(CLEAN_COMPILE_add2_arm_simulate)
	$(RM) $(CLEAN_COMPILE_add2_debug)
	$(RM) $(CLEAN_COMPILE_add2_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMPILE_add1_arm_simulate)
	$(RM) $(CLEAN_COMPILE_add1_debug)
	$(RM) $(CLEAN_COMPILE_add1_release)
	$(RM) $(CLEAN_COMPILE_add2_arm_simulate)
	$(RM) $(CLEAN_COMPILE_add2_debug)
	$(RM) $(CLEAN_COMPILE_add2_release)
	$(RM) $(INPUTS_LINK_add1_arm_simulate)
	$(RM) $(INPUTS_LINK_add2_arm_simulate)
	$(RM) $(INPUTS_LINK_add1_debug)
	$(RM) $(INPUTS_LINK_add2_debug)
	$(RM) $(INPUTS_LINK_add1_release)
	$(RM) $(INPUTS_LINK_add2_release)
	$(RM) libfoo_dynamic_add1_arm_simulate.so
	$(RM) libfoo_dynamic_add2_arm_simulate.so
	$(RM) libfoo_dynamic_add1_debug.so
	$(RM) libfoo_dynamic_add2_debug.so
	$(RM) libfoo_dynamic_add1_release.so
	$(RM) libfoo_dynamic_add2_release.so

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_arm_simulate.so"
	@echo " libfoo_dynamic_add2_arm_simulate.so"
	@echo " libfoo_dynamic_add1_debug.so"
	@echo " libfoo_dynamic_add2_debug.so"
	@echo " libfoo_dynamic_add1_release.so"
	@echo " libfoo_dynamic_add2_release.so"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_arm_simulate.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_rvbare_cortex_a15_vfp_neon_rvct_add2_release.d)


