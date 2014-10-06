#-*-makefile-*-

BASE=../../../../
CCDEP_debug = arm-linux-androideabi-gcc
CCDEP_release = arm-linux-androideabi-gcc
CC_debug = arm-linux-androideabi-gcc
CC_release = arm-linux-androideabi-gcc
CFLAGS_debug = -march=armv7-a -mfloat-abi=softfp -mfpu=neon -mthumb -g -O0 -c -Wall -pedantic -std=gnu99 -Wno-overlength-strings
CFLAGS_release = -march=armv7-a -mfloat-abi=softfp -mfpu=neon -mthumb -O3 -funroll-loops -c -Wall -pedantic -std=gnu99 -Wno-overlength-strings
DEFINES_debug = -DANDROID=1
DEFINES_release = -DANDROID=1 -DNDEBUG=1
INCLUDES_debug = -I$(BASE)example-1/include -I$(BASE).
INCLUDES_release = -I$(BASE)example-1/include -I$(BASE).
LDLIBS_debug = -lm
LDLIBS_release = -lm
LD_debug = arm-linux-androideabi-gcc
LD_release = arm-linux-androideabi-gcc

COMMON_FILES = $(BASE)example-1/frontend/main $(BASE)example-1/src/helloworld

INPUTS_COMMON_LINK_debug = $(addsuffix .helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.o,$(COMMON_FILES))
INPUTS_COMMON_LINK_release = $(addsuffix .helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.o,$(COMMON_FILES))


default: helloworld_as_one_project_debug helloworld_as_one_project_release

helloworld_as_one_project_debug: $(INPUTS_COMMON_LINK_debug)
	$(LD_debug) -o $@ $+ $(LDLIBS_debug)

helloworld_as_one_project_release: $(INPUTS_COMMON_LINK_release)
	$(LD_release) -o $@ $+ $(LDLIBS_release)

%.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.o: %.c
	$(CCDEP_debug) -march=armv7-a -mfloat-abi=softfp -mfpu=neon -mthumb -MM $(DEFINES_debug) $(INCLUDES_debug) -MT $@ -o $*.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.d $<
	$(CC_debug) $(CFLAGS_debug) $(DEFINES_debug) $(INCLUDES_debug) -o $@ $<

%.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.o: %.c
	$(CCDEP_release) -march=armv7-a -mfloat-abi=softfp -mfpu=neon -mthumb -MM $(DEFINES_release) $(INCLUDES_release) -MT $@ -o $*.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.d $<
	$(CC_release) $(CFLAGS_release) $(DEFINES_release) $(INCLUDES_release) -o $@ $<

CLEAN_COMMON_COMPILE_debug = $(addsuffix .helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.d,$(COMMON_FILES))
CLEAN_COMMON_COMPILE_release = $(addsuffix .helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.d,$(COMMON_FILES))

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

include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_debug.d)
include $(wildcard $(BASE)example-1/frontend/main.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.d)
include $(wildcard $(BASE)example-1/src/helloworld.helloworld_as_one_project_android_cortex_a9_vfp_neon_t2_androideabi_gnu_release.d)


