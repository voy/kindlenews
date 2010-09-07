# -*- coding: utf-8 -*-

# Django settings for kindlenews project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'kindlenews.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)

NEWS_SOURCES = (
    { 'name': 'zdrojak',
      'name_verbose': 'Zdroják',
      'url': 'http://www.zdrojak.cz/rss/clanky/',
      'selectors': {'content': '#main .urs'} },
    { 'name': 'smartmania',
      'name_verbose': 'SmartMania',
      'url': 'http://smartmania.cz/rss.php',
      'selectors': {'content': '#article-text'} },
    { 'name': 'arstechnica',
      'name_verbose': 'ars technica',
      'url': 'http://arstechnica.com/',
      #'max_items': 3,
      'continuations': lambda art: art.find(".pager li a"),
      'selectors': {
	      'stories': '#all-stories .story',
          'title': 'h2',
          'teaser': '.teaser',
          'link': '.read-more-link a',
          'content': '#story .body' } },
)

NEWS_SOURCES_LOOKUP = dict([(item['name'], item) for item in NEWS_SOURCES])

ALLOWED_TAGS = ('p', 'a', 'img', 'em', 'strong', 'pre', 'br', 'i', 'b', 'h2',
    		'h3')
    		
ALLOWED_ATTRIBUTES = ('href', 'src')

try:
    from local_settings import *
except ImportError:
    pass
    
