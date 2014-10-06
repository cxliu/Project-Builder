#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -rc
ARFLAGS_release = -rc
AR_debug = mips-sde-elf-ar
AR_release = mips-sde-elf-ar
CCDEP_debug = mips-linux-gnu-gcc
CCDEP_release = mips-linux-gnu-gcc
CC_debug = mips-sde-elf-gcc
CC_release = mips-sde-elf-gcc
CFLAGS_debug = -EL -mips32r2 -march=24kec -msoft-float -g -O0 -mdsp -c -Wno-attributes
CFLAGS_release = -EL -mips32r2 -march=24kec -msoft-float -O3 -mdsp -c -Wno-attributes
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_bare_24kec_el_csmips_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_bare_24kec_el_csmips_release.o,$(COMMON_FILES))


default: libhelloworld_debug.a libhelloworld_release.a

libhelloworld_debug.a: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)   $@ $^

libhelloworld_release.a: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)   $@ $^

%.libhelloworld_bare_24kec_el_csmips_debug.o: %.c
	$(CCDEP_debug) -MM $(INCLUDES_debug) -MT $@ -o $*.libhelloworld_bare_24kec_el_csmips_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_bare_24kec_el_csmips_release.o: %.c
	$(CCDEP_release) -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.libhelloworld_bare_24kec_el_csmips_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_bare_24kec_el_csmips_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_bare_24kec_el_csmips_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_ARCHIVE_debug)
	$(RM) $(INPUTS_COMMON_ARCHIVE_release)
	$(RM) libhelloworld_debug.a
	$(RM) libhelloworld_release.a

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libhelloworld_debug.a"
	@echo " libhelloworld_release.a"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_bare_24kec_el_csmips_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_bare_24kec_el_csmips_release.d)


