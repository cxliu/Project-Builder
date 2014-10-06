#-*-makefile-*-

BASE=../../../../
CCDEP_add1_debug = $(CC)
CCDEP_add1_release = $(CC)
CCDEP_add2_debug = $(CC)
CCDEP_add2_release = $(CC)
CC_add1_debug = $(CC)
CC_add1_release = $(CC)
CC_add2_debug = $(CC)
CC_add2_release = $(CC)
CFLAGS_add1_debug = -msse2 -g -ggdb3 -O0 -fPIC -shared -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add1_release = -msse2 -O3 -funroll-loops -ftree-vectorize -fPIC -shared -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add2_debug = -msse2 -g -ggdb3 -O0 -fPIC -shared -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add2_release = -msse2 -O3 -funroll-loops -ftree-vectorize -fPIC -shared -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CXXFLAGS_add1_debug = -msse2 -g -ggdb3 -O0 -fPIC -shared -m32 -c -Wall
CXXFLAGS_add1_release = -msse2 -O3 -funroll-loops -ftree-vectorize -fPIC -shared -m32 -c -Wall
CXXFLAGS_add2_debug = -msse2 -g -ggdb3 -O0 -fPIC -shared -m32 -c -Wall
CXXFLAGS_add2_release = -msse2 -O3 -funroll-loops -ftree-vectorize -fPIC -shared -m32 -c -Wall
CXX_add1_debug = $(CXX)
CXX_add1_release = $(CXX)
CXX_add2_debug = $(CXX)
CXX_add2_release = $(CXX)
DEFINES_add1_debug = -DADD_THIS=1 -DWIN32=1 -D_USRDLL=1 -D_WINDOWS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1 -DWIN32=1 -D_USRDLL=1 -D_WINDOWS=1
DEFINES_add2_debug = -DADD_THIS=2 -DWIN32=1 -D_USRDLL=1 -D_WINDOWS=1
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1 -DWIN32=1 -D_USRDLL=1 -D_WINDOWS=1
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).
LDFLAGS_add1_debug = -rdynamic -fPIC -shared -m32
LDFLAGS_add1_release = -O2 -fPIC -shared -m32
LDFLAGS_add2_debug = -rdynamic -fPIC -shared -m32
LDFLAGS_add2_release = -O2 -fPIC -shared -m32
LD_add1_debug = gcc
LD_add1_release = gcc
LD_add2_debug = gcc
LD_add2_release = gcc


INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_debug.o
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_release.o
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_debug.o
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_release.o


default: libfoo_dynamic_add1_debug.dll libfoo_dynamic_add2_debug.dll libfoo_dynamic_add1_release.dll libfoo_dynamic_add2_release.dll

libfoo_dynamic_add1_debug.dll: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) -o $@ $+ 

libfoo_dynamic_add2_debug.dll: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) -o $@ $+ 

libfoo_dynamic_add1_release.dll: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) -o $@ $+ 

libfoo_dynamic_add2_release.dll: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) -o $@ $+ 

%.libfoo_dynamic_windows_x86_gnu_add1_debug.o: %.c
	$(CCDEP_add1_debug) -msse2 -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) -msse2 -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add1_release.o: %.c
	$(CCDEP_add1_release) -msse2 -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add1_release.o: %.cpp
	$(CCDEP_add1_release) -msse2 -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add2_debug.o: %.c
	$(CCDEP_add2_debug) -msse2 -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) -msse2 -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add2_release.o: %.c
	$(CCDEP_add2_release) -msse2 -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_dynamic_windows_x86_gnu_add2_release.o: %.cpp
	$(CCDEP_add2_release) -msse2 -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_windows_x86_gnu_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_release.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_release.d

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
	$(RM) libfoo_dynamic_add1_debug.dll
	$(RM) libfoo_dynamic_add2_debug.dll
	$(RM) libfoo_dynamic_add1_release.dll
	$(RM) libfoo_dynamic_add2_release.dll

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_debug.dll"
	@echo " libfoo_dynamic_add2_debug.dll"
	@echo " libfoo_dynamic_add1_release.dll"
	@echo " libfoo_dynamic_add2_release.dll"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_x86_gnu_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_x86_gnu_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_x86_gnu_add2_release.d)


