# -*- coding: utf-8 -*-
"""
Django production settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#std:setting-DATABASES
from common import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # postgresql_psycopg2   =   mysql
        'NAME': SITE_NAME,
        'HOST': '',
        'USER': 'user',
        'PASSWORD': 'PASSWD',
        'PORT': 1433,
    }
}

# used by default django_nginx config
USE_X_FORWARDED_HOST = True

MEDIA_ROOT = "/home/media/prod/%s/" % SITE_NAME
MEDIA_CACHE_DIR = os.path.join(MEDIA_ROOT , 'cache')

INSTALLED_APPS = (
    'gunicorn',
) + INSTALLED_APPS




DEBUG = False
logfile = "/var/log/django/%s/django.log" % FULL_SITE_NAME
if os.access(os.path.dirname(os.path.dirname(logfile)), os.W_OK) and not os.path.exists(os.path.dirname(logfile)):
    try:
        os.mkdir(os.path.dirname(logfile))
    except OSError:
        pass

if os.access(logfile, os.W_OK) or (not os.path.exists(logfile) and os.access(os.path.dirname(logfile), os.W_OK)):
    LOGGING['handlers']["logfile"]["filename"] = logfile


if DEBUG:
    # permet de recupere des info en plus en prod en cas de pepin
    for apps in INSTALLED_APPS:
        LOGGING['loggers'][apps] = {
             'handlers':['logfile'],
             'level': 'DEBUG',
         }

    LOGGING['handlers']["logfile"]["level"] = "DEBUG"
