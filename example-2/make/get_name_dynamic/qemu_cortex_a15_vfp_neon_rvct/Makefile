#-*-makefile-*-

BASE=../../../../
CCDEP_lower_add1_debug = armcc
CCDEP_lower_add1_release = armcc
CCDEP_lower_add2_debug = armcc
CCDEP_lower_add2_release = armcc
CCDEP_upper_add1_debug = armcc
CCDEP_upper_add1_release = armcc
CCDEP_upper_add2_debug = armcc
CCDEP_upper_add2_release = armcc
CC_lower_add1_debug = armcc
CC_lower_add1_release = armcc
CC_lower_add2_debug = armcc
CC_lower_add2_release = armcc
CC_upper_add1_debug = armcc
CC_upper_add1_release = armcc
CC_upper_add2_debug = armcc
CC_upper_add2_release = armcc
CFLAGS_lower_add1_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_lower_add1_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_lower_add2_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_lower_add2_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_upper_add1_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_upper_add1_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
CFLAGS_upper_add2_debug = --cpu=Cortex-A15 --fpu=VFPv4 -g -O0 --apcs=/interwork -c --c99
CFLAGS_upper_add2_release = --cpu=Cortex-A15 --fpu=VFPv4 -O3 -Otime --apcs=/interwork -c --c99
DEFINES_lower_add1_debug = -DADD_THIS=1 -DGET_NAME_TRANSFORM=tolower
DEFINES_lower_add1_release = -DADD_THIS=1 -DGET_NAME_TRANSFORM=tolower -DNDEBUG=1
DEFINES_lower_add2_debug = -DADD_THIS=2 -DGET_NAME_TRANSFORM=tolower
DEFINES_lower_add2_release = -DADD_THIS=2 -DGET_NAME_TRANSFORM=tolower -DNDEBUG=1
DEFINES_upper_add1_debug = -DADD_THIS=1 -DGET_NAME_TRANSFORM=toupper
DEFINES_upper_add1_release = -DADD_THIS=1 -DGET_NAME_TRANSFORM=toupper -DNDEBUG=1
DEFINES_upper_add2_debug = -DADD_THIS=2 -DGET_NAME_TRANSFORM=toupper
DEFINES_upper_add2_release = -DADD_THIS=2 -DGET_NAME_TRANSFORM=toupper -DNDEBUG=1
INCLUDES_lower_add1_debug = -I$(BASE).
INCLUDES_lower_add1_release = -I$(BASE).
INCLUDES_lower_add2_debug = -I$(BASE).
INCLUDES_lower_add2_release = -I$(BASE).
INCLUDES_upper_add1_debug = -I$(BASE).
INCLUDES_upper_add1_release = -I$(BASE).
INCLUDES_upper_add2_debug = -I$(BASE).
INCLUDES_upper_add2_release = -I$(BASE).
LDFLAGS_lower_add1_debug = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_lower_add1_release = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_lower_add2_debug = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_lower_add2_release = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_upper_add1_debug = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_upper_add1_release = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_upper_add2_debug = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LDFLAGS_upper_add2_release = --cpp -L--cpu=Cortex-A15 -L--fpu=VFPv4 -L--sysv
LD_lower_add1_debug = armcc
LD_lower_add1_release = armcc
LD_lower_add2_debug = armcc
LD_lower_add2_release = armcc
LD_upper_add1_debug = armcc
LD_upper_add1_release = armcc
LD_upper_add2_debug = armcc
LD_upper_add2_release = armcc

COMMON_FILES = $(BASE)example-2/frontend/main $(BASE)example-2/src/get_name/get_name $(BASE)example-2/src/get_name/get_name_raw

