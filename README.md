django startapp/startproject templates 
============================

a template usable by django_admin.py to start a apps with some better defaults files (django1.7)

usage
-----

first : clone this git repo to get all templates

    git clone https://github.com/onysos/django-start-templates.git /tmp/django-start-template

then startproject

    django-admin.py startproject --template --extension=cfg,hgignore /tmp/django-start-templates/templates/project_template myamazingproject
    
or startapp

    django-admin.py startapp --extension=cfg,html   --template /tmp/django-start-templates/templates/app_template/ myamazingApp



then : insert your own important data in the templates : 

    grep -R --exclude-dir=.git '!![^!]*!!' .  --exclude="*.min.js"

this will show you all «tags» inserted in the templates by a double !!tag!!.

tags can be AUTHOR or AUTHOR_MAIL. just replaces them and that's it,.


startapps
---------
it include for «django-admin.py startapps»:

- all file started by the «coding: utf-8» comment to permit non ASCII char in source file (see http://www.python.org/dev/peps/pep-0263/) 
- an urls.py default file.
- an admin.py 
- a logger variable for each file that will log to the logger designed by the __file__ value.
- a default base template (dont forget the --extension .html)


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
- a twiter bootstrap3 based skelton with: 
  - navbar  (connexion, admin access, password change) with dynamic par apps «active» items 
  - footer
  - javascript
  - customized errors pages (404,500,503)
- all settings needed by default for use django_nginx apps (designed to generate init script and nginx config)
- a buildout.cfg default file which can be a good start point.

  
all templates is currently writen un French, so remember to translate manualy all these. 
(feel free to make a push request if you translate without customizing too much)


exemple of default site in 5 minute
-----------------------------------

first, don't work in your home, or it will be a mess soon enouth
```bash
cd /tmp/
mkdir experiments
cd experiments
```

copy this repo (how can you try it without getting it ?)

```bash
git clone https://github.com/onysos/django-start-templates.git /tmp/django-start-template
```

create your project «amayinapps» rigth hier

```bash
django-admin.py startproject amazingapps --extension .cfg --template /tmp/django-start-template/templates/project_template

cd amazingapps
```

create buildout tree

```bash
python bootstrap.py
```

make buildout env for dev (-c prod.cfg will use prod dependecy and settings.prod)

```bash
bin/buildout -c dev.cfg
```

go into the dirrectory for custom apps

```bash
cd src/amazingapps/apps
```

create your app «app1»

```bash
django-admin.py startapp --template /tmp/django-start-template/templates/app_template app1 --extension .html


cd ../../.. 
```

run the server and check your message «It worked!»
```bash
bin/django runserver
```
  
  
  
####rigth now
you don't have anything in your urls.py, so you can't see anything.
lets correct this by:

1. add «app1» in INSTALLED_APPS:

```vim src/amazingapps/amazingapps/settings/common.py```

2. add some url in your urls.py (project and apps)

```
vim src/amazingapps/apps/app1/urls.py
vim src/amazingapps/amazingapps/urls.py
```


3. restart server:

```bin/django runserver```


####take a look at your files:


templates: 

- src/amazingapps/amazingapps/templates
- src/amazingapps/apps/app1/templates

urls:

- src/amazingapps/amazingapps/urls.py
- src/amazingapps/apps/app1/urls.py

views:

- src/amazingapps/apps/app1/views.py
  

thanks
------

a big thanks to Randall Degges whos wrote http://www.rdegges.com/the-perfect-django-settings-file/
where i found the settings skeleton.

note
----

feel free to contribute if you see somthing usefull that is not in this template

  
