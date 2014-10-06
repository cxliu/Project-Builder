#-*-makefile-*-

BASE=../../../../
CC_lower_add1_debug = icl
CC_lower_add1_release = icl
CC_lower_add2_debug = icl
CC_lower_add2_release = icl
CC_upper_add1_debug = icl
CC_upper_add1_release = icl
CC_upper_add2_debug = icl
CC_upper_add2_release = icl
CFLAGS_lower_add1_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_lower_add1_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
CFLAGS_lower_add2_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_lower_add2_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
CFLAGS_upper_add1_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_upper_add1_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
CFLAGS_upper_add2_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_upper_add2_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
DEFINES_lower_add1_debug = /DADD_THIS=1 /DGET_NAME_TRANSFORM=tolower /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_lower_add1_release = /DADD_THIS=1 /DGET_NAME_TRANSFORM=tolower /DNDEBUG=1 /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_lower_add2_debug = /DADD_THIS=2 /DGET_NAME_TRANSFORM=tolower /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_lower_add2_release = /DADD_THIS=2 /DGET_NAME_TRANSFORM=tolower /DNDEBUG=1 /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_upper_add1_debug = /DADD_THIS=1 /DGET_NAME_TRANSFORM=toupper /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_upper_add1_release = /DADD_THIS=1 /DGET_NAME_TRANSFORM=toupper /DNDEBUG=1 /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_upper_add2_debug = /DADD_THIS=2 /DGET_NAME_TRANSFORM=toupper /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
DEFINES_upper_add2_release = /DADD_THIS=2 /DGET_NAME_TRANSFORM=toupper /DNDEBUG=1 /DWIN32=1 /D_CONSOLE=1 /D_CRT_SECURE_NO_WARNINGS=1
INCLUDES_lower_add1_debug = /I$(BASE).
INCLUDES_lower_add1_release = /I$(BASE).
INCLUDES_lower_add2_debug = /I$(BASE).
INCLUDES_lower_add2_release = /I$(BASE).
INCLUDES_upper_add1_debug = /I$(BASE).
INCLUDES_upper_add1_release = /I$(BASE).
INCLUDES_upper_add2_debug = /I$(BASE).
INCLUDES_upper_add2_release = /I$(BASE).
LDFLAGS_lower_add1_debug = /DEBUG /nologo
LDFLAGS_lower_add1_release = /nologo
LDFLAGS_lower_add2_debug = /DEBUG /nologo
LDFLAGS_lower_add2_release = /nologo
LDFLAGS_upper_add1_debug = /DEBUG /nologo
LDFLAGS_upper_add1_release = /nologo
LDFLAGS_upper_add2_debug = /DEBUG /nologo
LDFLAGS_upper_add2_release = /nologo
LD_lower_add1_debug = icpc
LD_lower_add1_release = icpc
LD_lower_add2_debug = icpc
LD_lower_add2_release = icpc
LD_upper_add1_debug = icpc
LD_upper_add1_release = icpc
LD_upper_add2_debug = icpc
LD_upper_add2_release = icpc

COMMON_FILES = $(BASE)example-2/frontend/main $(BASE)example-2/src/get_name/get_name $(BASE)example-2/src/get_name/target/windows/get_name_raw