INPUTS_COMMON_LINK_lower_add1_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add1_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_lower_add1_debug = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add1_debug.so
DEP_PROJ_LINK_lower_add1_release = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add1_release.so
DEP_PROJ_LINK_lower_add2_debug = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add2_debug.so
DEP_PROJ_LINK_lower_add2_release = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add2_release.so
DEP_PROJ_LINK_upper_add1_debug = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add1_debug.so
DEP_PROJ_LINK_upper_add1_release = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add1_release.so
DEP_PROJ_LINK_upper_add2_debug = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add2_debug.so
DEP_PROJ_LINK_upper_add2_release = $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct/libfoo_dynamic_add2_release.so

default: get_name_dynamic_lower_add1_debug.axf get_name_dynamic_lower_add2_debug.axf get_name_dynamic_upper_add1_debug.axf get_name_dynamic_upper_add2_debug.axf get_name_dynamic_lower_add1_release.axf get_name_dynamic_lower_add2_release.axf get_name_dynamic_upper_add1_release.axf get_name_dynamic_upper_add2_release.axf

get_name_dynamic_lower_add1_debug.axf: $(INPUTS_COMMON_LINK_lower_add1_debug) $(DEP_PROJ_LINK_lower_add1_debug)
	$(LD_lower_add1_debug) $(LDFLAGS_lower_add1_debug) -o $@ $+ 

get_name_dynamic_lower_add2_debug.axf: $(INPUTS_COMMON_LINK_lower_add2_debug) $(DEP_PROJ_LINK_lower_add2_debug)
	$(LD_lower_add2_debug) $(LDFLAGS_lower_add2_debug) -o $@ $+ 

get_name_dynamic_upper_add1_debug.axf: $(INPUTS_COMMON_LINK_upper_add1_debug) $(DEP_PROJ_LINK_upper_add1_debug)
	$(LD_upper_add1_debug) $(LDFLAGS_upper_add1_debug) -o $@ $+ 

get_name_dynamic_upper_add2_debug.axf: $(INPUTS_COMMON_LINK_upper_add2_debug) $(DEP_PROJ_LINK_upper_add2_debug)
	$(LD_upper_add2_debug) $(LDFLAGS_upper_add2_debug) -o $@ $+ 

get_name_dynamic_lower_add1_release.axf: $(INPUTS_COMMON_LINK_lower_add1_release) $(DEP_PROJ_LINK_lower_add1_release)
	$(LD_lower_add1_release) $(LDFLAGS_lower_add1_release) -o $@ $+ 

get_name_dynamic_lower_add2_release.axf: $(INPUTS_COMMON_LINK_lower_add2_release) $(DEP_PROJ_LINK_lower_add2_release)
	$(LD_lower_add2_release) $(LDFLAGS_lower_add2_release) -o $@ $+ 

get_name_dynamic_upper_add1_release.axf: $(INPUTS_COMMON_LINK_upper_add1_release) $(DEP_PROJ_LINK_upper_add1_release)
	$(LD_upper_add1_release) $(LDFLAGS_upper_add1_release) -o $@ $+ 

