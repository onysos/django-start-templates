# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
logger = logging.getLogger(__name__)


from django.conf.urls import patterns, include, url
from views import BaseTemplate


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', BaseTemplate.as_view(), name="view1"),

)
