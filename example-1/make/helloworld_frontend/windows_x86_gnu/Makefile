#-*-makefile-*-

BASE=../../../../
CCDEP_debug = $(CC)
CCDEP_release = $(CC)
CC_debug = $(CC)
CC_release = $(CC)
CFLAGS_debug = -msse2 -g -ggdb3 -O0 -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_release = -msse2 -O3 -funroll-loops -ftree-vectorize -m32 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
DEFINES_debug = -DWIN32=1 -D_CONSOLE=1
DEFINES_release = -DNDEBUG=1 -DWIN32=1 -D_CONSOLE=1
INCLUDES_debug = -I$(BASE).
INCLUDES_release = -I$(BASE).
LDFLAGS_debug = -rdynamic -m32
LDFLAGS_release = -O2 -m32
LDLIBS_debug = -lm
LDLIBS_release = -lm
LD_debug = gcc
LD_release = gcc

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_windows_x86_gnu_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_windows_x86_gnu_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/windows_x86_gnu/libhelloworld_debug.lib
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/windows_x86_gnu/libhelloworld_release.lib

default: helloworld_frontend_debug.exe helloworld_frontend_release.exe

helloworld_frontend_debug.exe: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $+ $(LDLIBS_debug)

helloworld_frontend_release.exe: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $+ $(LDLIBS_release)

%.helloworld_frontend_windows_x86_gnu_debug.o: %.c
	$(CCDEP_debug) -msse2 -MM $(DEFINES_debug) $(INCLUDES_debug) -MT $@ -o $*.helloworld_frontend_windows_x86_gnu_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_frontend_windows_x86_gnu_release.o: %.c
	$(CCDEP_release) -msse2 -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.helloworld_frontend_windows_x86_gnu_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_frontend_windows_x86_gnu_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_frontend_windows_x86_gnu_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/windows_x86_gnu cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_frontend_debug.exe
	$(RM) helloworld_frontend_release.exe

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_frontend_debug.exe"
	@echo " helloworld_frontend_release.exe"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_windows_x86_gnu_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_windows_x86_gnu_release.d)

%.lib: FORCE
	$(MAKE) -C $(@D) $(@F)


