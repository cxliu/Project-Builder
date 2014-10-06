#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = -rc -s
ARFLAGS_release = -rc -s
AR_debug = xcrun -sdk iphoneos ar
AR_release = xcrun -sdk iphoneos ar
CCDEP_debug = xcrun -sdk iphoneos clang -arch armv7
CCDEP_release = xcrun -sdk iphoneos clang -arch armv7
CC_debug = xcrun -sdk iphoneos clang
CC_release = xcrun -sdk iphoneos clang
CFLAGS_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include -I${IPPROOT}/include
INCLUDES_release = -I$(BASE)example-1/include -I${IPPROOT}/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_ios_cortex_a9_vfp_neon_clang_debug.o,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_ios_cortex_a9_vfp_neon_clang_release.o,$(COMMON_FILES))


default: libhelloworld_debug.a libhelloworld_release.a

libhelloworld_debug.a: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug)   $@ $^

libhelloworld_release.a: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release)   $@ $^

%.libhelloworld_ios_cortex_a9_vfp_neon_clang_debug.o: %.c
	$(CCDEP_debug) -MM $(INCLUDES_debug) -MT $@ -o $*.libhelloworld_ios_cortex_a9_vfp_neon_clang_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.libhelloworld_ios_cortex_a9_vfp_neon_clang_release.o: %.c
	$(CCDEP_release) -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.libhelloworld_ios_cortex_a9_vfp_neon_clang_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .libhelloworld_ios_cortex_a9_vfp_neon_clang_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .libhelloworld_ios_cortex_a9_vfp_neon_clang_release.d,$(COMMON_FILES))

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

include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_ios_cortex_a9_vfp_neon_clang_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.libhelloworld_ios_cortex_a9_vfp_neon_clang_release.d)


