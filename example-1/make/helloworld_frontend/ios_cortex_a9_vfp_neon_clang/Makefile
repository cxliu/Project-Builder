#-*-makefile-*-

BASE=../../../../
CCDEP_debug = xcrun -sdk iphoneos clang -arch armv7
CCDEP_release = xcrun -sdk iphoneos clang -arch armv7
CC_debug = xcrun -sdk iphoneos clang
CC_release = xcrun -sdk iphoneos clang
CFLAGS_debug = -O0 -g -fcatch-undefined-behavior -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_release = -O3 -funroll-loops -arch armv7 -arch armv7s -fPIC -c -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_release = -DNDEBUG=1
INCLUDES_debug = -I$(BASE). -I${IPPROOT}/include
INCLUDES_release = -I$(BASE). -I${IPPROOT}/include
LDFLAGS_debug = -arch armv7 -arch armv7s
LDFLAGS_release = -O2 -arch armv7 -arch armv7s
LDLIBS_debug = -lippac_l -lipps_l -lippcore_l
LDLIBS_release = -lippac_l -lipps_l -lippcore_l
LD_debug = xcrun -sdk iphoneos clang
LD_release = xcrun -sdk iphoneos clang

COMMON_FILES = $(BASE)example-1/frontend/main

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_frontend_ios_cortex_a9_vfp_neon_clang_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_frontend_ios_cortex_a9_vfp_neon_clang_release.o,$(COMMON_FILES))

DEP_PROJ_LINK_debug = $(BASE)example-1/make/libhelloworld/ios_cortex_a9_vfp_neon_clang/libhelloworld_debug.a
DEP_PROJ_LINK_release = $(BASE)example-1/make/libhelloworld/ios_cortex_a9_vfp_neon_clang/libhelloworld_release.a

default: helloworld_frontend_debug helloworld_frontend_release

helloworld_frontend_debug: $(INPUTS_COMMON_LINK_debug) $(DEP_PROJ_LINK_debug)
	$(LD_debug) $(LDFLAGS_debug) -o  $@ $+ $(LDLIBS_debug)

helloworld_frontend_release: $(INPUTS_COMMON_LINK_release) $(DEP_PROJ_LINK_release)
	$(LD_release) $(LDFLAGS_release) -o  $@ $+ $(LDLIBS_release)

%.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_debug.o: %.c
	$(CCDEP_debug) -MM $(INCLUDES_debug) -MT $@ -o $*.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_release.o: %.c
	$(CCDEP_release) -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_frontend_ios_cortex_a9_vfp_neon_clang_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_frontend_ios_cortex_a9_vfp_neon_clang_release.d,$(COMMON_FILES))

cleandeps:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)

clean: cleanself
	$(MAKE) -C $(BASE)example-1/make/libhelloworld/ios_cortex_a9_vfp_neon_clang cleanself

cleanself:
	$(RM) $(CLEAN_COMMON_COMPILE_debug)
	$(RM) $(CLEAN_COMMON_COMPILE_release)
	$(RM) $(INPUTS_COMMON_LINK_debug)
	$(RM) $(INPUTS_COMMON_LINK_release)
	$(RM) helloworld_frontend_debug
	$(RM) helloworld_frontend_release

.PHONY: default FORCE clean cleandeps cleanself help

FORCE:

help:
	@echo "This makefile has the following targets:"
	@echo " helloworld_frontend_debug"
	@echo " helloworld_frontend_release"
	@echo " default"
	@echo " clean"
	@echo " cleandeps"
	@echo " help"

include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_frontend_ios_cortex_a9_vfp_neon_clang_release.d)

%.a: FORCE
	$(MAKE) -C $(@D) $(@F)


