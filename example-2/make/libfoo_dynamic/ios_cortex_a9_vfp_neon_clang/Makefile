#-*-makefile-*-

BASE=../../../../
CCDEP_add1_debug = xcrun -sdk iphoneos clang -arch armv7
CCDEP_add1_release = xcrun -sdk iphoneos clang -arch armv7
CCDEP_add2_debug = xcrun -sdk iphoneos clang -arch armv7
CCDEP_add2_release = xcrun -sdk iphoneos clang -arch armv7
CC_add1_debug = xcrun -sdk iphoneos clang
CC_add1_release = xcrun -sdk iphoneos clang
CC_add2_debug = xcrun -sdk iphoneos clang
CC_add2_release = xcrun -sdk iphoneos clang
CFLAGS_add1_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_add1_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_add2_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_add2_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CXXFLAGS_add1_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall
CXXFLAGS_add1_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall
CXXFLAGS_add2_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall
CXXFLAGS_add2_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall
CXX_add1_debug = xcrun -sdk iphoneos clang++
CXX_add1_release = xcrun -sdk iphoneos clang++
CXX_add2_debug = xcrun -sdk iphoneos clang++
CXX_add2_release = xcrun -sdk iphoneos clang++
DEFINES_add1_debug = -DADD_THIS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add2_debug = -DADD_THIS=2
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).
LDFLAGS_add1_debug = -fPIC -shared -arch armv7 -arch armv7s
LDFLAGS_add1_release = -O2 -fPIC -shared -arch armv7 -arch armv7s
LDFLAGS_add2_debug = -fPIC -shared -arch armv7 -arch armv7s
LDFLAGS_add2_release = -O2 -fPIC -shared -arch armv7 -arch armv7s
LD_add1_debug = xcrun -sdk iphoneos clang
LD_add1_release = xcrun -sdk iphoneos clang
LD_add2_debug = xcrun -sdk iphoneos clang
LD_add2_release = xcrun -sdk iphoneos clang


INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.o
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.o
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.o
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.o


default: libfoo_dynamic_add1_debug.dylib libfoo_dynamic_add2_debug.dylib libfoo_dynamic_add1_release.dylib libfoo_dynamic_add2_release.dylib

libfoo_dynamic_add1_debug.dylib: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) -o  $@ $+ 

libfoo_dynamic_add2_debug.dylib: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) -o  $@ $+ 

libfoo_dynamic_add1_release.dylib: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) -o  $@ $+ 

libfoo_dynamic_add2_release.dylib: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) -o  $@ $+ 

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.o: %.c
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.o: %.c
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.o: %.cpp
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.o: %.c
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.o: %.c
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.o: %.cpp
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d

cleandeps:
	$(RM) $(CLEAN_COMPILE_add1_debug)
	$(RM) $(CLEAN_COMPILE_add1_release)
	$(RM) $(CLEAN_COMPILE_add2_debug)
	$(RM) $(CLEAN_COMPILE_add2_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMPILE_add1_debug)
	$(RM) $(CLEAN_COMPILE_add1_release)
	$(RM) $(CLEAN_COMPILE_add2_debug)
	$(RM) $(CLEAN_COMPILE_add2_release)
	$(RM) $(INPUTS_LINK_add1_debug)
	$(RM) $(INPUTS_LINK_add2_debug)
	$(RM) $(INPUTS_LINK_add1_release)
	$(RM) $(INPUTS_LINK_add2_release)
	$(RM) libfoo_dynamic_add1_debug.dylib
	$(RM) libfoo_dynamic_add2_debug.dylib
	$(RM) libfoo_dynamic_add1_release.dylib
	$(RM) libfoo_dynamic_add2_release.dylib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_debug.dylib"
	@echo " libfoo_dynamic_add2_debug.dylib"
	@echo " libfoo_dynamic_add1_release.dylib"
	@echo " libfoo_dynamic_add2_release.dylib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_ios_cortex_a9_vfp_neon_clang_add2_release.d)


