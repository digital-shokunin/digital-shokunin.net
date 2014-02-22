Title: Metasploitation
Date: 2013-08-05 21:00
Tags: metasploit, security
Category: InfoSec
Slug: metasploitation
Author: David Mitchell
Summary: Metasploit the safe and easy way

So I've been using some of my spare time to experiment with and learn 
how to use Metasploit. I've been familiar with Metasploit for a while 
now, so this isn't really about learning something new so much as it is 
finally getting familiar with a tool that I've messed with only a little
in the past. Part of this is because I have no programming projects to 
occupy myself with since I have a real problem finding an interesting 
problem or project that I can code a solution for. Metasploit is also 
something I feel I should know how to use, if I ever want to run a quick
pentest against my own network, etc.

[Metasploit](http://www.metasploit.com), to be really simple is a "free" 
suite of penetration testing software.  It gives you a framework full of 
tools needed to scan networks, find their vulnerabilites, exploit them, 
and keep track of what you find. Running it requires all the skill of 
your average skiddie, which is good, because I'm mainly a sysadmin who
dabbles in infosec. 

The best way to learn any piece of software is to use it, but with 
something like Metasploit, you kind of need a target network, and you 
don't necessarily want to exploit your own production boxes, and even if
you did, assuming you've "hardened" and patched your services reasonably
well, it will be difficult to get very far with Metasploit knowing very
little about it. Thankfully, the community has provided a solution 
aptly named Metasploitable. [Metasploitable](http://sourceforge.net/projects/metasploitable/) 
is a virtual machine image that runs in [VirtualBox](http://www.virtualbox.org) 
(also "free") which contains a preconfigured Ubuntu Server that is 
intentionally unpatched or has "vulnerablities included". This allows 
you to practice against the target host through multiple vectors to try 
and gain full root access or compromise it some other way.

So you you have a machine to target, now you just need Metasploit, you
of course could just download and install it, but I have found the best
way is to run [BackTrack Linux](http://www.backtrack-linux.org) which 
comes with Metasploit and other tools preinstalled. I personally also 
run this in a virtual box instance, although you could simply run it 
natively off the liveCD or install it on a computer you have available.

You have Metasploit, and you have a machine to practice using it 
against, now you just need a guide to use it all. Well, MetaSploit is 
pretty well documented by itself, but what was recommended to me is the 
[Metasploit Unleashed](http://www.offensive-security.com/metasploit-unleashed/) 
course provided by Offensive Security that guides you through the 
various features of MetaSploit and later exercises you can use. The only 
caveat I've found is that many of the Windows examples obviously don't 
work well against Metasploitable, being Linux, although I suppose you 
could spin up an unpatched Windows XP or 2000 instance to mess with as 
well.

I'm only partially through a few chapters of the Metasploit Unleashed 
course and have already learned quite a bit. Maybe later I'll share some
of what I've learned that I've found very useful here.
