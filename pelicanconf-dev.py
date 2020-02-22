#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Jason Hall'
SITENAME = 'A Rapt Mind'
SITETITLE = 'ARM'
SITESUBTITLE = 'Suffering from tech ADD'
SITEDESCRIPTION = 'A Rapt Mind - A blog about technology and life'
#SITEURL = 'https://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

USE_FOLDER_AS_CATEGORY=True
DISPLAY_CATEGORIES_ON_MENU=True


# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/makerjd/'),
        ('Twitter', 'https://twitter.com/cleverIdent'),
        ('rss', '/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
            'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## pulled fom Flex's pelicanconf.py
SITELOGO = '/images/profile-hollow.png'
favicon = '/images/favicon.ico'
browser_color = '#333333'
pygments_style = 'monokai'

ROBOTS = 'index, follow'

date_formats = {
    'en': '%b %d, %y',
}

MAIN_MENU = True
#home_hide_tags = True

MENUITEMS = (('archives', '/archives.html'),
             ('categories', '/categories.html'),
             ('tags', '/tags.html'),)

cc_license = {
    'name': 'creative commons attribution-sharealike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#disqus_sitename = "flex-pelican"
#add_this_id = 'ra-55adbb025d4f7e55'

#static_paths = ['images', 'extra']

#custom_css = 'static/custom.css'

#use_less = true

#google_adsense = {
#    'ca_id': 'ca-pub-6625957038449899',
#    'page_level_ads': true,
#    'ads': {
#        'aside': '8752710348',
#        'main_menu': '',
#        'index_top': '',
#        'index_bottom': '1124188687',
#        'article_top': '',
#        'article_bottom': '4843941849',
#    }
#}
