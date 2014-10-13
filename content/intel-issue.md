Title: Intel Graphics Issues with Ubuntu 12.04
Date: 2014-02-20 21:00
Tags: hardware, ubuntu, linux
Slug: intel-issue
Category: DevOps
Author: David Mitchell
Summary: Intel 4400 bug in Ubuntu 12.04 LTS

I have an [XPS 13 Developer edition laptop (aka Project Sputnick)][xps13], after 
some updates to Ubuntu in recent months, it would randomly freeze. It became apparent it 
was the graphics card that was freezing as processes were still running 
even though the display image was frozen and the mouse nor any other input
seemed to have no affect (if I left it on downloads would finish). 
This was very frustrating as I had bought an officially supported set of 
hardware for Ubuntu from Dell to eliminate these kind of hardware support 
headaches. Turns out the issue is a [known issue][issues] with Intel 4400 
graphics chipset and the old kernel. The solution was simple, 
get a more recent kernel, which means updating from the LTS 12.04 release 
of Ubuntu to a newer version. Since doing the update I've had only one freeze 
in almost a month.

I will say I am a bit disappointed with Dell and Ubuntu for letting this
issue continue. This is nearly unexcusable and the LTS version should be
the most stable and well supported, especially since it is what it comes with. 
This has made me lose work, and is a massive problem with an otherwise high 
quality set of hardware. Such a hard lock issue on a platform known for stability
on a widely available chipset should receive top priority and the fix should
have been back ported to the kernel used by 12.04 by the Ubuntu dev team.
 
[issues]: http://www.howtoeverything.net/linux/hardware/random-freezes-integrated-hd-4000-graphics
[xps13]: http://www.dell.com/us/business/p/xps-13-linux/pd