INPUTS_COMMON_LINK_lower_add1_debug = $(addsuffix .get_name_dynamic_windows_x86_icl_lower_add1_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add1_release = $(addsuffix .get_name_dynamic_windows_x86_icl_lower_add1_release.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_debug = $(addsuffix .get_name_dynamic_windows_x86_icl_lower_add2_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_release = $(addsuffix .get_name_dynamic_windows_x86_icl_lower_add2_release.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_debug = $(addsuffix .get_name_dynamic_windows_x86_icl_upper_add1_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_release = $(addsuffix .get_name_dynamic_windows_x86_icl_upper_add1_release.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_debug = $(addsuffix .get_name_dynamic_windows_x86_icl_upper_add2_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_release = $(addsuffix .get_name_dynamic_windows_x86_icl_upper_add2_release.obj,$(COMMON_FILES))

DEP_PROJ_LINK_lower_add1_debug = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add1_debug.dll
DEP_PROJ_LINK_lower_add1_release = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add1_release.dll
DEP_PROJ_LINK_lower_add2_debug = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add2_debug.dll
DEP_PROJ_LINK_lower_add2_release = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add2_release.dll
DEP_PROJ_LINK_upper_add1_debug = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add1_debug.dll
DEP_PROJ_LINK_upper_add1_release = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add1_release.dll
DEP_PROJ_LINK_upper_add2_debug = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add2_debug.dll
DEP_PROJ_LINK_upper_add2_release = $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl/libfoo_dynamic_add2_release.dll

default: get_name_dynamic_lower_add1_debug.exe get_name_dynamic_lower_add2_debug.exe get_name_dynamic_upper_add1_debug.exe get_name_dynamic_upper_add2_debug.exe get_name_dynamic_lower_add1_release.exe get_name_dynamic_lower_add2_release.exe get_name_dynamic_upper_add1_release.exe get_name_dynamic_upper_add2_release.exe

get_name_dynamic_lower_add1_debug.exe: $(INPUTS_COMMON_LINK_lower_add1_debug) $(DEP_PROJ_LINK_lower_add1_debug)
	$(LD_lower_add1_debug) $(LDFLAGS_lower_add1_debug) /OUT:$@ $^ 

get_name_dynamic_lower_add2_debug.exe: $(INPUTS_COMMON_LINK_lower_add2_debug) $(DEP_PROJ_LINK_lower_add2_debug)
	$(LD_lower_add2_debug) $(LDFLAGS_lower_add2_debug) /OUT:$@ $^ 

get_name_dynamic_upper_add1_debug.exe: $(INPUTS_COMMON_LINK_upper_add1_debug) $(DEP_PROJ_LINK_upper_add1_debug)
	$(LD_upper_add1_debug) $(LDFLAGS_upper_add1_debug) /OUT:$@ $^ 

get_name_dynamic_upper_add2_debug.exe: $(INPUTS_COMMON_LINK_upper_add2_debug) $(DEP_PROJ_LINK_upper_add2_debug)
	$(LD_upper_add2_debug) $(LDFLAGS_upper_add2_debug) /OUT:$@ $^ 

get_name_dynamic_lower_add1_release.exe: $(INPUTS_COMMON_LINK_lower_add1_release) $(DEP_PROJ_LINK_lower_add1_release)
	$(LD_lower_add1_release) $(LDFLAGS_lower_add1_release) /OUT:$@ $^ 

get_name_dynamic_lower_add2_release.exe: $(INPUTS_COMMON_LINK_lower_add2_release) $(DEP_PROJ_LINK_lower_add2_release)
	$(LD_lower_add2_release) $(LDFLAGS_lower_add2_release) /OUT:$@ $^ 

get_name_dynamic_upper_add1_release.exe: $(INPUTS_COMMON_LINK_upper_add1_release) $(DEP_PROJ_LINK_upper_add1_release)
	$(LD_upper_add1_release) $(LDFLAGS_upper_add1_release) /OUT:$@ $^ 

get_name_dynamic_upper_add2_release.exe: $(INPUTS_COMMON_LINK_upper_add2_release) $(DEP_PROJ_LINK_upper_add2_release)
	$(LD_upper_add2_release) $(LDFLAGS_upper_add2_release) /OUT:$@ $^ 

%.get_name_dynamic_windows_x86_icl_lower_add1_debug.obj: %.c
	$(CC_lower_add1_debug) $(CFLAGS_lower_add1_debug) $(DEFINES_lower_add1_debug) $(INCLUDES_lower_add1_debug) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_lower_add1_release.obj: %.c
	$(CC_lower_add1_release) $(CFLAGS_lower_add1_release) $(DEFINES_lower_add1_release) $(INCLUDES_lower_add1_release) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_lower_add2_debug.obj: %.c
	$(CC_lower_add2_debug) $(CFLAGS_lower_add2_debug) $(DEFINES_lower_add2_debug) $(INCLUDES_lower_add2_debug) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_lower_add2_release.obj: %.c
	$(CC_lower_add2_release) $(CFLAGS_lower_add2_release) $(DEFINES_lower_add2_release) $(INCLUDES_lower_add2_release) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_upper_add1_debug.obj: %.c
	$(CC_upper_add1_debug) $(CFLAGS_upper_add1_debug) $(DEFINES_upper_add1_debug) $(INCLUDES_upper_add1_debug) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_upper_add1_release.obj: %.c
	$(CC_upper_add1_release) $(CFLAGS_upper_add1_release) $(DEFINES_upper_add1_release) $(INCLUDES_upper_add1_release) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_upper_add2_debug.obj: %.c
	$(CC_upper_add2_debug) $(CFLAGS_upper_add2_debug) $(DEFINES_upper_add2_debug) $(INCLUDES_upper_add2_debug) /Fo$@ $<

%.get_name_dynamic_windows_x86_icl_upper_add2_release.obj: %.c
	$(CC_upper_add2_release) $(CFLAGS_upper_add2_release) $(DEFINES_upper_add2_release) $(INCLUDES_upper_add2_release) /Fo$@ $<


clean: cleanself
	$(MAKE) -C $(BASE)example-2/make/libfoo_dynamic/windows_x86_icl cleanself

cleanself:
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_release)
	$(RM) get_name_dynamic_lower_add1_debug.exe
	$(RM) get_name_dynamic_lower_add2_debug.exe
	$(RM) get_name_dynamic_upper_add1_debug.exe
	$(RM) get_name_dynamic_upper_add2_debug.exe
	$(RM) get_name_dynamic_lower_add1_release.exe
	$(RM) get_name_dynamic_lower_add2_release.exe
	$(RM) get_name_dynamic_upper_add1_release.exe
	$(RM) get_name_dynamic_upper_add2_release.exe

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " get_name_dynamic_lower_add1_debug.exe"
	@echo " get_name_dynamic_lower_add2_debug.exe"
	@echo " get_name_dynamic_upper_add1_debug.exe"
	@echo " get_name_dynamic_upper_add2_debug.exe"
	@echo " get_name_dynamic_lower_add1_release.exe"
	@echo " get_name_dynamic_lower_add2_release.exe"
	@echo " get_name_dynamic_upper_add1_release.exe"
	@echo " get_name_dynamic_upper_add2_release.exe"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"


%.dll: FORCE
	$(MAKE) -C $(@D) $(@F)


