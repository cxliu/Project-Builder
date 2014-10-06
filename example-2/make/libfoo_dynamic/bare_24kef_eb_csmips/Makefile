#-*-makefile-*-

BASE=../../../../
CCDEP_add1_debug = mips-linux-gnu-gcc
CCDEP_add1_release = mips-linux-gnu-gcc
CCDEP_add2_debug = mips-linux-gnu-gcc
CCDEP_add2_release = mips-linux-gnu-gcc
CC_add1_debug = mips-sde-elf-gcc
CC_add1_release = mips-sde-elf-gcc
CC_add2_debug = mips-sde-elf-gcc
CC_add2_release = mips-sde-elf-gcc
CFLAGS_add1_debug = -EB -mips32r2 -march=24kef -mhard-float -g -O0 -mdsp -c -Wno-attributes
CFLAGS_add1_release = -EB -mips32r2 -march=24kef -mhard-float -O3 -mdsp -c -Wno-attributes
CFLAGS_add2_debug = -EB -mips32r2 -march=24kef -mhard-float -g -O0 -mdsp -c -Wno-attributes
CFLAGS_add2_release = -EB -mips32r2 -march=24kef -mhard-float -O3 -mdsp -c -Wno-attributes
CXXFLAGS_add1_debug = -EB -mips32r2 -march=24kef -g -O0 -mdsp -x c
CXXFLAGS_add1_release = -EB -mips32r2 -march=24kef -O3 -mdsp -x c
CXXFLAGS_add2_debug = -EB -mips32r2 -march=24kef -g -O0 -mdsp -x c
CXXFLAGS_add2_release = -EB -mips32r2 -march=24kef -O3 -mdsp -x c
CXX_add1_debug = mips-sde-elf-g++
CXX_add1_release = mips-sde-elf-g++
CXX_add2_debug = mips-sde-elf-g++
CXX_add2_release = mips-sde-elf-g++
DEFINES_add1_debug = -DADD_THIS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add2_debug = -DADD_THIS=2
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).
LDFLAGS_add1_debug = -Tmalta-ram-hosted.ld -EB -static -mhard-float
LDFLAGS_add1_release = -Tmalta-ram-hosted.ld -EB -static -mhard-float
LDFLAGS_add2_debug = -Tmalta-ram-hosted.ld -EB -static -mhard-float
LDFLAGS_add2_release = -Tmalta-ram-hosted.ld -EB -static -mhard-float
LD_add1_debug = mips-sde-elf-gcc
LD_add1_release = mips-sde-elf-gcc
LD_add2_debug = mips-sde-elf-gcc
LD_add2_release = mips-sde-elf-gcc


INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o


default: libfoo_dynamic_add1_debug.a libfoo_dynamic_add2_debug.a libfoo_dynamic_add1_release.a libfoo_dynamic_add2_release.a

libfoo_dynamic_add1_debug.a: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) -o $@ $+ 

libfoo_dynamic_add2_debug.a: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) -o $@ $+ 

libfoo_dynamic_add1_release.a: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) -o $@ $+ 

libfoo_dynamic_add2_release.a: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) -o $@ $+ 

$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.cc
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.cc
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.cxx
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.cxx
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.cc
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.cc
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.cxx
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.cxx
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.cc
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.cc
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.cxx
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.cxx
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.cc
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.cc
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.cxx
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<


$(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d: $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.cxx
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<


%.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: %.c
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: %.cc
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.o: %.cxx
	$(CCDEP_add1_debug) -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: %.c
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: %.cc
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: %.cpp
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.o: %.cxx
	$(CCDEP_add1_release) -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: %.c
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: %.cc
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.o: %.cxx
	$(CCDEP_add2_debug) -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: %.c
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: %.cc
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: %.cpp
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<

%.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.o: %.cxx
	$(CCDEP_add2_release) -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o  $@ $<

CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d\
                             $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d

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
	$(RM) libfoo_dynamic_add1_debug.a
	$(RM) libfoo_dynamic_add2_debug.a
	$(RM) libfoo_dynamic_add1_release.a
	$(RM) libfoo_dynamic_add2_release.a

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_debug.a"
	@echo " libfoo_dynamic_add2_debug.a"
	@echo " libfoo_dynamic_add1_release.a"
	@echo " libfoo_dynamic_add2_release.a"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_bare_24kef_eb_csmips_add2_release.d)


