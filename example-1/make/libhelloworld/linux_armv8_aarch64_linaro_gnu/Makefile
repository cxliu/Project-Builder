#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -rc
ARFLAGS_release = -rc
AR_debug = aarch64-linux-gnu-ar
AR_release = aarch64-linux-gnu-ar
CCDEP_debug = aarch64-linux-gnu-gcc
CCDEP_release = aarch64-linux-gnu-gcc
CC_debug = aarch64-linux-gnu-gcc
CC_release = aarch64-linux-gnu-gcc
CFLAGS_debug = -march=armv8-a -O0 -g -c -Wall -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_release = -march=armv8-a -O3 -funroll-loops -c -Wall -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_linux_armv8_aarch64_linaro_gnu_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_linux_armv8_aarch64_linaro_gnu_release.o,$(COMMON_FILES))


default: libhelloworld_debug.a libhelloworld_release.a

libhelloworld_debug.a: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)   $@ $^

libhelloworld_release.a: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)   $@ $^

%.libhelloworld_linux_armv8_aarch64_linaro_gnu_debug.o: %.c
	$(CCDEP_debug) -march=armv8-a -MM $(INCLUDES_debug) -MT $@ -o $*.libhelloworld_linux_armv8_aarch64_linaro_gnu_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_linux_armv8_aarch64_linaro_gnu_release.o: %.c
	$(CCDEP_release) -march=armv8-a -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.libhelloworld_linux_armv8_aarch64_linaro_gnu_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_linux_armv8_aarch64_linaro_gnu_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_linux_armv8_aarch64_linaro_gnu_release.d,$(COMMON_FILES))

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

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_linux_armv8_aarch64_linaro_gnu_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_linux_armv8_aarch64_linaro_gnu_release.d)


