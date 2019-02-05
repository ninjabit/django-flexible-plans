# -*- coding: utf-8 -*-

from django.db import models
from model_utils.managers import InheritanceManager
from django.utils.translation import gettext_lazy as _
import swapper


class BaseFeature(models.Model):
    """
    BaseFeature Abstract Model defines the feature behaviour
    """
    name = models.CharField(_('name'), max_length=255)
    codename = models.CharField(
        _('codename'), max_length=50, unique=True, db_index=True)
    description = models.TextField(_('description'), blank=True)

    def get_validator(self):
        """
        Get the proper validator from the ValidatorPolicy registry
        :return: Validator object that matches with the feature codename or None
        """
        validators = []
        for validator in validators:
            if validator.name == self.codename:
                return validator
        return None

    def log_usage(self):
        """
        Logs the feature usage, against the correct validator
        """
        # TODO: write a base implementation, or raise an error to force a subsclass specific implementation
        pass
        # raise NotImplementedError()

    class Meta:
        abstract = True


class Feature(BaseFeature):
    """
    Feature default implementation
    Feature is a swappable model to allow client to use their own Feature model.
    It is recommended to subclass BaseFeature to inherit all the behaviours and base fields.
    Being Feature a base class of other specific Feature Classes, it support an InheritanceManager
    to return all kinds of objects on Feature querysets
    """
    objects = InheritanceManager()

    class Meta:
        # Setting model as swappable
        swappable = swapper.swappable_setting('flexible_plans', 'Feature')


class MeteredFeature(Feature):
    units = models.PositiveIntegerField(default=0)
    usage = models.PositiveIntegerField(default=0)


class CumulativeFeature(Feature):
    usage = models.PositiveIntegerField(default=0)
