#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'David Mitchell'
SITENAME = u'Digital Shokunin'
SITEURL = ''

LOCALE = 'en_US'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME='subtle'

#Menu items
MENUITEMS = (('Home', 'http://digital-shokunin.net'),)

# Blogroll
#LINKS =  (('FabLocker', 'http://www.fablocker.org'),
#          ('PyPTUG', 'http://www.pyptug.org'),
#          ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#         )

# Social widget
SOCIAL = (('google+','https://plus.google.com/u/0/112141969866873644503/'),
          ('github', 'http://github.com/digital-shokunin'),
          ('twitter', 'http://twitter.com/digitalshokunin'),
          ('linkedin', 'http://www.linkedin.com/profile/view?id=51799602'),
          ('lastfm', 'http://lastfm.com/user/surgeterrix'),
          ('email', 'mailto:david.mitchell@digital-shokunin.net'),
         )


# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "digitalshokunin"
GOOGLE_ANALYTICS = "UA-37662566-1"
GITHUB_URL = 'http://github.com/digital-shokunin/'
TWITTER_USERNAME = 'digitalshokunin'


DELETE_OUTPUT_DIRECTORY = False

SITEURL = 'http://digital-shokunin.net'
