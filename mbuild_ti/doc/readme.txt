TI Plugin for M-Build

Contents
--------
1. What is this?
2. What exactly does this provide?
3. How do I use it?
4. How does a customer use it?


1. What is this?
----------------
This is a plugin for M-Build which adds support for the TI C6x(+) toolchain. Only a subset of the cores that are supported by TI CCS are supported here, more may be added as needed but the intent is to support just the things that are in active use. When this plugin is used, it will allow a project to say that it supports some flavours of TI C6x(+) cores, and then M-Build will generate Makefiles for these different flavours.

2. What exactly does this provide?
----------------------------------
This plugin can provide targets for TI C6x builds at present. The builds will be compiled using "cl6x" and linked using "lnk6x" from TI's CGT(Code Generation Tools) or CCS.

1) The supported cores were: 
        c64, c64plus
        c67, c67plus
        c674,
        c66
2) The supported TI's CGT were: 
        v7 (Tested with v7.2.2 and v7.4.2)
        v6 (Tested with v6.0.13)
3) The supported bin format(abi) were:
        coffabi
        eabi(conditional, see details in section 4, topic DSPLIB)

3. How do I use it?
-------------------
In your top level manifest, @import the mbuild_ti/manifest.mb file. Once you have done this, you can add TI support to any project by using the "ti_support" symbol in a .project file. e.g. if you had:

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
                    ti_support,
                  ),
)

And makefiles will be generated for all of the supported TI C64x(+) cores.


4. How does a customer use it?
------------------------------
1) **** CGT(toolchain) ****
To build programs for TI C6x, we require cl6x compiler and related tools to be in your $PATH.
You also need to set the environment variable C6X_C_DIR correctly. It should include the path of CGT's header files and libraries. It might include the path of TI's dsplib file as well.
One example:

% export C6X_C_DIR="/data/soft/Linux/opt/TI/C6000CGT7.2.2/include;/data/soft/Linux/opt/TI/C6000CGT7.2.2/lib"
% export C6X_C_DIR="/data/soft/Linux/opt/TI/dsplib_dir;$C6X_C_DIR"
% export C6X_C_DIR="/data/soft/Linux/opt/TI/fastmathlib/lib;$C6X_C_DIR"

One thing needs your attention: to separate the paths in C6X_C_DIR, use use ; (semicolon) not : (colon). It's different with setting PATH environment variable under Linux.


2) **** CMD file ****
TI's linking command files is used to pass options and arguments to linker(of cource you can also pass them by command line) and tell the linker about the memory layout of your target platform.
In mbuild_ti, 
1) you can use a default cmd file included in mbuild_ti(mbuild_ti/resource/c64pluslnkx.cmd, it can be used for all cores supported in mbuild_ti, on TI's simulator), or
2) you can provide a custom cmd file, which includes all link options and arguments. (It's highly recommended to use this method.)
    
However, you need to set the TI_LINK_COMMAND_FILE environment variable to point to it.

% export TI_LINK_COMMAND_FILE=somewhere/foo.cmd


3) **** EABI(ELF based ABI) ****
TI's C6000 compilers earlier than version 7.2.x support only one ABI, called COFF ABI. Starting with compiler release v7.2.x, the C6000 compiler continues to support COFF ABI, but also supports a new ABI named EABI via the build option --abi=eabi.*
Mbuild_ti supports both of COFFABI and EABI. By default, it will generate Makefiles individually for these two ABIs. For example, they will be put at /tisim_coffabi_c64 and /tisim_eabi_c64 for TI C64. 


4) **** DSPLIB ****
a) Keywords need to be added
By default, mbuild_ti won't link TI dsplib. If you want to call some functions in the TI dsplib, add these keywords in your manifest.mb:
    @add ti_dsplib_c64_style   ==> means to link TI's C64 or C64plus (fixed-point) dsplib
    @add ti_dsplib_c67_style   ==> means to link TI's C67 or C67plus (floating-point) dsplib
    @add ti_dsplib_c674_style  ==> means to link TI's C674 (floating-point) dsplib
In addition, to distinguish between plain C64 and C64plus on C64plus and C674 platform (similar for C67/C67plus), mbuild_ti will check which of following keywords has been added/defined:
    @add ti_non_plus_core    ==> ISA of non-plus processor will be used (C64 or C67)
    @add ti_plus_core        ==> ISA of plus processor will be used (C64+ or C67+)
