#-*-makefile-*-

BASE=../../../../
CCDEP_debug = armcc
CCDEP_release = armcc
CC_debug = armcc
CC_release = armcc
CFLAGS_debug = --cpu=5TE -g -O0 --apcs=/interwork -c --c99
CFLAGS_release = --cpu=5TE -O3 -Otime --apcs=/interwork -c --c99
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE).
INCLUDES_release = -I$(BASE).
LDFLAGS_debug = -L--cpu=5TE -L--sysv
LDFLAGS_release = -L--cpu=5TE -L--sysv
LD_debug = armcc
LD_release = armcc

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_qemu_armv5te_rvct_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_qemu_armv5te_rvct_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/qemu_armv5te_rvct/libhelloworld_debug.lib
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/qemu_armv5te_rvct/libhelloworld_release.lib

default: helloworld_frontend_debug.axf helloworld_frontend_release.axf

helloworld_frontend_debug.axf: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $+ 

helloworld_frontend_release.axf: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $+ 

%.helloworld_frontend_qemu_armv5te_rvct_debug.o: %.c
	$(CCDEP_debug) --cpu=5TE --mm $(INCLUDES_debug) -o $@ > $*.helloworld_frontend_qemu_armv5te_rvct_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_frontend_qemu_armv5te_rvct_release.o: %.c
	$(CCDEP_release) --cpu=5TE --mm $(DEFINES_release) $(INCLUDES_release) -o $@ > $*.helloworld_frontend_qemu_armv5te_rvct_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_frontend_qemu_armv5te_rvct_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_frontend_qemu_armv5te_rvct_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/qemu_armv5te_rvct cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_frontend_debug.axf
	$(RM) helloworld_frontend_release.axf

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_frontend_debug.axf"
	@echo " helloworld_frontend_release.axf"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_qemu_armv5te_rvct_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_qemu_armv5te_rvct_release.d)

%.lib: FORCE
	$(MAKE) -C $(@D) $(@F)


