#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -rc
ARFLAGS_release = -rc
AR_debug = xiar
AR_release = xiar
CCDEP_debug = icc
CCDEP_release = icc
CC_debug = icc
CC_release = icc
CFLAGS_debug = -c -w3 -std=c99 -wd2415,981,1572 -g -O0 -isystem/usr/include
CFLAGS_release = -c -w3 -std=c99 -wd2415,981,1572 -O3 -funroll-loops -ansi-alias -Wstrict-aliasing -fp-model fast=2 -isystem/usr/include
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_osx_amd64_icc_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_osx_amd64_icc_release.o,$(COMMON_FILES))


default: libhelloworld_debug.a libhelloworld_release.a

libhelloworld_debug.a: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)  $@ $^

libhelloworld_release.a: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)  $@ $^

%.libhelloworld_osx_amd64_icc_debug.o: %.c
	$(CCDEP_debug) -isystem/usr/include -MM $(INCLUDES_debug) -MT $@ -o $*.libhelloworld_osx_amd64_icc_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_osx_amd64_icc_release.o: %.c
	$(CCDEP_release) -isystem/usr/include -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.libhelloworld_osx_amd64_icc_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_osx_amd64_icc_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_osx_amd64_icc_release.d,$(COMMON_FILES))

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

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_osx_amd64_icc_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_osx_amd64_icc_release.d)


