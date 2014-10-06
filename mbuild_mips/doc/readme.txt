MIPS Plugin for M-Build

Contents
--------
1. What is this?
2. What exactly does this provide?
3. How do I use it?
4. How does a customer use it?


1. What is this?
----------------
This is a plugin for M-Build which adds support for the MIPS toolchain. Only a subset of the cores that are supported by MIPS are supported here, more may be added as needed but the intent is to support just the things that are in active use. When this plugin is used, it will allow a project to say that it supports some flavours of MIPS cores, and then M-Build will generate Makefiles for these different flavours.

2. What exactly does this provide?
----------------------------------
This plugin can provide targets for MIPS builds at present. The builds will be compiled using "mips-linux-gnu-gcc" or "mips-sde-elf-gcc" in Codesourcery.

1) The supported cores were: 
        24KEf
2) The supported MIPS's tools' version were: 
        v4.7.2(2012.09-99)
3) The supported lib linkage were:
        static lib linkage
   Because the MIPS board can be configured to hard-float or soft-float. To make things simple we used 'static' linkage that we can execute the test on the board no matter the configuration of MIPS board. If you need to do qemu test, you can use the makefile in the linux_24ke* folders.

3. How do I use it?
-------------------
In your top level manifest, @import the mbuild_mips/manifest.mb file. Once you have done this, you can add MIPS support to any project by using the "mips_support" symbol in a .project file. e.g. if you had:

my_project = ProjectSpec(
	actions=mbuild_compile_and_link,
	depends=[],
	build_configs=mbuild_standard,
)

You can change this to:

my_project = ProjectSpec(
	actions=mbuild_compile_and_link,
	depends=[],
	build_configs=mbuild_union(
                    mbuild_standard,
                    mips_support,
                  ),
)

And makefiles will be generated for all of the supported MIPS cores.


4. How does a customer use it?
------------------------------
To build programs for MIPS, we require CodeSourcery "mips-linux-gnu-gcc" or "mips-sde-elf-gcc" compilers and related tools to be in your $PATH.
The newlib in mips-sde-elf-gcc tool chain needs the supports by operating system or target hardware platforms. Maybe user needs to provide or implement the functions that are needed by newlib, while the target system doesn't provide. For the details, please refer to http://www.billgatliff.com/newlib.html
