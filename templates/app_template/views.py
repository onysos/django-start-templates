# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
from django.views.generic.base import TemplateView
logger = logging.getLogger(__name__)


from django.shortcuts import render

# Create your views here.

class BaseTemplate(TemplateView):
    template_name = "{{app_name}}/base.html"
