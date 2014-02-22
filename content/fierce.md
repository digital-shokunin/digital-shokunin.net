Title: Fierce
Date: 2013-04-11 21:00
Tags: Security, Pen Testing, DNS
Category: InfoSec
Slug: fierce
Author: David Mitchell
Summary: Using fierce to map an organization's external online assets.

I've been learning a little bit about security and penetration testing in my spare time. I have some friends who are professionals in the industry and I have an interest in it myself so when they mention a tool I like to take a look at what it does and learn a little bit about it.

[Fierce](http://ha.ckers.org/fierce/) is a domain scanning tool, what that means is it scans an organization's domains for listed hosts. For example, a target company may have several non-contigious IP ranges or have branch sites or locations that aren't using the same public IP's as say their website or main office. By scanning their DNS records you might discover some hosts on IP's that weren't in the same scope as say their website or primary data center, and thus may be hosts that aren't as vigilantly maintained. An organization's IT department might have hosts or backdoors to access a branch location they setup for themselves that they setup a domain name for (ex:branch32-jumphost.company.com) that isn't apparent by scanning a single IP address range.

By scanning the company's DNS records, you can easily discover the lesser known vectors of attack in theory. Also, it's not as likely to trigger an intrusion detection system like one would if you port scanned an entire company's IP range looking for available hosts.

Fierce is a really simple tool to use, anyone who has used a tool like 
nmap will find it straight forward. Installation is simply done by checking out their subversion repository.

	:::svn
	svn co https://svn.assembla.com/svn/fierce/fierce2/trunk/ fierce2/

It's written in Perl, so you should already have that installed on whatever you'll be running it on. From there it's as simple as going into the newly created fierce2 directory and running a scan against your target.

	:::example
	fierce -dns company.com

There are more [examples on the wiki](https://trac.assembla.com/fierce/wiki)

Now, that I've said all that, while querying someone's DNS records is in and of itself harmless, exercise some common sense. Don't be scanning networks or domains you don't yourself own or have permission to be messing with. At the very least, don't do it exposed from your home IP as you can get yourself in trouble, reported to your ISP, or even in trouble with local law enforcement even if you're just being curious and not going any further then seeing what's out there, it still might be enough to get you in hot water depending on your local laws and ISP's policies. 

However, you might want to know just how much your own domain records give away, and if you administrate your own DNS, you might want to adjust some settings on your DNS servers to prevent too much from being exposed to would-be attackers. After all, why give away more information to the outside world then you absolutely have to. For those cases, this tool is worth having available even if you're not a dediated security professional yourself.
