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




MEDIA_ROOT = "/home/media/prod/%s/" % SITE_NAME
MEDIA_CACHE_DIR = os.path.join(MEDIA_ROOT , 'cache')

INSTALLED_APPS = (
    'gunicorn',
) + INSTALLED_APPS




DEBUG = False

LOGGING['handlers']["logfile"]["filename"] = "/var/log/nginx/%s/django.log" %  
