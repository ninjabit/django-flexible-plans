# -*- coding: utf-8
from django.apps import AppConfig


class FlexiblePlansConfig(AppConfig):
    """
    Default App Config

    Usage:

    * add 'flexible_plans' to INSTALLED_APPS settings and this config will be loaded
    * create and add another config to INSTALLED_APPS settings to load this app with custom AppConfig
    """
    name = 'flexible_plans'
    verbose_name = 'Plans'