User should define them in their manifest.mb. Then mbuild_ti will choose right ones to link.

So,
    to link C64     dsplib (even on C64plus and C674 platform), you need to add keywords "ti_dsplib_c64_style" and "ti_non_plus_core";
    to link C64plus dsplib (even on             C674 platform), you need to add keywords "ti_dsplib_c64_style" and "ti_plus_core";
    to link C67     dsplib (even on C67plus and C674 platform), you need to add keywords "ti_dsplib_c67_style" and "ti_non_plus_core";
    to link C67plus dsplib (even on             C674 platform), you need to add keywords "ti_dsplib_c67_style" and "ti_plus_core".

b) The naming of DSPLIB
TI provides several versions of dsplib, but not all of them have ELF versions. Such as plain C64, there is only coffabi version of dsplib for this platform.
For those missing dsplib, users should build it by themselves.

Pay attention that mbuild_ti uses its own naming scheme for dsplibs, dsplib_<platform>_<abi>.lib.
    *) <platform> : c64, c64plus, c67, c67plus, c674
    *) <abi> : coffabi, eabi
Make sure you have installed the right dsp library file provided by TI, and rename them to right format or make symbolic links to them with correct names.
    
    Below is a summary of dsplib names:
---------------------------------------------------------------
|         |         coff            |          elf            |
---------------------------------------------------------------
| C64     | dsplib_c64_coff.lib     | dsplib_c64_eabi.lib     | (a)
| C64PLUS | dsplib_c64plus_coff.lib | dsplib_c64plus_eabi.lib |
| C67     | dsplib_c67_coff.lib     | dsplib_c67_eabi.lib     | (b)
| C67PLUS | dsplib_c67plus_coff.lib | dsplib_c67plus_eabi.lib | (c)
| C674    | dsplib_c674_coff.lib    | dsplib_c674_eabi.lib    | (d)
---------------------------------------------------------------
    a) TI doesn't provide c64 eabi.lib, user should rebuild it from source code of coff.lib
    b) TI doesn't provide c67 eabi.lib, user should rebuild it from source code of coff.lib
    c) TI doesn't provide c67plus dsplibs directly, user can reuse dsplib for c674
    d) The dsplib for c674, provided by TI, is a float-point library. To run fixed point code on c674, it just links c64/c64plus dsplib.


5) **** C67x FastRTS Library(fastMath lib) ****
The C67x FastRTS library is an optimized floating-point math function library for C programmers using TMS320C67x devices.

a) Keywords need to be added
By default, mbuild_ti won't link FastRTS library. If you want to use them, add this keyword in your manifest.mb:
    @add ti_fastmathlib_c67_style
Same as dsplib linkage for C67/C67plus, to distinguish between plain C67 and C67plus on C67plus and C674 platform, mbuild_ti will check which of following keywords has been added/defined:
    @add ti_non_plus_core    ==> ISA of non-plus processor will be used (C67)
    @add ti_plus_core        ==> ISA of plus processor will be used (C67+)
and then, mbuild_ti will link the correct FastRTS library according to which keywords you add.

So,
    to link C67     fastMath lib (even on C67plus and C674 platform), you need to add keywords "ti_fastmathlib_c67_style" and "ti_non_plus_core";
    to link C67plus fastMath lib (even on             C674 platform), you need to add keywords "ti_fastmathlib_c67_style" and "ti_plus_core".

b) The naming of fastMath lib
The FastRTS libraries will be linked are:
#    c67pfastMath.lib       ==>  for c67plus, coff
#    c67pfastMath_elf.lib   ==>  for c67plus, elf
#    c67xfastMath.lib       ==>  for c67,     coff
#    c67xfastMath_elf.lib   ==>  for c67,     elf
#    c674xfastMath.lib      ==>  for c674,    coff
#    c674xfastMath_elf.lib  ==>  for c674,    elf
Make sure you have installed the right library files provided by TI.



6) **** Other hints ****
a) Automatic RTS Library Selection
From CGT v6.1.2, the linker has the capability to automatically choose the correct library to match the target and model options of your object code.

b) About C67x Fast Run-Time Support (RTS) Library
C6700 rts library are no longer included in CGT, from v7.3.0. User can download it from TI’s website.
