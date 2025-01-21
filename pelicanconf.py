import os
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.contents import Content

AUTHOR = 'PM'
SITENAME = 'Center for Multimodal Neuroimaging'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/cmn-themes"
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
STATIC_PATHS = ['images', "assets"]

MARKDOWN = {
    'extensions': ['extra', 'codehilite', 'toc'],
    'output_format': 'html5',
}


# Activate the plugin
PLUGINS = [
    'plugins.generate_people', 
    'plugins.generate_talks', 
    'plugins.generate_series',
    'plugins.generate_posts',
]
#SITEURL = 'https://cmn.nimh.nih.gov'
SITEURL = 'http://localhost:8000'
