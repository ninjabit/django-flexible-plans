# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from model_utils import Choices
from model_utils.models import TimeStampedModel, SoftDeletableModel
import swapper


class PlanFeature(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    feature = models.ForeignKey(
        swapper.get_model_name('flexible_plans', 'Feature'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )


class BasePlan(TimeStampedModel, SoftDeletableModel):
    """
    Abstract BasePlan
    -----------------

    BasePlan is TimeStamped, which means it holds a reference to dates of creation and modification.
    BasePlan is SoftDeletable, which means it becomes deactivated and not removed entirely (to keep a reference to
    subscribed plans which become soft-deleted and thus no more available).

    BasePlan also can be visible and available. Plan is displayed on the list of currently available plans
    for user if it is visible. User cannot change plan to a plan that is not visible. Available means
    that user can buy a plan. If plan is not visible but still available it means that user which
    is using this plan already will be able to extend this plan again. If plan is not visible and not
    available, he will be forced then to change plan next time he extends an account.

    BasePlan is defined by its Features, which can be quotas, permissions on objects and features

    """

    class INTERVALS(object):
        DAY = 'day'
        WEEK = 'week'
        MONTH = 'month'
        YEAR = 'year'

        CHOICES = Choices(
            (DAY, _('Day')),
            (WEEK, _('Week')),
            (MONTH, _('Month')),
            (YEAR, _('Year'))
        )

    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)
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
    visible = models.BooleanField(
        _('visible'), default=True, db_index=True,
        help_text=_('Is visible in current offer')
    )
    features = models.ManyToManyField(
        swapper.get_model_name('flexible_plans', 'Feature'),
        through='flexible_plans.PlanFeature'
    )
    interval = models.CharField(
        choices=INTERVALS.CHOICES, max_length=12, default=INTERVALS.MONTH,
        help_text='The frequency with which a subscription should be billed.'
    )
    interval_count = models.PositiveIntegerField(
        help_text='The number of intervals between each subscription billing'
    )
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    @staticmethod
    def get_provider_choices():
        """
        Scans settings to look for configured payment providers and serve them as choice list
        :return: [PaymentProvider]
        """
        from django.conf import settings
        choices = []
        if getattr(settings, 'PAYMENT_PROVIDERS', None):
            choices = list(settings.PAYMENT_PROVIDERS)
        return choices

    @staticmethod
    def get_default_plan(cls):
        """
        Shortcut to retrieve the default plan to be assigned if no plan is selected
        :param cls:
        :return: default Plan instance
        """
        try:
            default_plan = cls.objects.get(default=True)
        except cls.DoesNotExists():
            default_plan = None
        return default_plan

    def get_features_dict(self):
        """
        Retrieve a Dict of all the plan's feature to pass through validators
        :return: {feat.codename: feat.value}
        """
        feat_dict = {}
        for plan_feature in PlanFeature.objects.filter(plan=self).select_related('feature'):
            feat_dict[plan_feature.feature.codename] = plan_feature.value
        return feat_dict

    class Meta:
        abstract = True


class Plan(BasePlan):
    """
    Single plan defined in the system. A plan can be customized (for specific users), which means
    that only those users can purchase this plan and have it selected.

    """
    provider = models.CharField(max_length=100, choices=BasePlan.get_provider_choices())

    def __str__(self):
        return self.name

    class Meta:
        # Setting model as swappable
        swappable = swapper.swappable_setting('flexible_plans', 'Plan')
