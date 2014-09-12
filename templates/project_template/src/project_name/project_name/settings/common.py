# -*- coding: utf-8 -*-
"""
Django common settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
import os



import sys
from os.path import abspath, basename, dirname, join, normpath

#===============================================================================
# MUST Update settings
#===============================================================================


DOMAIN_NAME = 'example.com'  # the root domain name from which all static and apps will be sub_domain.
# ie : sitename = django  => static_url will be //static-django.example.com/ and base site url will be //django.example.com/

# the administrator IP address which can have direct access event durring server maintenance (used by django_ngnix apps)
ADMINISTRATOR_IP = ['127.0.0.1']

# urls from with all transmission shoul be securized with ssl (https).
# remember do prefix your urls (in urls.py) with this to make sur that the http server can
# make the redirections acordingly (see django_nginx apps)
# SECURE_PREFIX = ["/secure/", "/accounts/"] # for only /secure and /accounts/ pages # beware for session thief 
SECURE_PREFIX = ["~ /.+"] # for all non home pages
SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')

########## APP CONFIGURATION
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #------------------------------------------------------------------------------
    # some well recomended apps :D
    #------------------------------------------------------------------------------
    # 'grappelli', # jazzy  admin interface
    # 'django.contrib.admin', # django admin interface


    # 'sorl.thumbnail', # powerfull thumbnail lib in templates
    # 'registration', # django_registration => a complet registarion apps with mail validation
    # 'bootstrap_toolkit',# usefull helper for skin using twiter bootstrap
    # 'django_nginx', # generate nginx config with «manage.py create_nginx_config»

    #------------------------------------------------------------------------------
    # some must have apps (activated by default
    #------------------------------------------------------------------------------
    'south',  # South migration tool.
    'django_extensions',  # a Must have tool

    #------------------------------------------------------------------------------
    # your apps come hier
    #------------------------------------------------------------------------------
    # 'app1',

)

#===============================================================================
# dynamic settings
#===============================================================================


########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
ROOT = DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Site name.
SITE_NAME = basename(DJANGO_ROOT)


DEFAULT_FROM_EMAIL = "%s@%s" % (SITE_NAME, DOMAIN_NAME)

# gues import path for project directory import
try:
    # try in a buildout powered env
    __import__("%s.%s.context_processors" % (SITE_NAME, SITE_NAME))
    BASE_IMPORT_PATH = "%s.%s" % (SITE_NAME, SITE_NAME)
except ImportError:
    # default conf
    BASE_IMPORT_PATH = SITE_NAME



# all path redefinable


# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
FQDN = "%s.%s" % (SITE_NAME, DOMAIN_NAME)
LOGFILE = SITE_ROOT + "/django.log"
try:
    # compatibilité avec django_manager
    # on umporte ces settings pour trouver les vrais paths demandé par
    # django_manager
    from {{ project_name }}.localsettings.django_manager_settings import *
except ImportError:
    pass  # pas de fichier importable

FULL_SITE_NAME = FQDN
_splited = FQDN.split(".")
DOMAIN_NAME = "%s.%s" % tuple(_splited[-2:])
if len(_splited) > 2:
    SITE_NAME = ".".join(_splited[:-2])



# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
SECRET_FILE = normpath(join(SITE_ROOT, 'SECRET'))

VERSION_FILE = normpath(join(SITE_ROOT, 'VERSION'))


# after each update, i do a
# $ hg parent -q > $VERSION_FILE which permit to display the current version in the footer for example.
if os.access(VERSION_FILE, os.R_OK):
    LOCAL_VERSION = open(VERSION_FILE).read().strip()
else:
    LOCAL_VERSION = None
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# Disable debugging by default.
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = (
    ('admin', 'admin@%s' % DOMAIN_NAME),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems. On Unix systems, a value
# of None will cause Django to use the same timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Paris"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html.
LANGUAGE_CODE = 'fr'

LANGUAGES = (
        ('fr', 'Français'),
)


# AUTH_USER_MODEL = "appname.modelname"



DEFAULT_LANGUAGE = 1
# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific site(s) and a
# single database can manage content for multiple sites.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.


# URL that handles the media served from MEDIA_ROOT.
if LOCAL_VERSION is None:
    MEDIA_URL = '//static-%s/media/' % FULL_SITE_NAME
else:
    MEDIA_URL = '//static-%s/media/r%s/' % (FULL_SITE_NAME, LOCAL_VERSION)

########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.

# URL prefix for static files.


if LOCAL_VERSION is None:
    STATIC_URL = '//static-%s/static/' % FULL_SITE_NAME
else:
    STATIC_URL = '//static-%s/static/r%s/' % (FULL_SITE_NAME, LOCAL_VERSION)


# Additional locations of static files.
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'staticfiles')),
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION

########## TEMPLATE CONFIGURATION
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "%s.context_processors.version" % BASE_IMPORT_PATH,  # a simple processor who give access to LOCAL_VERSION isued from VCS

    )





########## END MIDDLEWARE CONFIGURATION
BOOTSTRAP_BASE_URL = STATIC_URL + "/bootstrap/"
LOGIN_URL = "auth:login"  # since django 1.5, can be a named url patern

LOGIN_REDIRECT_URL = "/"


########## END APP CONFIGURATION


########## URL CONFIGURATION

# buildout : we have root/src/project/project/urls.py

# ROOT_URLCONF = '%s.%s.urls' % (SITE_NAME, SITE_NAME)
# default
ROOT_URLCONF = '%s.urls' % (BASE_IMPORT_PATH)

ALLOWED_HOSTS = [FULL_SITE_NAME] + ADMINISTRATOR_IP
########## END URL CONFIGURATION

CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
   }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

########## KEY CONFIGURATION
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    from random import choice
    try:
        with open(SECRET_FILE, 'w') as f:
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)') for i in range(50)])
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
########## END KEY CONFIGURATION

######### Mercurial Version



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
                        'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
                    },
        'simple': {
                        'format': '%(levelname)-8s %(asctime)s %(module)-8s:%(lineno)-4s %(message)s'
                    },
        'colored': {  # a nice colored format for terminal output
                        'format': '\033[1;33m%(levelname)s\033[0m [\033[1;31m%(name)s\033[0m:\033[1;32m%(lineno)s\033[0m:\033[1;35m%(funcName)s\033[0m] \033[1;37m%(message)s\033[0m'
                    },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
         'console':{
             'level':'DEBUG',
             'class':'logging.StreamHandler',
             'formatter': 'colored',
         },
         'logfile': {
            'level':'WARNING',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['logfile'],
            'level': 'WARNING',
            'propagate': True,
        },


    }

}


