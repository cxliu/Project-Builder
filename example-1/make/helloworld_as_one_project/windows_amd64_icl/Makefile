#-*-makefile-*-

BASE=../../../../
CC_debug = icl
CC_release = icl
CFLAGS_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
DEFINES_debug = /DWIN32=1 /DWIN64=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_release = /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
INCLUDES_debug = /I$(BASE)example-1/include /I$(BASE).
INCLUDES_release = /I$(BASE)example-1/include /I$(BASE).
LDFLAGS_debug = /DEBUG /nologo
LDFLAGS_release = /nologo
LD_debug = xilink
LD_release = xilink

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_windows_amd64_icl_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_windows_amd64_icl_release.obj,$(COMMON_FILES))


default: helloworld_as_one_project_debug.exe helloworld_as_one_project_release.exe

helloworld_as_one_project_debug.exe: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) /OUT:$@ $^ 

helloworld_as_one_project_release.exe: $(INPUTS_COMMON_LINK_release)
	$(LD_release) $(LDFLAGS_release) /OUT:$@ $^ 

%.helloworld_as_one_project_windows_amd64_icl_debug.obj: %.c
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) /Fo$@ $<

%.helloworld_as_one_project_windows_amd64_icl_release.obj: %.c
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) /Fo$@ $<


clean: cleanself

cleanself:
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_as_one_project_debug.exe
	$(RM) helloworld_as_one_project_release.exe

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_as_one_project_debug.exe"
	@echo " helloworld_as_one_project_release.exe"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"



