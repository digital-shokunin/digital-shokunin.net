Title: PyDev and wsadmin unite
Date: 2013-02-23 21:00
Tags: python, pydev, websphere
Category: Code
Slug: pydev-wsadmin-unite
Author: David Mitchell
Summary: How to integrate PyDev with the Jython engine for wsadmin used by Websphere Application Server

Those of us that use WebSphere Application Server in our environments as our J2EE application server have a very
powerful tool to administrate or automate tasks from the command line, wsadmin. wsadmin is a command line utility that
allows you to issue commands in a single server or network deployment (multiple servers in a single administrative domain
or "cell"). If you are reading this you probably know all about it and its support for Python, or Jython environment as
a language to issue commands and run scripts to handle a variety of tasks.

Most of us who write scripts for it write our scripts in a text editor and then manually execute them or test small 
portions of our script in a separate command line window. This can be tedious at best, those of us that use an IDE
have the issue that the standard Python interpreter doesn't respect the Websphere modules and it shows errors for 
portions of code that are perfectly valid inside wsadmin.

So when I found [instructions](http://www.ibm.com/developerworks/websphere/techjournal/1209_vansickel/1209_vansickel.html)
on how to integrate the [PyDev IDE add-on/module for Eclipse](http://pydev.org/) and 
wsadmin, I was a little more then excited. This can save me a lot of time writing new code. 

The [steps](http://www.ibm.com/developerworks/websphere/techjournal/1209_vansickel/1209_vansickel.html) are fairly 
straight forward, install Eclipse and PyDev if you haven't already done so, and download [Jython](http://www.jython.org/).
You then configure PyDev to use the Jython jar as your Python interpreter. They provide a script that customizes the 
Jython environment to use wsadmin.

  :::wsadmin script
  wsadmin.bat/sh -host <DM_HOST> -port <SOAP_PORT> 
  -profile WSAdminProfile.py
	-f GeneratePyPredefs.py	
	-pypredefsDir <PREDEFINED_COMPLETIONS>

Overall, the setup is pretty straight forward, if you want to try it yourself, the full instructions along with the 
necessary scripts are [here](http://www.ibm.com/developerworks/websphere/techjournal/1209_vansickel/1209_vansickel.html).