get_name_dynamic_upper_add2_release.axf: $(INPUTS_COMMON_LINK_upper_add2_release) $(DEP_PROJ_LINK_upper_add2_release)
	$(LD_upper_add2_release) $(LDFLAGS_upper_add2_release) -o $@ $+ 

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.o: %.c
	$(CCDEP_lower_add1_debug) --cpu=Cortex-A15 --mm $(DEFINES_lower_add1_debug) $(INCLUDES_lower_add1_debug) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.d $<
	$(CC_lower_add1_debug) $(CFLAGS_lower_add1_debug) $(DEFINES_lower_add1_debug) $(INCLUDES_lower_add1_debug) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.o: %.c
	$(CCDEP_lower_add1_release) --cpu=Cortex-A15 --mm $(DEFINES_lower_add1_release) $(INCLUDES_lower_add1_release) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.d $<
	$(CC_lower_add1_release) $(CFLAGS_lower_add1_release) $(DEFINES_lower_add1_release) $(INCLUDES_lower_add1_release) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.o: %.c
	$(CCDEP_lower_add2_debug) --cpu=Cortex-A15 --mm $(DEFINES_lower_add2_debug) $(INCLUDES_lower_add2_debug) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.d $<
	$(CC_lower_add2_debug) $(CFLAGS_lower_add2_debug) $(DEFINES_lower_add2_debug) $(INCLUDES_lower_add2_debug) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.o: %.c
	$(CCDEP_lower_add2_release) --cpu=Cortex-A15 --mm $(DEFINES_lower_add2_release) $(INCLUDES_lower_add2_release) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.d $<
	$(CC_lower_add2_release) $(CFLAGS_lower_add2_release) $(DEFINES_lower_add2_release) $(INCLUDES_lower_add2_release) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.o: %.c
	$(CCDEP_upper_add1_debug) --cpu=Cortex-A15 --mm $(DEFINES_upper_add1_debug) $(INCLUDES_upper_add1_debug) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.d $<
	$(CC_upper_add1_debug) $(CFLAGS_upper_add1_debug) $(DEFINES_upper_add1_debug) $(INCLUDES_upper_add1_debug) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.o: %.c
	$(CCDEP_upper_add1_release) --cpu=Cortex-A15 --mm $(DEFINES_upper_add1_release) $(INCLUDES_upper_add1_release) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.d $<
	$(CC_upper_add1_release) $(CFLAGS_upper_add1_release) $(DEFINES_upper_add1_release) $(INCLUDES_upper_add1_release) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.o: %.c
	$(CCDEP_upper_add2_debug) --cpu=Cortex-A15 --mm $(DEFINES_upper_add2_debug) $(INCLUDES_upper_add2_debug) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.d $<
	$(CC_upper_add2_debug) $(CFLAGS_upper_add2_debug) $(DEFINES_upper_add2_debug) $(INCLUDES_upper_add2_debug) -o $@ $<

%.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.o: %.c
	$(CCDEP_upper_add2_release) --cpu=Cortex-A15 --mm $(DEFINES_upper_add2_release) $(INCLUDES_upper_add2_release) -o $@ > $*.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.d $<
	$(CC_upper_add2_release) $(CFLAGS_upper_add2_release) $(DEFINES_upper_add2_release) $(INCLUDES_upper_add2_release) -o $@ $<

CLEAN_COMMON_COMPILE_lower_add1_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add1_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add2_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add2_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add1_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add1_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add2_debug = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add2_release = $(addsuffix .get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-2/make/libfoo_dynamic/qemu_cortex_a15_vfp_neon_rvct cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_release)
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_release)
	$(RM) get_name_dynamic_lower_add1_debug.axf
	$(RM) get_name_dynamic_lower_add2_debug.axf
	$(RM) get_name_dynamic_upper_add1_debug.axf
	$(RM) get_name_dynamic_upper_add2_debug.axf
	$(RM) get_name_dynamic_lower_add1_release.axf
	$(RM) get_name_dynamic_lower_add2_release.axf
	$(RM) get_name_dynamic_upper_add1_release.axf
	$(RM) get_name_dynamic_upper_add2_release.axf

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " get_name_dynamic_lower_add1_debug.axf"
	@echo " get_name_dynamic_lower_add2_debug.axf"
	@echo " get_name_dynamic_upper_add1_debug.axf"
	@echo " get_name_dynamic_upper_add2_debug.axf"
	@echo " get_name_dynamic_lower_add1_release.axf"
	@echo " get_name_dynamic_lower_add2_release.axf"
	@echo " get_name_dynamic_upper_add1_release.axf"
	@echo " get_name_dynamic_upper_add2_release.axf"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add1_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_lower_add2_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add1_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_dynamic_qemu_cortex_a15_vfp_neon_rvct_upper_add2_release.d)

%.so: FORCE
	$(MAKE) -C $(@D) $(@F)


