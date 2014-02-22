Title: Python indicator applet
Date: 2013-12-14 21:00
Tags: python, qt, gtk
Slug: indicator-project
Category: Code
Author: David Mitchell
Summary: Writing a Hacker News applet for Gtk/Ubuntu indicators

In my attempt to code more, I've been looking for a purpose or a problem 
to which I can apply what I've learned or use as a reason to acquire new
knowledge. One of the things I've been working on a clone of a Mac OS X 
application an [acquaintance of mine is writing][hacker-bar].
This has begun my foray into writing using the [PyGObject][pyGOTutorial]
API for GTK along with the [Ubuntu GTK indicator API][ubuntuAppIndicator]. 
The PyGTK library is deprecated (GTK 3 going forward), which is what most 
of the examples I've found online use where as there is less documentation 
and discussion for PyGObject. In keeping with using the latest I am writing 
it in Python 3.

I have it somewhat working, in that it will display a list of links that 
you can click on and open a browser, but have had some trouble getting it
to update/refresh the listing. I've also run into limitations in GTK menus
that will not allow me to show little icons for the number of points/comments
an article has. You can view what I have so far on the [GitHub repo][hacker-news-applet]

I'm also trying out Qt as an alternative to get around the GTK limitations. 
There is a [Qt branch][hacker-news-app-qt] for that. Still, I have some 
separate issues like getting the links to open. If I can get those squared 
away and make the menu refresh and draw icons, I will abandon the GTK API 
entirely and merge the Qt version/branch into the main branch.


[hacker-bar]: https://github.com/MohawkApps/Hacker-Bar
[pyGOTutorial]: https://python-gtk-3-tutorial.readthedocs.org/en/latest/index.html
[ubuntuAppIndicator]: https://unity.ubuntu.com/projects/appindicators/
[hacker-news-applet]: https://github.com/digital-shokunin/Hacker-News-Applet
[hacker-news-app-qt]: https://github.com/digital-shokunin/Hacker-News-Applet/tree/qt
