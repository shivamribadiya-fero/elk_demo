import logging

from django.conf import settings


class SiteFilter(logging.Filter):

    def filter(self, record):
        record.site = getattr(settings, "SITE_NAME", "tia_vm")  # set dynamically in middleware.py
        return True
