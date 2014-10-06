#-*-makefile-*-

BASE=../../../../
ARFLAGS_add1_debug = /nologo
ARFLAGS_add1_release = /nologo
ARFLAGS_add2_debug = /nologo
ARFLAGS_add2_release = /nologo
AR_add1_debug = xilib
AR_add1_release = xilib
AR_add2_debug = xilib
AR_add2_release = xilib
CC_add1_debug = icl
CC_add1_release = icl
CC_add2_debug = icl
CC_add2_release = icl
CFLAGS_add1_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_add1_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
CFLAGS_add2_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_add2_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
CXXFLAGS_add1_debug = /c /W3 /nologo /Qstd=c++0x /Od /Zi
CXXFLAGS_add1_release = /c /W3 /nologo /Qstd=c++0x /O3 /Qunroll /Qansi-alias
CXXFLAGS_add2_debug = /c /W3 /nologo /Qstd=c++0x /Od /Zi
CXXFLAGS_add2_release = /c /W3 /nologo /Qstd=c++0x /O3 /Qunroll /Qansi-alias
CXX_add1_debug = icpc
CXX_add1_release = icpc
CXX_add2_debug = icpc
CXX_add2_release = icpc
DEFINES_add1_debug = /DADD_THIS=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
DEFINES_add1_release = /DADD_THIS=1 /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
DEFINES_add2_debug = /DADD_THIS=2 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
DEFINES_add2_release = /DADD_THIS=2 /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
INCLUDES_add1_debug = /I$(BASE).
INCLUDES_add1_release = /I$(BASE).
INCLUDES_add2_debug = /I$(BASE).
INCLUDES_add2_release = /I$(BASE).


INPUTS_ARCHIVE_add1_debug = $(BASE)example-2/src/foo/foo.libfoo_static_windows_amd64_icl_add1_debug.obj $(BASE)example-2/src/foo/foo_asm.libfoo_static_windows_amd64_icl_add1_debug.obj\
                            $(BASE)example-2/src/foo/foo_cpp.libfoo_static_windows_amd64_icl_add1_debug.obj
INPUTS_ARCHIVE_add1_release = $(BASE)example-2/src/foo/foo.libfoo_static_windows_amd64_icl_add1_release.obj $(BASE)example-2/src/foo/foo_asm.libfoo_static_windows_amd64_icl_add1_release.obj\
                              $(BASE)example-2/src/foo/foo_cpp.libfoo_static_windows_amd64_icl_add1_release.obj
INPUTS_ARCHIVE_add2_debug = $(BASE)example-2/src/foo/foo.libfoo_static_windows_amd64_icl_add2_debug.obj $(BASE)example-2/src/foo/foo_asm.libfoo_static_windows_amd64_icl_add2_debug.obj\
                            $(BASE)example-2/src/foo/foo_cpp.libfoo_static_windows_amd64_icl_add2_debug.obj
INPUTS_ARCHIVE_add2_release = $(BASE)example-2/src/foo/foo.libfoo_static_windows_amd64_icl_add2_release.obj $(BASE)example-2/src/foo/foo_asm.libfoo_static_windows_amd64_icl_add2_release.obj\
                              $(BASE)example-2/src/foo/foo_cpp.libfoo_static_windows_amd64_icl_add2_release.obj


default: libfoo_static_add1_debug.lib libfoo_static_add2_debug.lib libfoo_static_add1_release.lib libfoo_static_add2_release.lib

libfoo_static_add1_debug.lib: $(INPUTS_ARCHIVE_add1_debug)
	$(AR_add1_debug) $(ARFLAGS_add1_debug) /out:$@ $^

libfoo_static_add2_debug.lib: $(INPUTS_ARCHIVE_add2_debug)
	$(AR_add2_debug) $(ARFLAGS_add2_debug) /out:$@ $^

libfoo_static_add1_release.lib: $(INPUTS_ARCHIVE_add1_release)
	$(AR_add1_release) $(ARFLAGS_add1_release) /out:$@ $^

libfoo_static_add2_release.lib: $(INPUTS_ARCHIVE_add2_release)
	$(AR_add2_release) $(ARFLAGS_add2_release) /out:$@ $^

%.libfoo_static_windows_amd64_icl_add1_debug.obj: %.c
	$(CC_add1_debug) $(CFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add1_debug.obj: %.cpp
	$(CXX_add1_debug) $(CXXFLAGS_add1_debug) $(DEFINES_add1_debug) $(INCLUDES_add1_debug) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add1_release.obj: %.c
	$(CC_add1_release) $(CFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add1_release.obj: %.cpp
	$(CXX_add1_release) $(CXXFLAGS_add1_release) $(DEFINES_add1_release) $(INCLUDES_add1_release) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add2_debug.obj: %.c
	$(CC_add2_debug) $(CFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add2_debug.obj: %.cpp
	$(CXX_add2_debug) $(CXXFLAGS_add2_debug) $(DEFINES_add2_debug) $(INCLUDES_add2_debug) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add2_release.obj: %.c
	$(CC_add2_release) $(CFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) /Fo$@ $<

%.libfoo_static_windows_amd64_icl_add2_release.obj: %.cpp
	$(CXX_add2_release) $(CXXFLAGS_add2_release) $(DEFINES_add2_release) $(INCLUDES_add2_release) /Fo$@ $<


clean: cleanself

cleanself:
	$(RM) $(INPUTS_ARCHIVE_add1_debug)
	$(RM) $(INPUTS_ARCHIVE_add2_debug)
	$(RM) $(INPUTS_ARCHIVE_add1_release)
	$(RM) $(INPUTS_ARCHIVE_add2_release)
	$(RM) libfoo_static_add1_debug.lib
	$(RM) libfoo_static_add2_debug.lib
	$(RM) libfoo_static_add1_release.lib
	$(RM) libfoo_static_add2_release.lib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libfoo_static_add1_debug.lib"
	@echo " libfoo_static_add2_debug.lib"
	@echo " libfoo_static_add1_release.lib"
	@echo " libfoo_static_add2_release.lib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"



