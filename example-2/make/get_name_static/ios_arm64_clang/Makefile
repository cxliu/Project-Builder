#-*-makefile-*-

BASE=../../../../
CCDEP_lower_add1_debug = xcrun -sdk iphoneos clang -arch arm64
CCDEP_lower_add1_release = xcrun -sdk iphoneos clang -arch arm64
CCDEP_lower_add2_debug = xcrun -sdk iphoneos clang -arch arm64
CCDEP_lower_add2_release = xcrun -sdk iphoneos clang -arch arm64
CCDEP_upper_add1_debug = xcrun -sdk iphoneos clang -arch arm64
CCDEP_upper_add1_release = xcrun -sdk iphoneos clang -arch arm64
CCDEP_upper_add2_debug = xcrun -sdk iphoneos clang -arch arm64
CCDEP_upper_add2_release = xcrun -sdk iphoneos clang -arch arm64
CC_lower_add1_debug = xcrun -sdk iphoneos clang
CC_lower_add1_release = xcrun -sdk iphoneos clang
CC_lower_add2_debug = xcrun -sdk iphoneos clang
CC_lower_add2_release = xcrun -sdk iphoneos clang
CC_upper_add1_debug = xcrun -sdk iphoneos clang
CC_upper_add1_release = xcrun -sdk iphoneos clang
CC_upper_add2_debug = xcrun -sdk iphoneos clang
CC_upper_add2_release = xcrun -sdk iphoneos clang
CFLAGS_lower_add1_debug = -g -O0 -fcatch-undefined-behavior -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_lower_add1_release = -O3 -funroll-loops -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_lower_add2_debug = -g -O0 -fcatch-undefined-behavior -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_lower_add2_release = -O3 -funroll-loops -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_upper_add1_debug = -g -O0 -fcatch-undefined-behavior -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_upper_add1_release = -O3 -funroll-loops -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_upper_add2_debug = -g -O0 -fcatch-undefined-behavior -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_upper_add2_release = -O3 -funroll-loops -arch armv7 -arch armv7s -arch arm64 -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_lower_add1_debug = -DADD_THIS=1 -DGET_NAME_TRANSFORM=tolower
DEFINES_lower_add1_release = -DADD_THIS=1 -DGET_NAME_TRANSFORM=tolower -DNDEBUG=1
DEFINES_lower_add2_debug = -DADD_THIS=2 -DGET_NAME_TRANSFORM=tolower
DEFINES_lower_add2_release = -DADD_THIS=2 -DGET_NAME_TRANSFORM=tolower -DNDEBUG=1
DEFINES_upper_add1_debug = -DADD_THIS=1 -DGET_NAME_TRANSFORM=toupper
DEFINES_upper_add1_release = -DADD_THIS=1 -DGET_NAME_TRANSFORM=toupper -DNDEBUG=1
DEFINES_upper_add2_debug = -DADD_THIS=2 -DGET_NAME_TRANSFORM=toupper
DEFINES_upper_add2_release = -DADD_THIS=2 -DGET_NAME_TRANSFORM=toupper -DNDEBUG=1
INCLUDES_lower_add1_debug = -I$(BASE).
INCLUDES_lower_add1_release = -I$(BASE).
INCLUDES_lower_add2_debug = -I$(BASE).
INCLUDES_lower_add2_release = -I$(BASE).
INCLUDES_upper_add1_debug = -I$(BASE).
INCLUDES_upper_add1_release = -I$(BASE).
INCLUDES_upper_add2_debug = -I$(BASE).
INCLUDES_upper_add2_release = -I$(BASE).
LDFLAGS_lower_add1_debug = -arch armv7 -arch armv7s -arch arm64
LDFLAGS_lower_add1_release = -O2 -arch armv7 -arch armv7s -arch arm64
LDFLAGS_lower_add2_debug = -arch armv7 -arch armv7s -arch arm64
LDFLAGS_lower_add2_release = -O2 -arch armv7 -arch armv7s -arch arm64
LDFLAGS_upper_add1_debug = -arch armv7 -arch armv7s -arch arm64
LDFLAGS_upper_add1_release = -O2 -arch armv7 -arch armv7s -arch arm64
LDFLAGS_upper_add2_debug = -arch armv7 -arch armv7s -arch arm64
LDFLAGS_upper_add2_release = -O2 -arch armv7 -arch armv7s -arch arm64
LD_lower_add1_debug = xcrun -sdk iphoneos clang++
LD_lower_add1_release = xcrun -sdk iphoneos clang++
LD_lower_add2_debug = xcrun -sdk iphoneos clang++
LD_lower_add2_release = xcrun -sdk iphoneos clang++
LD_upper_add1_debug = xcrun -sdk iphoneos clang++
LD_upper_add1_release = xcrun -sdk iphoneos clang++
LD_upper_add2_debug = xcrun -sdk iphoneos clang++
LD_upper_add2_release = xcrun -sdk iphoneos clang++

