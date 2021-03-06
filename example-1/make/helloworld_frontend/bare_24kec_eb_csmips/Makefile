#-*-makefile-*-

BASE=../../../../
CCDEP_debug = mips-linux-gnu-gcc
CCDEP_release = mips-linux-gnu-gcc
CC_debug = mips-sde-elf-gcc
CC_release = mips-sde-elf-gcc
CFLAGS_debug = -EB -mips32r2 -march=24kec -msoft-float -g -O0 -mdsp -c -Wno-attributes
CFLAGS_release = -EB -mips32r2 -march=24kec -msoft-float -O3 -mdsp -c -Wno-attributes
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE).
INCLUDES_release = -I$(BASE).
LDFLAGS_debug = -Tmalta-ram-hosted.ld -EB -static -msoft-float
LDFLAGS_release = -Tmalta-ram-hosted.ld -EB -static -msoft-float
LDLIBS_debug = -lm
LDLIBS_release = -lm
LD_debug = mips-sde-elf-gcc
LD_release = mips-sde-elf-gcc

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_bare_24kec_eb_csmips_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_bare_24kec_eb_csmips_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/bare_24kec_eb_csmips/libhelloworld_debug.a
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/bare_24kec_eb_csmips/libhelloworld_release.a

default: helloworld_frontend_debug helloworld_frontend_release

helloworld_frontend_debug: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $+ $(LDLIBS_debug)

helloworld_frontend_release: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $+ $(LDLIBS_release)

%.helloworld_frontend_bare_24kec_eb_csmips_debug.o: %.c
	$(CCDEP_debug) -MM $(INCLUDES_debug) -MT $@ -o $*.helloworld_frontend_bare_24kec_eb_csmips_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_frontend_bare_24kec_eb_csmips_release.o: %.c
	$(CCDEP_release) -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.helloworld_frontend_bare_24kec_eb_csmips_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_frontend_bare_24kec_eb_csmips_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_frontend_bare_24kec_eb_csmips_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/bare_24kec_eb_csmips cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_frontend_debug
	$(RM) helloworld_frontend_release

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_frontend_debug"
	@echo " helloworld_frontend_release"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_bare_24kec_eb_csmips_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_bare_24kec_eb_csmips_release.d)

%.a: FORCE
	$(MAKE) -C $(@D) $(@F)


