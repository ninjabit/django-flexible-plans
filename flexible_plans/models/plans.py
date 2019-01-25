# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, SoftDeletableModel
import swapper


class BasePlan(TimeStampedModel, SoftDeletableModel):
    """
    Abstract BasePlan
    BasePlan is TimeStamped, which means it holds a reference to dates of creation and modification.
    BasePlan is SoftDeletable, which means it becomes deactivated and not removed entirely (to keep a reference to
    subscribed plans which become soft-deleted and thus no more available).
    """
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        abstract = True


class Plan(BasePlan):
    """
    Single plan defined in the system. A plan can be customized (for specific users), which means
    that only those users can purchase this plan and have it selected.

    Plan also can be visible and available. Plan is displayed on the list of currently available plans
    for user if it is visible. User cannot change plan to a plan that is not visible. Available means
    that user can buy a plan. If plan is not visible but still available it means that user which
    is using this plan already will be able to extend this plan again. If plan is not visible and not
    available, he will be forced then to change plan next time he extends an account.

    Plan is defined by its Features, which can be quotas, permissions on objects and features
    """

    default = models.NullBooleanField(
        help_text=_('Both "Unknown" and "No" means that the plan is not default'),
        default=None,
        db_index=True,
        unique=True,
    )
    available = models.BooleanField(
        _('available'), default=False, db_index=True,
        help_text=_('Is still available for purchase')
    )
    features = models.ManyToManyField(swapper.get_model_name('flexible_plan', 'Feature'))
