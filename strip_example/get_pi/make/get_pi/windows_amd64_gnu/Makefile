#-*-makefile-*-

BASE=../../../../../
CCDEP_roundingoff_debug = $(CC)
CCDEP_roundingoff_release = $(CC)
CCDEP_roundingon_debug = $(CC)
CCDEP_roundingon_release = $(CC)
CC_roundingoff_debug = $(CC)
CC_roundingoff_release = $(CC)
CC_roundingon_debug = $(CC)
CC_roundingon_release = $(CC)
CFLAGS_roundingoff_debug = -g -ggdb3 -O0 -m64 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_roundingoff_release = -O3 -funroll-loops -ftree-vectorize -m64 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_roundingon_debug = -g -ggdb3 -O0 -m64 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
CFLAGS_roundingon_release = -O3 -funroll-loops -ftree-vectorize -m64 -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wdeclaration-after-statement -Wvla
DEFINES_roundingoff_debug = -DDEBUG=1 -DWIN32=1 -DWIN64=1 -D_CONSOLE=1
DEFINES_roundingoff_release = -DNDEBUG=1 -DWIN32=1 -DWIN64=1 -D_CONSOLE=1
DEFINES_roundingon_debug = -DDEBUG=1 -DROUND=1 -DWIN32=1 -DWIN64=1 -D_CONSOLE=1
DEFINES_roundingon_release = -DNDEBUG=1 -DROUND=1 -DWIN32=1 -DWIN64=1 -D_CONSOLE=1
INCLUDES_roundingoff_debug = -I$(BASE)strip_example/common
INCLUDES_roundingoff_release = -I$(BASE)strip_example/common
INCLUDES_roundingon_debug = -I$(BASE)strip_example/common
INCLUDES_roundingon_release = -I$(BASE)strip_example/common
LDFLAGS_roundingoff_debug = -rdynamic -m64
LDFLAGS_roundingoff_release = -O2 -m64
LDFLAGS_roundingon_debug = -rdynamic -m64
LDFLAGS_roundingon_release = -O2 -m64
LD_roundingoff_debug = gcc
LD_roundingoff_release = gcc
LD_roundingon_debug = gcc
LD_roundingon_release = gcc

COMMON_FILES = $(BASE)strip_example/get_pi/src/get_pi $(BASE)strip_example/get_pi/src/main

