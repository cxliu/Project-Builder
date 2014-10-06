#-*-makefile-*-

BASE=../../../../
ARFLAGS_add1_debug = -rc
ARFLAGS_add1_release = -rc
ARFLAGS_add2_debug = -rc
ARFLAGS_add2_release = -rc
AR_add1_debug = ar
AR_add1_release = ar
AR_add2_debug = ar
AR_add2_release = ar
ASFLAGS_add1_debug = -c
ASFLAGS_add1_release = -c
ASFLAGS_add2_debug = -c
ASFLAGS_add2_release = -c
AS_add1_debug = $(CC)
AS_add1_release = $(CC)
AS_add2_debug = $(CC)
AS_add2_release = $(CC)
CCDEP_add1_debug = $(CC)
CCDEP_add1_release = $(CC)
CCDEP_add2_debug = $(CC)
CCDEP_add2_release = $(CC)
CC_add1_debug = $(CC)
CC_add1_release = $(CC)
CC_add2_debug = $(CC)
CC_add2_release = $(CC)
CFLAGS_add1_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add1_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add2_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_add2_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CXXFLAGS_add1_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall
CXXFLAGS_add1_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall
CXXFLAGS_add2_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall
CXXFLAGS_add2_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall
CXX_add1_debug = $(CXX)
CXX_add1_release = $(CXX)
CXX_add2_debug = $(CXX)
CXX_add2_release = $(CXX)
DEFINES_add1_debug = -DADD_THIS=1
DEFINES_add1_release = -DADD_THIS=1 -DNDEBUG=1
DEFINES_add2_debug = -DADD_THIS=2
DEFINES_add2_release = -DADD_THIS=2 -DNDEBUG=1
INCLUDES_add1_debug = -I$(BASE).
INCLUDES_add1_release = -I$(BASE).
INCLUDES_add2_debug = -I$(BASE).
INCLUDES_add2_release = -I$(BASE).


INPUTS_ARCHIVE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_debug.o $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_debug.o\
                            $(BASE)example-2/src/foo/target/x86/foo_asm_x86_gas.libfoo_static_linux_x86_gnu_add1_debug.o
INPUTS_ARCHIVE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_release.o $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_release.o\
                              $(BASE)example-2/src/foo/target/x86/foo_asm_x86_gas.libfoo_static_linux_x86_gnu_add1_release.o
INPUTS_ARCHIVE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_debug.o $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_debug.o\
                            $(BASE)example-2/src/foo/target/x86/foo_asm_x86_gas.libfoo_static_linux_x86_gnu_add2_debug.o
INPUTS_ARCHIVE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_release.o $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_release.o\
                              $(BASE)example-2/src/foo/target/x86/foo_asm_x86_gas.libfoo_static_linux_x86_gnu_add2_release.o


default: libfoo_static_add1_debug.a libfoo_static_add2_debug.a libfoo_static_add1_release.a libfoo_static_add2_release.a

libfoo_static_add1_debug.a: $(INPUTS_ARCHIVE_add1_debug)
	$(AR_add1_debug) $(ARFLAGS_add1_debug)  $@ $^

libfoo_static_add2_debug.a: $(INPUTS_ARCHIVE_add2_debug)
	$(AR_add2_debug) $(ARFLAGS_add2_debug)  $@ $^

libfoo_static_add1_release.a: $(INPUTS_ARCHIVE_add1_release)
	$(AR_add1_release) $(ARFLAGS_add1_release)  $@ $^

libfoo_static_add2_release.a: $(INPUTS_ARCHIVE_add2_release)
	$(AR_add2_release) $(ARFLAGS_add2_release)  $@ $^

%.libfoo_static_linux_x86_gnu_add1_debug.o: %.c
	$(CCDEP_add1_debug) -msse2 -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add1_debug.d $<
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add1_debug.o: %.cpp
	$(CCDEP_add1_debug) -msse2 -MM $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add1_debug.d $<
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add1_debug.o: %.s
	$(AS_add1_debug) $(ASFLAGS_add1_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add1_release.o: %.c
	$(CCDEP_add1_release) -msse2 -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add1_release.d $<
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_static_linux_x86_gnu_add1_release.o: %.cpp
	$(CCDEP_add1_release) -msse2 -MM $(DEFINES_add1_release) $(INCLUDES_add1_release) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add1_release.d $<
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) -o $@ $<

%.libfoo_static_linux_x86_gnu_add1_release.o: %.s
	$(AS_add1_release) $(ASFLAGS_add1_release) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_debug.o: %.c
	$(CCDEP_add2_debug) -msse2 -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add2_debug.d $<
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_debug.o: %.cpp
	$(CCDEP_add2_debug) -msse2 -MM $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add2_debug.d $<
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_debug.o: %.s
	$(AS_add2_debug) $(ASFLAGS_add2_debug) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_release.o: %.c
	$(CCDEP_add2_release) -msse2 -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add2_release.d $<
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_release.o: %.cpp
	$(CCDEP_add2_release) -msse2 -MM $(DEFINES_add2_release) $(INCLUDES_add2_release) -MT $@ -o $*.libfoo_static_linux_x86_gnu_add2_release.d $<
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) -o $@ $<

%.libfoo_static_linux_x86_gnu_add2_release.o: %.s
	$(AS_add2_release) $(ASFLAGS_add2_release) -o $@ $<

CLEAN_COMPILE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_debug.d $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_debug.d
CLEAN_COMPILE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_release.d $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_release.d
CLEAN_COMPILE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_debug.d $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_debug.d
CLEAN_COMPILE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_release.d $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_release.d

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
	$(RM) $(INPUTS_ARCHIVE_add1_debug)
	$(RM) $(INPUTS_ARCHIVE_add2_debug)
	$(RM) $(INPUTS_ARCHIVE_add1_release)
	$(RM) $(INPUTS_ARCHIVE_add2_release)
	$(RM) libfoo_static_add1_debug.a
	$(RM) libfoo_static_add2_debug.a
	$(RM) libfoo_static_add1_release.a
	$(RM) libfoo_static_add2_release.a

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_static_add1_debug.a"
	@echo " libfoo_static_add2_debug.a"
	@echo " libfoo_static_add1_release.a"
	@echo " libfoo_static_add2_release.a"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add1_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_debug.d)
include $(wildcard $(BASE)example-2/src/foo/foo.libfoo_static_linux_x86_gnu_add2_release.d)
include $(wildcard $(BASE)example-2/src/foo/foo_cpp.libfoo_static_linux_x86_gnu_add2_release.d)


