#-*-makefile-*-

BASE=../../../../
CC_add1_debug = icl
CC_add1_release = icl
CC_add2_debug = icl
CC_add2_release = icl
CFLAGS_add1_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi /LDd
CFLAGS_add1_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias /LD
CFLAGS_add2_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi /LDd
CFLAGS_add2_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias /LD
CXXFLAGS_add1_debug = /c /W3 /nologo /Qstd=c++0x /Od /Zi /LDd
CXXFLAGS_add1_release = /c /W3 /nologo /Qstd=c++0x /O3 /Qunroll /Qansi-alias /LD
CXXFLAGS_add2_debug = /c /W3 /nologo /Qstd=c++0x /Od /Zi /LDd
CXXFLAGS_add2_release = /c /W3 /nologo /Qstd=c++0x /O3 /Qunroll /Qansi-alias /LD
CXX_add1_debug = icpc
CXX_add1_release = icpc
CXX_add2_debug = icpc
CXX_add2_release = icpc
DEFINES_add1_debug = /DADD_THIS=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_USRDLL=1 /D_WINDOWS=1
DEFINES_add1_release = /DADD_THIS=1 /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_USRDLL=1 /D_WINDOWS=1
DEFINES_add2_debug = /DADD_THIS=2 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_USRDLL=1 /D_WINDOWS=1
DEFINES_add2_release = /DADD_THIS=2 /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_USRDLL=1 /D_WINDOWS=1
INCLUDES_add1_debug = /I$(BASE).
INCLUDES_add1_release = /I$(BASE).
INCLUDES_add2_debug = /I$(BASE).
INCLUDES_add2_release = /I$(BASE).
LDFLAGS_add1_debug = /DEBUG /DLL /nologo
LDFLAGS_add1_release = /DLL /nologo
LDFLAGS_add2_debug = /DEBUG /DLL /nologo
LDFLAGS_add2_release = /DLL /nologo
LD_add1_debug = xilink
LD_add1_release = xilink
LD_add2_debug = xilink
LD_add2_release = xilink


INPUTS_LINK_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_amd64_icl_add1_debug.obj $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_amd64_icl_add1_debug.obj\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_amd64_icl_add1_debug.obj
INPUTS_LINK_add1_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_amd64_icl_add1_release.obj $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_amd64_icl_add1_release.obj\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_amd64_icl_add1_release.obj
INPUTS_LINK_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_amd64_icl_add2_debug.obj $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_amd64_icl_add2_debug.obj\
                         $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_amd64_icl_add2_debug.obj
INPUTS_LINK_add2_release = $(BASE)example-2/src/foo/foo.libfoo_dynamic_windows_amd64_icl_add2_release.obj $(BASE)example-2/src/foo/foo_asm.libfoo_dynamic_windows_amd64_icl_add2_release.obj\
                           $(BASE)example-2/src/foo/foo_cpp.libfoo_dynamic_windows_amd64_icl_add2_release.obj


default: libfoo_dynamic_add1_debug.dll libfoo_dynamic_add2_debug.dll libfoo_dynamic_add1_release.dll libfoo_dynamic_add2_release.dll

libfoo_dynamic_add1_debug.dll: $(INPUTS_LINK_add1_debug)
	$(LD_add1_debug) $(LDFLAGS_add1_debug) /OUT:$@ $^ 

libfoo_dynamic_add2_debug.dll: $(INPUTS_LINK_add2_debug)
	$(LD_add2_debug) $(LDFLAGS_add2_debug) /OUT:$@ $^ 

libfoo_dynamic_add1_release.dll: $(INPUTS_LINK_add1_release)
	$(LD_add1_release) $(LDFLAGS_add1_release) /OUT:$@ $^ 

libfoo_dynamic_add2_release.dll: $(INPUTS_LINK_add2_release)
	$(LD_add2_release) $(LDFLAGS_add2_release) /OUT:$@ $^ 

%.libfoo_dynamic_windows_amd64_icl_add1_debug.obj: %.c
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add1_debug.obj: %.cpp
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add1_release.obj: %.c
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add1_release.obj: %.cpp
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add2_debug.obj: %.c
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add2_debug.obj: %.cpp
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add2_release.obj: %.c
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) /Fo$@ $<

%.libfoo_dynamic_windows_amd64_icl_add2_release.obj: %.cpp
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) /Fo$@ $<


clean: cleanself

cleanself:
	$(RM) $(INPUTS_LINK_add1_debug)
	$(RM) $(INPUTS_LINK_add2_debug)
	$(RM) $(INPUTS_LINK_add1_release)
	$(RM) $(INPUTS_LINK_add2_release)
	$(RM) libfoo_dynamic_add1_debug.dll
	$(RM) libfoo_dynamic_add2_debug.dll
	$(RM) libfoo_dynamic_add1_release.dll
	$(RM) libfoo_dynamic_add2_release.dll

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_dynamic_add1_debug.dll"
	@echo " libfoo_dynamic_add2_debug.dll"
	@echo " libfoo_dynamic_add1_release.dll"
	@echo " libfoo_dynamic_add2_release.dll"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"



