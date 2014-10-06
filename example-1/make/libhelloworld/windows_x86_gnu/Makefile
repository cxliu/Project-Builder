#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -rc
ARFLAGS_release = -rc
AR_debug = ar
AR_release = ar
CCDEP_debug = $(CC)
CCDEP_release = $(CC)
CC_debug = $(CC)
CC_release = $(CC)
CFLAGS_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
DEFINES_debug = -DWIN32=1 -D_LIB=1
DEFINES_release = -DNDEBUG=1 -DWIN32=1 -D_LIB=1
INCLUDES_debug = -I$(BASE)example-1/include
INCLUDES_release = -I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_windows_x86_gnu_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_windows_x86_gnu_release.o,$(COMMON_FILES))


default: libhelloworld_debug.lib libhelloworld_release.lib

libhelloworld_debug.lib: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)  $@ $^

libhelloworld_release.lib: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)  $@ $^

%.libhelloworld_windows_x86_gnu_debug.o: %.c
	$(CCDEP_debug) -msse2 -MM $(DEFINES_debug) $(INCLUDES_debug) -MT $@ -o $*.libhelloworld_windows_x86_gnu_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_windows_x86_gnu_release.o: %.c
	$(CCDEP_release) -msse2 -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.libhelloworld_windows_x86_gnu_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_windows_x86_gnu_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_windows_x86_gnu_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_ARCHIVE_debug)
	$(RM) $(INPUTS_COMMON_ARCHIVE_release)
	$(RM) libhelloworld_debug.lib
	$(RM) libhelloworld_release.lib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libhelloworld_debug.lib"
	@echo " libhelloworld_release.lib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_windows_x86_gnu_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_windows_x86_gnu_release.d)


