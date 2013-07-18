# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django.conf import settings
logger = logging.getLogger(__name__)


def version(request):
    ret = {}
    if hasattr(settings, "LOCAL_VERSION"):
        ret["LOCAL_VERSION"] = settings.LOCAL_VERSION

    if hasattr(settings, "SITE_NAME"):
        ret["SITE_NAME"] = settings.SITE_NAME

    return ret

