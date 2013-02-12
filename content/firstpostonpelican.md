Title: My first post using Pelican
Date: 2013-02-10 21:00
Tags: python, pelican
Category: Code
Slug: first-post-pelican
Author: David Mitchell
Summary: First post using Pelican blogging platform

This is my first post using Pelican as my new blogging platform. I had considered using [OctoPress](http://www.octopress.org) but encountered too much trouble getting the ruby stack to work properly without dependency problems, even following directions or tutorials. So I looked for a Python alternative and found [Pelican](http://docs.notmyidea.org/alexis/pelican/). I found it was much simpler to get running just following the directions. Plus, I know Python, so I'm obviously more comfortable with it then Ruby. Ruby I've never dealt with directly until OctoPress and my prior experience only included reading about it.

I am using AWS to host this, AWS EC2 host or S3 bucket are securely configured to only allow login through ssh with a private key. This makes it difficult to simply publish over ssh. Some changes need to be made to the site Makefile to allow for this.

On line 18:

    :::Makefile
    SSH_PRI_KEY=<path to private key file>

Further down on line 60:

    :::Makefile	
    ssh_upload: publish
    scp -i $(SSH_PRI_KEY) -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

From there a simple 

    :::sshupload
    make ssh_upload

will push it out to my AWS host.

For some reason, this type of blogging platform seems more elegant then a CMS like WordPress, it gives you the control you get from statically coding your site's html/css/js, to say nothing of the lack of overhead required to serve static content. However, it still gives you the dynamically generated links and ease of management one gets from a CMS. That and it's very programmer friendly.

I need some time to go through all the [themes](https://github.com/getpelican/pelican-themes) for Pelican but so far I like the simple look of the default template. I may either tweak it or try out some of the other themes.

I also have some other things to work on this site, get used to using markdown, adding some more content, and testing the limitations of Pelican.
    
