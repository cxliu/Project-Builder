Android Plugin for M-Build

Contents
--------
1. What is this?
2. What exactly does this provide?
3. How do I use it?
4. How does a customer use it?


1. What is this?
----------------
This is plugin for M-Build which adds support for the androideabi toolchain. When this plugin is used, it will allow a project to say that it wishes to support building with androideabi, and then M-Build will generate Makefiles for these configurations. The plugin expects that the androideabi toolchain is properly configuered on the users machine.

2. What exactly does this provide?
----------------------------------
This plugin can provide targets for android based systems. Release and Debug flavours with support for armv7a processors.


3. How do I use it?
-------------------
In your top level manifest, @import the mbuild_android/manifest.mb file. Once you have done this, you can add android support to any project by using the "android_support" symbol in a .project file. e.g. if you had:

my_project = ProjectSpec(
	actions=mbuild_compile_and_link,
	depends=[],
	build_configuration=mbuild_standard,
)

You can change this to:

my_project = ProjectSpec(
	actions=mbuild_compile_and_link,
	depends=[],
	build_configuration=mbuild_union(
                    mbuild_standard,
                    android_support,
                  ),
)

And makefiles will be generated for all of the supported cores.

Notes that this plugin depends on mbuild_arm, please be sure mbuild_arm/manifest.mb is imported too.

4. How does a customer use it?
------------------------------
For building images on ARM-Linux Android we require the arm-linux-androideabi compiler and related tools to be in your $PATH.

First download latest NDK at http://developer.android.com/tools/sdk/ndk/index.html#Installing
Unpack it to directory <NDK>, The toolchain in <NDK>/toolchains/arm-linux-androideabi-4.8 can't be used separately, we should build a standalone version of android cross compiler which including system header files and libs located at <NDK>/platforms/android-9/arch-arm. This could be done by command:

	<NDK>/build/tools/make-standalone-toolchain.sh --ndk-dir=<NDK> --platform=<PLATFORM> --toolchain=<TOOLCHAIN> --arch=arm --system=<SYSTEM> --install-dir=<ANDROID TOOLCHAIN>
 
For example:
	<NDK>/build/tools/make-standalone-toolchain.sh --ndk-dir=/home/cxliu/bin/android-ndk-r9c --platform=android-9 --toolchain=arm-linux-androideabi-4.8 --arch=arm --install-dir=/home/cxliu/bin/arm-linux-androideabi-4.8-r9 --system=linux-x86 --verbose

Include this standalone toolchain into PATH:
	export PATH="<ANDROID TOOLCHAIN>/bin":$PATH
