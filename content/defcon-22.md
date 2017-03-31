Title: DefCon 22 and BSides LV recap
Date: 2014-09-02 21:00
Tags: hacking, security 
Slug: defcon-22
Category: InfoSec
Author: David Mitchell
Summary: Summary of my experiences at BSides LV and DefCon 22

I managed to make it to Vegas in a rather unexpected way, what originally
was a planned beach trip ended up not working out, and I ended up being 
able to join [FALE][fale] at [BSides LV][bsideslv] and [DefCon 22][defcon].

<img width="600" alt="badge" src="/pictures/table.jpg">

I was working in the mornings, but most of my free time at BSides LV was 
spent at our lockpick village where we were joined by someone making hand
made lockpicks as you can see above. I didn't get to attend any talks, but the 
talks were [found online][bsides-talks] shortly after, my favorite one 
being the Hack the Gibson talk which focused on IBM mainframes. Very 
educational considering I work with mainframes and do some operations on 
them at work. Jon McAfee, yes, that [McAfee](http://www.mcafee.com) also 
made an appearance, which was interesting to say the least. He talked a 
little about his version of events regarding [his recent troubles in Belize](http://www.wired.com/2012/12/ff-john-mcafees-last-stand/).
Including alleged hired assassins out to get him, his personal [spy ring](http://arstechnica.com/tech-policy/2013/01/the-bizarre-tale-of-john-mcafee-spymaster/), and people
popping out from behind trees they're hiding behind, and snapping pictures, etc.
Later, he shifted into some Snowden-esque persona rallying for personal
privacy online, and plugged his new product that spys on spyware, not sure
how you protect yourself from spyware by installing his "trusted" spyware,
but that was the sales pitch from my view. Also, there was the 
[tower of vendor distributed condoms, collectively named "Bonerhenge"][bonerhenge], 
built by some people who apparently didn't have a better use for them in 
Vegas, thus had some time on their hands. 

<img width="600" alt="badge" src="/pictures/lockpicks.jpg">

There were super sensitive recruiters who get really upset when you tell 
them that you don't like them, when asked why your refusing their stuff 
after they continually interrupt your conversation to offer you something, 
and report you to the staff for "rudeness". This may or may 
not have lead to FALE not being invited back next year, which would be 
kind of sad because BSides started because vendor influence at other cons 
kept certain talks from taking place. Granted this is a meager incident, 
but it still means a vendor is dictating what's allowed and all of FALE 
is being held accountable for someone's individual opinion. Although, I 
concur that recruiters especially in this case can be annoying. If someone 
doesn't want what you're offering and is trying to talk to someone, step 
off. If you want to know their reasons and ask, at least don't get mad 
when you get an honest answer. What's weird is it probably wasn't even 
close to some things we normally do that some might consider offensive. 
So when someone from the BSides staff pointed his finger at us and started
heckling us saying we should be ashamed of ourselves, with zero context a
long time after the "incident" took place of which the rest of us weren't 
aware of, we asked him what specificaly was he referring to?

The rest of the week was spent at DefCon...sort of. We spent at least half
of it at the hotel room hacking the badge do all sorts of crazy stuff like
spam/reset other people's badges, etc. The source code for the badge firmware 
was provided on a disc, and found online as well. We created our own altered
versions and you can take a look at the code on [github][badge-code]. The badge
was based on the propeller chipset by a company called Parallax. The propeller 
an open source multi-core chip that's low power and could be compared to an
Arduino. Like an Arduino it has a C like language and can be re-programmed
over an USB interface. The badge itself had LED's, various touch/contact 
switches that functioned like buttons, pin outs and IR TX/RX which were
mainly used for communicating with other badges. Due to it's capabilities
there are all sorts of projects you can use the badge for, you can do your
own Propeller based robot which I know some people are working on, or just
about anything. The hardware hacking room had a contest for the coolest 
badge hack. The code also contained clues that were used in the badge challenge
which they have every year which is a key to a larger puzzle that you solve. That 
was for those who were very dedicated. Most of our hacks were getting it
to do cool new LED patterns and to reset other badges like a Goon badge 
(attendees had a mere Human badge, where as people with special status 
had custom badges, like Speakers, Press, etc).

<img width="600" alt="badge" src="/pictures/badge.jpg">

To be honest, the most fun was trying to figure out the badge, I attended
some talks sure, but nothing to me is better than sitting around a table 
trying to figure out how the thing works while drinking red bull. This
to me is the quintessential DefCon experience I'd always heard about.

<img width="600" alt="badge" src="/pictures/badge_hacking.jpg">

I did attend some talks, still waiting for them to make it online, I also
checked out the rest of the con, saw what there was to see, went to a few
after hours events, ate my first In and Out burger which I went to in a 
limo. I also just chilled out by the pool, especially when I managed to 
lock myself out of the hotel room.

<img width="600" alt="badge" src="/pictures/pool.jpg">

All and all, it was a great first time experience, and I hope I can do 
it again next year.


[defcon]: https://defcon.org
[fale]: http://www.lockfale.com
[bsides-talks]: http://www.irongeek.com/i.php?page=videos/bsideslasvegas2014/mainlist
[bsideslv]: http://www.bsideslv.org/
[bonerhenge]: /pictures/henge.jpg
[badge-code]: https://github.com/lockfale/Defcon-22-badge



