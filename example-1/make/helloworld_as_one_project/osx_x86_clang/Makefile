#-*-makefile-*-

BASE=../../../../
CCDEP_debug = xcrun clang
CCDEP_release = xcrun clang
CC_debug = xcrun clang
CC_release = xcrun clang
CFLAGS_debug = -g -O0 -fcatch-undefined-behavior -arch i386 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_release = -O3 -funroll-loops -arch i386 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_release = -I$(BASE)example-1/include -I$(BASE).
LDFLAGS_debug = -arch i386
LDFLAGS_release = -O2 -arch i386
LDLIBS_debug = -lm
LDLIBS_release = -lm
LD_debug = xcrun clang
LD_release = xcrun clang

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_osx_x86_clang_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_osx_x86_clang_release.o,$(COMMON_FILES))


default: helloworld_as_one_project_debug helloworld_as_one_project_release

helloworld_as_one_project_debug: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o $@ $+ $(LDLIBS_debug)

helloworld_as_one_project_release: $(INPUTS_COMMON_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o $@ $+ $(LDLIBS_release)

%.helloworld_as_one_project_osx_x86_clang_debug.o: %.c
	$(CCDEP_debug) -MM $(INCLUDES_debug) -MT $@ -o $*.helloworld_as_one_project_osx_x86_clang_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_as_one_project_osx_x86_clang_release.o: %.c
	$(CCDEP_release) -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.helloworld_as_one_project_osx_x86_clang_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_as_one_project_osx_x86_clang_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_as_one_project_osx_x86_clang_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_as_one_project_debug
	$(RM) helloworld_as_one_project_release

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_as_one_project_debug"
	@echo " helloworld_as_one_project_release"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_osx_x86_clang_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_osx_x86_clang_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_osx_x86_clang_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_osx_x86_clang_release.d)


