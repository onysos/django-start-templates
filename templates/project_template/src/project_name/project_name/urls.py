# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
logger = logging.getLogger(__name__)

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),


    # some exemples
    # url(r'^$', RedirectView.as_view(url="app1/")),
    # url(r'^app1/', include('app1.urls', namespace="app1")),
)
