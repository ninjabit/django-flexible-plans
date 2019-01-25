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

    class Meta:
        abstract = True


class Feature(BaseFeature):
    objects = InheritanceManager()

    class Meta:
        swappable = swapper.swappable_setting('flexible_plan', 'Feature')


class MeteredFeature(Feature):
    units = models.PositiveIntegerField(default=0)


class CumulativeFeature(Feature):
    pass
