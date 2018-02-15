Title: Cutter - A GUI for radare2
Date: 2018-02-16 12:00
Tags: hacking, infosec, reverse engineering
Slug: cutter-gui-radare2
Category: InfoSec
Author:David Mitchell
Summary: Setting up Cutter on Linux to work with radare2

I've recently been using [radare2](http://radare.org/) for a bit of reverse engineering and have used it a little bit in the past for CTF competions. (Side note: scaleway.com is a great cloud/VPS service if you need an ARM based server/machine for a something like a CTF to analyze ARM binaries and do not have a Raspberry Pi, ODroid or similar ARM based computer handy.) 

I discovered [Cutter](https://github.com/radareorg/cutter) recently, which has some instructions to compile it using cmake (also qmake but I had and used cmake).

The compile/build instructions make some assumptions, since they're written by devs, they assume you have all the Qt graphics libraries it uses installed. Assuming you have the build-essential package or compile tools already installed.

If you're getting errors similar to:

    Could not find a package configuration file provided by "Qt5" with any of the following names:

      Qt5Config.cmake
      qt5-config.cmake

or

    Could not find a package configuration file provided by "Qt5Svg" with any of the following names:

      Qt5SvgConfig.cmake
      qt5svg-config.cmake

 To install the packages for the Qt libraries required on Ubuntu:

    sudo apt-get install qtdeclarative5-dev libqt5svg5-dev

To install the packages for the Qt libraries required on Fedora:

    sudo dnf install qt-devel qt5-qtsvg-devel

After that, the cmake instructions should work. 