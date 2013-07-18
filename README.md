django application templates 
============================

a template usable by django_admin.py to start a apps with some better defaults files (django1.5)

usage
-----

first : clone this git repo to get all templates

    git clone https://github.com/onysos/django-start-templates.git /tmp/django-start-template

then startproject

    django-admin.py startproject --template /tmp/django-start-templates/templates/project_template myamazingproject
    
or startapp

    django-admin.py startapp --template /tmp/django-start-templates/templates/app_template/ myamazingApp




startapps
---------
it include for «django-admin.py startapps»:

- all file started by the «coding: utf-8» comment to permit non ASCII char in source file (see http://www.python.org/dev/peps/pep-0263/) 
- an urls.py default file.
- an admin.py 
- a logger variable for each file that will log to the logger designed by the __file__ value.


startproject
------------
for django-admin.py startproject:


a fully functional tree for requirment and settings.  
it permit to put settings and requirments.txt in version controle and stay as modular as possible.

settings.py is expoded in : 
- settings/common.py
- settings/prod.py
- settings/dev.py

with a retrocopatibility with a basic DJANGO_SETTINGS_MODULE=myapps.settings since settings/__init__.py import all dev settings.

to use prod settings, just put  DJANGO_SETTINGS_MODULE=myapps.settings.prod

with this structur, you can have all prod/dev settings versionned and directly.

the default common.py settings provide:

- dynamic SECRET key generation in a local file (default to root_project/SECRET)
- absolute path detection and easy file location.
- a colorized logging formatter for console output. (autmatic in debug config)
- separated static/media url to skip useless cookie transmission. configure your server properly
- the include of a «VERSION» file that may be generated by VCS to access the current version.


thanks
------

a big thanks to Randall Degges whos wrote http://www.rdegges.com/the-perfect-django-settings-file/
where i found the settings skeleton.

note
----

feel free to contribute if you see somthing usefull that is not in this template

  