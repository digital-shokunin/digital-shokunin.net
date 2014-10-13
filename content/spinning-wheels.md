Title: Spinning Wheels
Date: 2014-06-12 21:00
Tags: python, docker, flask, android, vm, 
Slug: spinning-wheels
Category: DevOps
Author: David Mitchell
Summary: So many projects, so little time or motivation

I don't know if its because I'm now settled into the [dad life][dad-life] or what, but I've 
been taking on more personal projects lately, working on them until I 
loose interest or find something else. Of course, leaving them in various 
states of completion, some times returning later. Sometimes its just lack 
of [motivation][10programmerinspire], sometimes I hit a wall, a few cases
are delays since continuing requires hardware or something that costs 
money. Sometimes its just lack of time. A big part of it is the problems
I'm working on don't hold my interest or seem of little point. I seem to 
be working on tutorials or guides, or very little that isn't already
well tread. I want to learn new skills, but I also want to solve real
problems, or tangible improvments to something. I'd love to get involved
in some real projects (but I can't commit due to time), not run through a 
tutorial that gives me an example program to write that no one would 
actually use. That said, here is what I have in the hopper that I've slowly 
been trudging through. 

First is, this site. I haven't posted in months, not for lack of want
but because I had not gotten far enough with anything to make it worth 
posting over. Plus, who knows, talking about my lack of progress, even 
if its to no one in particular, may help me gather my thoughts. Not 
every post has to be great. I realize most won't interest anyone or have
anything that hasn't been said elsewhere. This place is for me to 
journal my attempts at improving myself and my skill set.

I recently stopped messing with [Koding.com][koding] and got myself an instance or
"droplet" with Digital Ocean. Been using that to have fun with Docker[docker].
If you don't know what Docker is, and you work with Linux in production or
development at all, get on that.

On the [Matasano Crypto Challenge][python-fun-profit], I'm just stuck on 
exercise 6 of the first set, which is kind of pathetic, especially when 
I read about how everyone is stuck on the 3rd or 4th set. I have what I 
think is a 95% working solution, but something is off in my ability to 
find just the right algorithm to crack the message. My current solution 
returns something with a lot of, English letters, which fools my algorithm 
into thinking I've found a solution, but none of its readable. In either 
case, I have to be vague about it as one of the rules is I can't post 
solutions. I have reached out for help or hints from both Matasano and 
someone I know whose completed it (actually the person I learned about 
it from). So far no response, which means their busy, but personal 
insecurity leaves me to think I'm so far off the mark I'm not worth 
bothering with. Right now, I'd just be happy to know I'm completely off 
or very warm. I personally just like learning the concepts and it gives 
me an interesting challenge or problem to solve with Python. The Cryto 
course I was taking online got too intense for me to keep up with, and 
knowing little math notation beyond some college algebra/trig, I couldn't
follow the lessons past the 3rd or 4th weeks. I might just lack the 
math knowledge and experience ultimately, even if I can work out an XOR 
or how some stream ciphers or block encryption work. All the same, even if
I take much longer then average people, I still want to at least get as 
far as I can.

For my [Hacker News indicator][indicator-project], I found out the Gtk indicator API could not
redraw the menu, or clear the pre-existing menu items. You can add menu items
but I have found little in the way to change them once its set. This  
meant I could not refresh the list of items with an update. I tried 
switching to the Qt API, which I liked better, but could not get the links
to load when I clicked on them. I really should just post on Stack Overflow
to see what it is exactly I'm doing wrong, of course after I rebuild my
dev virtualenv which kind of got trashed from recent updates to the latest
release of Ubuntu.

I've also been porting or re-writing a game a I wrote in Pascal during 
my senior year of high school for a Computer Science AP final project, 
Welcome to Roxboro, for Android in Java. I've also thought about playing 
around with [kivy][kivy].

Finally, I have been playing with Vagrant on my local machine and JBoss and 
Java Play application servers. This is more of a work thing, even if we're
not yet using any of it currently.

[koding]: http://www.koding.com
[docker]: http://docker.io
[vagrant]: http://vagrantup.com
[python-fun-profit]: /python-fun-profit.html
[securitytube]: http://www.securitytube.net
[flask book]: http://flaskbook.com/
[dad-life]: http://www.youtube.com/watch?v=DOKuSQIJlog
[indicator-project]: /indicator-project.html
[10programmerinspire]: http://halffull.org/2009/01/03/10-ways-to-get-inspiration-as-a-programmer/
[kivy]: http://bytedebugger.wordpress.com/2014/05/21/tutorial-android-development-with-python-and-kivy-introduction/
