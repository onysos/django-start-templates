# -*- coding: utf-8 -*-
"""
Django developement settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
from __future__ import absolute_import, print_function, unicode_literals
from .common import *  # @UnusedWildImport
import asyncore
import itertools
from copy import deepcopy

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

LOGGING = deepcopy(LOGGING)

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',  # how to debug without this
    )

    if 'debug_toolbar' in INSTALLED_APPS:
        MIDDLEWARE_CLASSES = (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
            ) + MIDDLEWARE_CLASSES

    skipped = [
               # "django_select2",
               ]
    forced = [
                # "django.db",
             ]
    for app in itertools.chain(INSTALLED_APPS, forced):
        LOGGING['loggers'][app] = {
             'handlers': ['console'],
             'level': 'DEBUG',
             'propagate': True,
         }
    for app in skipped:
        LOGGING['loggers'][app] = {
             'handlers': ['console'],
             'level': 'ERROR',
             'propagate': False,
         }
    LOGGING['loggers']['']['handlers'].remove("logfile")

# be realy carful hier. since in the __init__.py ther is the default settings who include this.
# so even if the real used setting in «prod.py». this file will always be included
if os.environ.get("LOCAL_EMAIL", "False").lower() in ("true", "y", "o"):
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

BOOTSTRAP3 = BOOTSTRAP3.copy()
BOOTSTRAP3.update({
    # The URL to the jQuery JavaScript file
    'jquery_url': STATIC_URL + "js/jquery-%s.min.js" % JQuery_Version,
    # The Bootstrap base URL
    'base_url': STATIC_URL + "bootstrap-%s-dist/" % BOOTSTRAP_VERSION,
    'theme_url': STATIC_URL + "bootstrap-%s-dist/css/bootstrap-theme.min.css" % BOOTSTRAP_VERSION,
})
