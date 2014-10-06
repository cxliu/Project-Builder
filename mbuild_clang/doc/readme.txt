Xcode Plugin for M-Build

Contents
--------
1. What is this?
2. What exactly does this provide?
3. How do I use it?
4. How does a customer use it?


1. What is this?
----------------
This is plugin for M-Build which adds support for the Xcode toolchain. When this plugin is used, it will allow a project to say that it wishes to support building with Xcode, and then M-Build will generate Makefiles (and potentially Xcode projects) for these configurations. The plugin uses the xcrun tool to call the toolchain so that command line tools are not required on the machine.

2. What exactly does this provide?
----------------------------------
This plugin can provide targets for OSX and iOS builds using Clang, called via the xcrun tool. Release and Debug flavours with support for x86, amd64 and armv7 processors.


3. How do I use it?
-------------------
In your top level manifest, @import the mbuild_clang/manifest.mb file. Once you have done this, you can add clang support to any project by using the "clang_support" symbol in a .project file. e.g. if you had:

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
                    clang_support,
                  ),
)

And makefiles will be generated for all of the supported cores.
