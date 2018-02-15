#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Mitchell'
SITENAME = 'Digital Shokunin'
SITEURL = 'https://digital-shokunin.net'

PATH = 'content'

THEME='blueidea'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('google+','https://plus.google.com/u/0/112141969866873644503/'),
          ('github', 'https://github.com/digital-shokunin'),
          ('twitter', 'https://twitter.com/digitalshokunin'),
          ('linkedin', 'https://linkedin.com/in/sdavidmitchell/'),
          ('email', 'mailto:david.mitchell@digital-shokunin.net'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "digitalshokunin"
GOOGLE_ANALYTICS = "UA-37662566-1"
GITHUB_URL = 'https://github.com/digital-shokunin/'
TWITTER_USERNAME = 'digitalshokunin'

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", 'extra/robots.txt', 'extra/favicon.ico' ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'pictures': {'path': 'pictures'},
    }

DELETE_OUTPUT_DIRECTORY = False
DISPLAY_PAGES_ON_MENU = True