COMMON_FILES = $(BASE)example-2/frontend/main $(BASE)example-2/src/get_name/get_name $(BASE)example-2/src/get_name/get_name_raw

INPUTS_COMMON_LINK_lower_add1_debug = $(addsuffix .get_name_static_ios_arm64_clang_lower_add1_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add1_release = $(addsuffix .get_name_static_ios_arm64_clang_lower_add1_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_debug = $(addsuffix .get_name_static_ios_arm64_clang_lower_add2_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_lower_add2_release = $(addsuffix .get_name_static_ios_arm64_clang_lower_add2_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_debug = $(addsuffix .get_name_static_ios_arm64_clang_upper_add1_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add1_release = $(addsuffix .get_name_static_ios_arm64_clang_upper_add1_release.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_debug = $(addsuffix .get_name_static_ios_arm64_clang_upper_add2_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_upper_add2_release = $(addsuffix .get_name_static_ios_arm64_clang_upper_add2_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_lower_add1_debug = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add1_debug.a
DEP_PROJ_LINK_lower_add1_release = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add1_release.a
DEP_PROJ_LINK_lower_add2_debug = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add2_debug.a
DEP_PROJ_LINK_lower_add2_release = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add2_release.a
DEP_PROJ_LINK_upper_add1_debug = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add1_debug.a
DEP_PROJ_LINK_upper_add1_release = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add1_release.a
DEP_PROJ_LINK_upper_add2_debug = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add2_debug.a
DEP_PROJ_LINK_upper_add2_release = $(BASE)example-2/make/libfoo_static/ios_arm64_clang/libfoo_static_add2_release.a

default: get_name_static_lower_add1_debug get_name_static_lower_add2_debug get_name_static_upper_add1_debug get_name_static_upper_add2_debug get_name_static_lower_add1_release get_name_static_lower_add2_release get_name_static_upper_add1_release get_name_static_upper_add2_release

get_name_static_lower_add1_debug: $(INPUTS_COMMON_LINK_lower_add1_debug) $(DEP_PROJ_LINK_lower_add1_debug)
	$(LD_lower_add1_debug) $(LDFLAGS_lower_add1_debug) -o $@ $+ 

get_name_static_lower_add2_debug: $(INPUTS_COMMON_LINK_lower_add2_debug) $(DEP_PROJ_LINK_lower_add2_debug)
	$(LD_lower_add2_debug) $(LDFLAGS_lower_add2_debug) -o $@ $+ 

get_name_static_upper_add1_debug: $(INPUTS_COMMON_LINK_upper_add1_debug) $(DEP_PROJ_LINK_upper_add1_debug)
	$(LD_upper_add1_debug) $(LDFLAGS_upper_add1_debug) -o $@ $+ 

get_name_static_upper_add2_debug: $(INPUTS_COMMON_LINK_upper_add2_debug) $(DEP_PROJ_LINK_upper_add2_debug)
	$(LD_upper_add2_debug) $(LDFLAGS_upper_add2_debug) -o $@ $+ 

get_name_static_lower_add1_release: $(INPUTS_COMMON_LINK_lower_add1_release) $(DEP_PROJ_LINK_lower_add1_release)
	$(LD_lower_add1_release) $(LDFLAGS_lower_add1_release) -o $@ $+ 

get_name_static_lower_add2_release: $(INPUTS_COMMON_LINK_lower_add2_release) $(DEP_PROJ_LINK_lower_add2_release)
	$(LD_lower_add2_release) $(LDFLAGS_lower_add2_release) -o $@ $+ 

get_name_static_upper_add1_release: $(INPUTS_COMMON_LINK_upper_add1_release) $(DEP_PROJ_LINK_upper_add1_release)
	$(LD_upper_add1_release) $(LDFLAGS_upper_add1_release) -o $@ $+ 

get_name_static_upper_add2_release: $(INPUTS_COMMON_LINK_upper_add2_release) $(DEP_PROJ_LINK_upper_add2_release)
	$(LD_upper_add2_release) $(LDFLAGS_upper_add2_release) -o $@ $+ 

%.get_name_static_ios_arm64_clang_lower_add1_debug.o: %.c
	$(CCDEP_lower_add1_debug) -MM $(DEFINES_lower_add1_debug) $(INCLUDES_lower_add1_debug) -MT $@ -o $*.get_name_static_ios_arm64_clang_lower_add1_debug.d $<
	$(CC_lower_add1_debug) $(CFLAGS_lower_add1_debug) $(DEFINES_lower_add1_debug) $(INCLUDES_lower_add1_debug) -o $@ $<

%.get_name_static_ios_arm64_clang_lower_add1_release.o: %.c
	$(CCDEP_lower_add1_release) -MM $(DEFINES_lower_add1_release) $(INCLUDES_lower_add1_release) -MT $@ -o $*.get_name_static_ios_arm64_clang_lower_add1_release.d $<
	$(CC_lower_add1_release) $(CFLAGS_lower_add1_release) $(DEFINES_lower_add1_release) $(INCLUDES_lower_add1_release) -o $@ $<

%.get_name_static_ios_arm64_clang_lower_add2_debug.o: %.c
	$(CCDEP_lower_add2_debug) -MM $(DEFINES_lower_add2_debug) $(INCLUDES_lower_add2_debug) -MT $@ -o $*.get_name_static_ios_arm64_clang_lower_add2_debug.d $<
	$(CC_lower_add2_debug) $(CFLAGS_lower_add2_debug) $(DEFINES_lower_add2_debug) $(INCLUDES_lower_add2_debug) -o $@ $<

%.get_name_static_ios_arm64_clang_lower_add2_release.o: %.c
	$(CCDEP_lower_add2_release) -MM $(DEFINES_lower_add2_release) $(INCLUDES_lower_add2_release) -MT $@ -o $*.get_name_static_ios_arm64_clang_lower_add2_release.d $<
	$(CC_lower_add2_release) $(CFLAGS_lower_add2_release) $(DEFINES_lower_add2_release) $(INCLUDES_lower_add2_release) -o $@ $<

%.get_name_static_ios_arm64_clang_upper_add1_debug.o: %.c
	$(CCDEP_upper_add1_debug) -MM $(DEFINES_upper_add1_debug) $(INCLUDES_upper_add1_debug) -MT $@ -o $*.get_name_static_ios_arm64_clang_upper_add1_debug.d $<
	$(CC_upper_add1_debug) $(CFLAGS_upper_add1_debug) $(DEFINES_upper_add1_debug) $(INCLUDES_upper_add1_debug) -o $@ $<

%.get_name_static_ios_arm64_clang_upper_add1_release.o: %.c
	$(CCDEP_upper_add1_release) -MM $(DEFINES_upper_add1_release) $(INCLUDES_upper_add1_release) -MT $@ -o $*.get_name_static_ios_arm64_clang_upper_add1_release.d $<
	$(CC_upper_add1_release) $(CFLAGS_upper_add1_release) $(DEFINES_upper_add1_release) $(INCLUDES_upper_add1_release) -o $@ $<

%.get_name_static_ios_arm64_clang_upper_add2_debug.o: %.c
	$(CCDEP_upper_add2_debug) -MM $(DEFINES_upper_add2_debug) $(INCLUDES_upper_add2_debug) -MT $@ -o $*.get_name_static_ios_arm64_clang_upper_add2_debug.d $<
	$(CC_upper_add2_debug) $(CFLAGS_upper_add2_debug) $(DEFINES_upper_add2_debug) $(INCLUDES_upper_add2_debug) -o $@ $<

%.get_name_static_ios_arm64_clang_upper_add2_release.o: %.c
	$(CCDEP_upper_add2_release) -MM $(DEFINES_upper_add2_release) $(INCLUDES_upper_add2_release) -MT $@ -o $*.get_name_static_ios_arm64_clang_upper_add2_release.d $<
	$(CC_upper_add2_release) $(CFLAGS_upper_add2_release) $(DEFINES_upper_add2_release) $(INCLUDES_upper_add2_release) -o $@ $<

CLEAN_COMMON_COMPILE_lower_add1_debug = $(addsuffix .get_name_static_ios_arm64_clang_lower_add1_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add1_release = $(addsuffix .get_name_static_ios_arm64_clang_lower_add1_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add2_debug = $(addsuffix .get_name_static_ios_arm64_clang_lower_add2_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_lower_add2_release = $(addsuffix .get_name_static_ios_arm64_clang_lower_add2_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add1_debug = $(addsuffix .get_name_static_ios_arm64_clang_upper_add1_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add1_release = $(addsuffix .get_name_static_ios_arm64_clang_upper_add1_release.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add2_debug = $(addsuffix .get_name_static_ios_arm64_clang_upper_add2_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_upper_add2_release = $(addsuffix .get_name_static_ios_arm64_clang_upper_add2_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-2/make/libfoo_static/ios_arm64_clang cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_lower_add2_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add1_release)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_upper_add2_release)
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_debug)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_debug)
	$(RM) $(INPUTS_COMMON_LINK_lower_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_lower_add2_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add1_release)
	$(RM) $(INPUTS_COMMON_LINK_upper_add2_release)
	$(RM) get_name_static_lower_add1_debug
	$(RM) get_name_static_lower_add2_debug
	$(RM) get_name_static_upper_add1_debug
	$(RM) get_name_static_upper_add2_debug
	$(RM) get_name_static_lower_add1_release
	$(RM) get_name_static_lower_add2_release
	$(RM) get_name_static_upper_add1_release
	$(RM) get_name_static_upper_add2_release

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " get_name_static_lower_add1_debug"
	@echo " get_name_static_lower_add2_debug"
	@echo " get_name_static_upper_add1_debug"
	@echo " get_name_static_upper_add2_debug"
	@echo " get_name_static_lower_add1_release"
	@echo " get_name_static_lower_add2_release"
	@echo " get_name_static_upper_add1_release"
	@echo " get_name_static_upper_add2_release"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_lower_add1_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_lower_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_lower_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_lower_add1_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_lower_add2_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_lower_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_lower_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_lower_add2_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_upper_add1_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_upper_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_upper_add1_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_upper_add1_release.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_upper_add2_debug.d)
include $(wildcard $(BASE)example-2/frontend/main.get_name_static_ios_arm64_clang_upper_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name.get_name_static_ios_arm64_clang_upper_add2_release.d)
include $(wildcard $(BASE)example-2/src/get_name/get_name_raw.get_name_static_ios_arm64_clang_upper_add2_release.d)

%.a: FORCE
	$(MAKE) -C $(@D) $(@F)


