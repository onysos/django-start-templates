# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
logger = logging.getLogger(__name__)

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import  admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #===========================================================================
    # url pour login/logout/registration
    #===========================================================================

    # django-registration. permet de s'inscire
    #
    # url(r'^registration/', include('registration.backends.default.urls')),

    # login/logout de django (exclusif a django-registration)
    # if you use this, find a way to remove all auth_ prefix in the templates.
    #
    # url(r'^auth/', include('django.contrib.auth.urls')),

    # some exemples
    # url(r'^$', RedirectView.as_view(url="app1/")),
    # url(r'^app1/', include('app1.urls')), # all namespace should be included by apps themselves
)
