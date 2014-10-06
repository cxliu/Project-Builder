#-*-makefile-*-

BASE=../../../../
CCDEP_add1_debug = icc
CCDEP_add1_release = icc
CCDEP_add2_debug = icc
CCDEP_add2_release = icc
CC_add1_debug = icc
CC_add1_release = icc
CC_add2_debug = icc
CC_add2_release = icc
CFLAGS_add1_debug = -c -w3 -std=c99 -wd2415,981,1572 -g -O0 -isystem/usr/include
CFLAGS_add1_release = -c -w3 -std=c99 -wd2415,981,1572 -O3 -funroll-loops -ansi-alias -Wstrict-aliasing -fp-model fast=2 -isystem/usr/include
CFLAGS_add2_debug = -c -w3 -std=c99 -wd2415,981,1572 -g -O0 -isystem/usr/include
CFLAGS_add2_release = -c -w3 -std=c99 -wd2415,981,1572 -O3 -funroll-loops -ansi-alias -Wstrict-aliasing -fp-model fast=2 -isystem/usr/include
CXXFLAGS_add1_debug = -c -w3 -std=c++0x -wd2415,981,1572 -g -O0 -isystem/usr/include
CXXFLAGS_add1_release = -c -w3 -std=c++0x -wd2415,981,1572 -O3 -funroll-loops -ansi-alias -Wstrict-aliasing -fp-model fast=2 -isystem/usr/include
CXXFLAGS_add2_debug = -c -w3 -std=c++0x -wd2415,981,1572 -g -O0 -isystem/usr/include
CXXFLAGS_add2_release = -c -w3 -std=c++0x -wd2415,981,1572 -O3 -funroll-loops -ansi-alias -Wstrict-aliasing -fp-model fast=2 -isystem/usr/include
CXX_add1_debug = icpc
CXX_add1_release = icpc
CXX_add2_debug = icpc
CXX_add2_release = icpc
DEFINES_add1_debug = -DADD_THIS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add2_debug = -DADD_THIS=2
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).
LDFLAGS_add1_debug = -fPIC -shared
LDFLAGS_add1_release = -fPIC -shared
LDFLAGS_add2_debug = -fPIC -shared
LDFLAGS_add2_release = -fPIC -shared
LD_add1_debug = icc
LD_add1_release = icc
LD_add2_debug = icc
LD_add2_release = icc


INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_debug.o
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_release.o
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_debug.o
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_release.o


default: libfoo_dynamic_add1_debug.so libfoo_dynamic_add2_debug.so libfoo_dynamic_add1_release.so libfoo_dynamic_add2_release.so

libfoo_dynamic_add1_debug.so: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) -o $@ $+ 

libfoo_dynamic_add2_debug.so: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) -o $@ $+ 

libfoo_dynamic_add1_release.so: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) -o $@ $+ 

libfoo_dynamic_add2_release.so: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) -o $@ $+ 

%.libfoo_dynamic_osx_amd64_icc_add1_debug.o: %.c
	$(CCDEP_add1_debug) -isystem/usr/include -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) -isystem/usr/include -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add1_release.o: %.c
	$(CCDEP_add1_release) -isystem/usr/include -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add1_release.o: %.cpp
	$(CCDEP_add1_release) -isystem/usr/include -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add2_debug.o: %.c
	$(CCDEP_add2_debug) -isystem/usr/include -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) -isystem/usr/include -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add2_release.o: %.c
	$(CCDEP_add2_release) -isystem/usr/include -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_dynamic_osx_amd64_icc_add2_release.o: %.cpp
	$(CCDEP_add2_release) -isystem/usr/include -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_osx_amd64_icc_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_release.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_release.d

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
	$(RM) libfoo_dynamic_add1_debug.so
	$(RM) libfoo_dynamic_add2_debug.so
	$(RM) libfoo_dynamic_add1_release.so
	$(RM) libfoo_dynamic_add2_release.so

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_debug.so"
	@echo " libfoo_dynamic_add2_debug.so"
	@echo " libfoo_dynamic_add1_release.so"
	@echo " libfoo_dynamic_add2_release.so"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_osx_amd64_icc_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_osx_amd64_icc_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_osx_amd64_icc_add2_release.d)