INPUTS_COMMON_LINK_roundingoff_debug = $(addsuffix .get_pi_windows_amd64_gnu_roundingoff_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_roundingoff_release = $(addsuffix .get_pi_windows_amd64_gnu_roundingoff_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_roundingon_debug = $(addsuffix .get_pi_windows_amd64_gnu_roundingon_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_roundingon_release = $(addsuffix .get_pi_windows_amd64_gnu_roundingon_release.o,$(COMMON_FILES))
INPUTS_LINK_roundingoff_debug = $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingoff_debug.o
INPUTS_LINK_roundingoff_release = $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingoff_release.o
INPUTS_LINK_roundingon_debug = $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingon_debug.o
INPUTS_LINK_roundingon_release = $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingon_release.o


default: get_pi_roundingoff_debug.exe get_pi_roundingon_debug.exe get_pi_roundingoff_release.exe get_pi_roundingon_release.exe

get_pi_roundingoff_debug.exe: $(INPUTS_COMMON_LINK_roundingoff_debug) $(INPUTS_LINK_roundingoff_debug)
	$(LD_roundingoff_debug) $(LDFLAGS_roundingoff_debug) -o $@ $+ 

get_pi_roundingon_debug.exe: $(INPUTS_COMMON_LINK_roundingon_debug) $(INPUTS_LINK_roundingon_debug)
	$(LD_roundingon_debug) $(LDFLAGS_roundingon_debug) -o $@ $+ 

get_pi_roundingoff_release.exe: $(INPUTS_COMMON_LINK_roundingoff_release) $(INPUTS_LINK_roundingoff_release)
	$(LD_roundingoff_release) $(LDFLAGS_roundingoff_release) -o $@ $+ 

get_pi_roundingon_release.exe: $(INPUTS_COMMON_LINK_roundingon_release) $(INPUTS_LINK_roundingon_release)
	$(LD_roundingon_release) $(LDFLAGS_roundingon_release) -o $@ $+ 

%.get_pi_windows_amd64_gnu_roundingoff_debug.o: %.c
	$(CCDEP_roundingoff_debug) -MM $(DEFINES_roundingoff_debug) $(INCLUDES_roundingoff_debug) -MT $@ -o $*.get_pi_windows_amd64_gnu_roundingoff_debug.d $<
	$(CC_roundingoff_debug) $(CFLAGS_roundingoff_debug) $(DEFINES_roundingoff_debug) $(INCLUDES_roundingoff_debug) -o $@ $<

%.get_pi_windows_amd64_gnu_roundingoff_release.o: %.c
	$(CCDEP_roundingoff_release) -MM $(DEFINES_roundingoff_release) $(INCLUDES_roundingoff_release) -MT $@ -o $*.get_pi_windows_amd64_gnu_roundingoff_release.d $<
	$(CC_roundingoff_release) $(CFLAGS_roundingoff_release) $(DEFINES_roundingoff_release) $(INCLUDES_roundingoff_release) -o $@ $<

%.get_pi_windows_amd64_gnu_roundingon_debug.o: %.c
	$(CCDEP_roundingon_debug) -MM $(DEFINES_roundingon_debug) $(INCLUDES_roundingon_debug) -MT $@ -o $*.get_pi_windows_amd64_gnu_roundingon_debug.d $<
	$(CC_roundingon_debug) $(CFLAGS_roundingon_debug) $(DEFINES_roundingon_debug) $(INCLUDES_roundingon_debug) -o $@ $<

%.get_pi_windows_amd64_gnu_roundingon_release.o: %.c
	$(CCDEP_roundingon_release) -MM $(DEFINES_roundingon_release) $(INCLUDES_roundingon_release) -MT $@ -o $*.get_pi_windows_amd64_gnu_roundingon_release.d $<
	$(CC_roundingon_release) $(CFLAGS_roundingon_release) $(DEFINES_roundingon_release) $(INCLUDES_roundingon_release) -o $@ $<

CLEAN_COMMON_COMPILE_roundingoff_debug = $(addsuffix .get_pi_windows_amd64_gnu_roundingoff_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_roundingoff_release = $(addsuffix .get_pi_windows_amd64_gnu_roundingoff_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_roundingon_debug = $(addsuffix .get_pi_windows_amd64_gnu_roundingon_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_roundingon_release = $(addsuffix .get_pi_windows_amd64_gnu_roundingon_release.d,$(COMMON_FILES))
CLEAN_COMPILE_roundingoff_debug = $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingoff_debug.d
CLEAN_COMPILE_roundingoff_release = $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingoff_release.d
CLEAN_COMPILE_roundingon_debug = $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingon_debug.d
CLEAN_COMPILE_roundingon_release = $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingon_release.d

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_roundingoff_debug)
	$(RM) $(CLEAN_COMPILE_roundingoff_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingoff_release)
	$(RM) $(CLEAN_COMPILE_roundingoff_release)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingon_debug)
	$(RM) $(CLEAN_COMPILE_roundingon_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingon_release)
	$(RM) $(CLEAN_COMPILE_roundingon_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_roundingoff_debug)
	$(RM) $(CLEAN_COMPILE_roundingoff_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingoff_release)
	$(RM) $(CLEAN_COMPILE_roundingoff_release)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingon_debug)
	$(RM) $(CLEAN_COMPILE_roundingon_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_roundingon_release)
	$(RM) $(CLEAN_COMPILE_roundingon_release)
	$(RM) $(INPUTS_COMMON_LINK_roundingoff_debug)
	$(RM) $(INPUTS_LINK_roundingoff_debug)
	$(RM) $(INPUTS_COMMON_LINK_roundingon_debug)
	$(RM) $(INPUTS_LINK_roundingon_debug)
	$(RM) $(INPUTS_COMMON_LINK_roundingoff_release)
	$(RM) $(INPUTS_LINK_roundingoff_release)
	$(RM) $(INPUTS_COMMON_LINK_roundingon_release)
	$(RM) $(INPUTS_LINK_roundingon_release)
	$(RM) get_pi_roundingoff_debug.exe
	$(RM) get_pi_roundingon_debug.exe
	$(RM) get_pi_roundingoff_release.exe
	$(RM) get_pi_roundingon_release.exe

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " get_pi_roundingoff_debug.exe"
	@echo " get_pi_roundingon_debug.exe"
	@echo " get_pi_roundingoff_release.exe"
	@echo " get_pi_roundingon_release.exe"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)strip_example/get_pi/src/get_pi.get_pi_windows_amd64_gnu_roundingoff_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/main.get_pi_windows_amd64_gnu_roundingoff_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingoff_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_pi.get_pi_windows_amd64_gnu_roundingoff_release.d)
include $(wildcard $(BASE)strip_example/get_pi/src/main.get_pi_windows_amd64_gnu_roundingoff_release.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingoff_release.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_pi.get_pi_windows_amd64_gnu_roundingon_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/main.get_pi_windows_amd64_gnu_roundingon_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_flavour_debug.get_pi_windows_amd64_gnu_roundingon_debug.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_pi.get_pi_windows_amd64_gnu_roundingon_release.d)
include $(wildcard $(BASE)strip_example/get_pi/src/main.get_pi_windows_amd64_gnu_roundingon_release.d)
include $(wildcard $(BASE)strip_example/get_pi/src/get_flavour_release.get_pi_windows_amd64_gnu_roundingon_release.d)


