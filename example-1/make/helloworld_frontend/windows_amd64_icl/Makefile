#-*-makefile-*-

BASE=../../../../
CC_debug = icl
CC_release = icl
CFLAGS_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
DEFINES_debug = /DWIN32=1 /DWIN64=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_release = /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
INCLUDES_debug = /I$(BASE).
INCLUDES_release = /I$(BASE).
LDFLAGS_debug = /DEBUG /nologo
LDFLAGS_release = /nologo
LD_debug = xilink
LD_release = xilink

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_windows_amd64_icl_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_windows_amd64_icl_release.obj,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/windows_amd64_icl/libhelloworld_debug.lib
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/windows_amd64_icl/libhelloworld_release.lib

default: helloworld_frontend_debug.exe helloworld_frontend_release.exe

helloworld_frontend_debug.exe: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) /OUT:$@ $^ 

helloworld_frontend_release.exe: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) /OUT:$@ $^ 

%.helloworld_frontend_windows_amd64_icl_debug.obj: %.c
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) /Fo$@ $<

%.helloworld_frontend_windows_amd64_icl_release.obj: %.c
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) /Fo$@ $<


clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/windows_amd64_icl cleanself

cleanself:
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


%.lib: FORCE
	$(MAKE) -C $(@D) $(@F)


