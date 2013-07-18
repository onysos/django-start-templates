#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Django developement settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
from common import *
import asyncore

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}

CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
   }
}

ALLOWED_HOSTS += ["127.0.0.1"]


DEBUG = True

THUMBNAIL_DEBUG = DEBUG  # used with sorl.thumbnail
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = dict(INTERCEPT_REDIRECTS=False)



if DEBUG:

    INSTALLED_APPS += (
        'debug_toolbar',  # how to debug without this
    )

    LOGGING['loggers'][''] = {
             'handlers':['console'],
             'level': 'DEBUG',
         }

# be realy carful hier. since in the __init__.py ther is the default settings who include this.
# so even if the real used setting in «prod.py». this file will always be included
if os.environ.has_key("LOCAL_EMAIL"):
    # start  a local debuging server for email.
    EMAIL_HOST = "localhost"
    EMAIL_PORT = "1026"

    from smtpd import DebuggingServer
    try:
        d = DebuggingServer((EMAIL_HOST, int(EMAIL_PORT)), ("localhost", 25))
        print ("debug serveur email runned %s:%s" % (EMAIL_HOST, int(EMAIL_PORT)))
        import threading
        t = threading.Thread(target=asyncore.loop)
        t.daemon = True
        t.start()
    except:
        pass


MEDIA_URL = '/media/'

# URL prefix for static files.
STATIC_URL = '/static/'
