# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
logger = logging.getLogger(__name__)


from django.conf.urls import patterns, include, url
from .views import BaseTemplate

# add all urls into a given namespace

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(
        patterns('',
            # Examples:
            # url(r'^blog/', include('blog.urls')),
            # url(r'^$', BaseTemplate.as_view(), name="view1"),
        ), namespace='{{project_name}}')
    ),
)


