# -*- coding: utf-8 -*-

# Django settings for kindlenews project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vojtech Jasny', 'voy@voy.cz'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

APP_ROOT = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(APP_ROOT, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = ''

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
    'django.contrib.admin',
    'kindlenews.apps.sources',
    'south'
)

NEWS_SOURCES_LOOKUP = dict([(item['name'], item) for item in NEWS_SOURCES])

ALLOWED_TAGS = ('p', 'a', 'img', 'em', 'strong', 'pre', 'br', 'i', 'b', 'h2',
    		'h3')
    		
ALLOWED_ATTRIBUTES = ('href', 'src')

