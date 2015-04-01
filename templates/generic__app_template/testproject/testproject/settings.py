# -*- coding: utf-8 -*-
"""
Django settings for testproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')rv-568mrdgim+gtev7&d^99csg%dw)ht)^v8ffx9o0+uc^40l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{{project_name}}',
    'searchlist.tests.testsapps',
    'django_nose',
    'bootstrap3',
    "django_select2",
    "bootstrap3_datetime",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-doctest',
    '--with-coverage',
    '--cover-package=searchlist',
    '--all-modules',
    # 'searchlist', 'testproject',
]

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = "Europe/Paris"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html.
LANGUAGE_CODE = 'fr'

LANGUAGES = (
        ('fr', 'Français'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

LOGGING_BASE = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'colored': {  # a nice colored format for terminal output
                        'format': '\033[1;33m%(levelname)s\033[0m [\033[1;31m%(name)s\033[0m:\033[1;32m%(lineno)s\033[0m:\033[1;35m%(funcName)s\033[0m] \033[1;37m%(message)s\033[0m'
                    },
    },
    'handlers': {
         'console': {
             'level':'DEBUG',
             'class':'logging.StreamHandler',
             'formatter': 'colored',
         },
    },
    'loggers': {
        'searchlist': {
             'handlers': ['console'],
             'level': 'DEBUG',
             'propagate': True,
        },
        '': {
             'handlers': ['console'],
             'level': 'ERROR',
             'propagate': True,
             },
    }
}

import os
if "DEBUG" in os.environ:
    LOGGING = LOGGING_BASE
STATIC_URL = '/static/'

SELECT2_BOOTSTRAP = True
