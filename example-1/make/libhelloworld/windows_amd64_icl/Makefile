#-*-makefile-*-

BASE=../../../../
ARFLAGS_debug = /nologo
ARFLAGS_release = /nologo
AR_debug = xilib
AR_release = xilib
CC_debug = icl
CC_release = icl
CFLAGS_debug = /c /W3 /nologo /Qstd=c99 /Od /Zi
CFLAGS_release = /c /W3 /nologo /Qstd=c99 /O3 /Qansi-alias
DEFINES_debug = /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
DEFINES_release = /DNDEBUG=1 /DWIN32=1 /DWIN64=1 /D_CRT_SECURE_NO_WARNINGS=1 /D_LIB=1
INCLUDES_debug = /I$(BASE)example-1/include
INCLUDES_release = /I$(BASE)example-1/include

COMMON_FILES = $(BASE)example-1/src/helloworld

INPUTS_COMMON_ARCHIVE_debug = $(addsuffix .libhelloworld_windows_amd64_icl_debug.obj,$(COMMON_FILES))
INPUTS_COMMON_ARCHIVE_release = $(addsuffix .libhelloworld_windows_amd64_icl_release.obj,$(COMMON_FILES))


default: libhelloworld_debug.lib libhelloworld_release.lib

libhelloworld_debug.lib: $(INPUTS_COMMON_ARCHIVE_debug)
	$(AR_debug) $(ARFLAGS_debug) /out:$@ $^

libhelloworld_release.lib: $(INPUTS_COMMON_ARCHIVE_release)
	$(AR_release) $(ARFLAGS_release) /out:$@ $^

%.libhelloworld_windows_amd64_icl_debug.obj: %.c
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) /Fo$@ $<

%.libhelloworld_windows_amd64_icl_release.obj: %.c
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) /Fo$@ $<


clean: cleanself

cleanself:
	$(RM) $(INPUTS_COMMON_ARCHIVE_debug)
	$(RM) $(INPUTS_COMMON_ARCHIVE_release)
	$(RM) libhelloworld_debug.lib
	$(RM) libhelloworld_release.lib

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " libhelloworld_debug.lib"
	@echo " libhelloworld_release.lib"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"



