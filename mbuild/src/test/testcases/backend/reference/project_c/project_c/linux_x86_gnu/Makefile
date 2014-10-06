#-*-makefile-*-

BASE=../../../../../../../../../
CCDEP_c0_debug = $(CC)
CCDEP_c0_release = $(CC)
CCDEP_c1_debug = $(CC)
CCDEP_c1_release = $(CC)
CC_c0_debug = $(CC)
CC_c0_release = $(CC)
CC_c1_debug = $(CC)
CC_c1_release = $(CC)
CFLAGS_c0_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_c0_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_c1_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_c1_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
DEFINES_c0_release = -DNDEBUG=1
DEFINES_c1_release = -DNDEBUG=1
LDFLAGS_c0_debug = -rdynamic -m32
LDFLAGS_c0_release = -O2 -m32
LDFLAGS_c1_debug = -rdynamic -m32
LDFLAGS_c1_release = -O2 -m32
LD_c0_debug = gcc
LD_c0_release = gcc
LD_c1_debug = gcc
LD_c1_release = gcc

COMMON_FILES = $(BASE)mbuild/src/test/testcases/backend/input/project_c/file

INPUTS_COMMON_LINK_c0_debug = $(addsuffix .project_c_linux_x86_gnu_c0_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_c0_release = $(addsuffix .project_c_linux_x86_gnu_c0_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_c1_debug = $(addsuffix .project_c_linux_x86_gnu_c1_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_c1_release = $(addsuffix .project_c_linux_x86_gnu_c1_release.o,$(COMMON_FILES))


default: project_c_c0_debug.a project_c_c1_debug.a project_c_c0_release.a project_c_c1_release.a

project_c_c0_debug.a: $(INPUTS_COMMON_LINK_c0_debug)
	$(LD_c0_debug) $(LDFLAGS_c0_debug) -o $@ $+ 

project_c_c1_debug.a: $(INPUTS_COMMON_LINK_c1_debug)
	$(LD_c1_debug) $(LDFLAGS_c1_debug) -o $@ $+ 

project_c_c0_release.a: $(INPUTS_COMMON_LINK_c0_release)
	$(LD_c0_release) $(LDFLAGS_c0_release) -o $@ $+ 

project_c_c1_release.a: $(INPUTS_COMMON_LINK_c1_release)
	$(LD_c1_release) $(LDFLAGS_c1_release) -o $@ $+ 

%.project_c_linux_x86_gnu_c0_debug.o: %.c
	$(CCDEP_c0_debug) -msse2 -MM -MT $@ -o $*.project_c_linux_x86_gnu_c0_debug.d $<
	$(CC_c0_debug) $(CFLAGS_c0_debug) -o $@ $<

%.project_c_linux_x86_gnu_c0_release.o: %.c
	$(CCDEP_c0_release) -msse2 -MM $(DEFINES_c0_release) -MT $@ -o $*.project_c_linux_x86_gnu_c0_release.d $<
	$(CC_c0_release) $(CFLAGS_c0_release) $(DEFINES_c0_release) -o $@ $<

%.project_c_linux_x86_gnu_c1_debug.o: %.c
	$(CCDEP_c1_debug) -msse2 -MM -MT $@ -o $*.project_c_linux_x86_gnu_c1_debug.d $<
	$(CC_c1_debug) $(CFLAGS_c1_debug) -o $@ $<

%.project_c_linux_x86_gnu_c1_release.o: %.c
	$(CCDEP_c1_release) -msse2 -MM $(DEFINES_c1_release) -MT $@ -o $*.project_c_linux_x86_gnu_c1_release.d $<
	$(CC_c1_release) $(CFLAGS_c1_release) $(DEFINES_c1_release) -o $@ $<

CLEAN_COMMON_COMPILE_c0_debug = $(addsuffix .project_c_linux_x86_gnu_c0_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_c0_release = $(addsuffix .project_c_linux_x86_gnu_c0_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_c1_debug = $(addsuffix .project_c_linux_x86_gnu_c1_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_c1_release = $(addsuffix .project_c_linux_x86_gnu_c1_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_c0_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_c0_release)
	$(RM) $(CLEAN_COMMON_COMPILE_c1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_c1_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_c0_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_c0_release)
	$(RM) $(CLEAN_COMMON_COMPILE_c1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_c1_release)
	$(RM) $(INPUTS_COMMON_LINK_c0_debug)
	$(RM) $(INPUTS_COMMON_LINK_c1_debug)
	$(RM) $(INPUTS_COMMON_LINK_c0_release)
	$(RM) $(INPUTS_COMMON_LINK_c1_release)
	$(RM) project_c_c0_debug.a
	$(RM) project_c_c1_debug.a
	$(RM) project_c_c0_release.a
	$(RM) project_c_c1_release.a

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " project_c_c0_debug.a"
	@echo " project_c_c1_debug.a"
	@echo " project_c_c0_release.a"
	@echo " project_c_c1_release.a"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)mbuild/src/test/testcases/backend/input/project_c/file.project_c_linux_x86_gnu_c0_debug.d)
include $(wildcard $(BASE)mbuild/src/test/testcases/backend/input/project_c/file.project_c_linux_x86_gnu_c0_release.d)
include $(wildcard $(BASE)mbuild/src/test/testcases/backend/input/project_c/file.project_c_linux_x86_gnu_c1_debug.d)
include $(wildcard $(BASE)mbuild/src/test/testcases/backend/input/project_c/file.project_c_linux_x86_gnu_c1_release.d)


