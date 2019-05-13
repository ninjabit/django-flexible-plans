import swapper
from datetime import date, timedelta, datetime
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django_fsm import FSMField, transition

from model_utils.models import TimeStampedModel
from datetime import date
from django.utils.translation import gettext_lazy as _

from flexible_plans.signals import subscription_activate, subscription_deactivate
from flexible_plans.utils.validators import plan_validation


class BaseSubscription(TimeStampedModel):
    """
    Base class for user subscriptions to plans
    """
    class STATE:
        ACTIVE = 'active'
        INACTIVE = 'inactive'
        ACTIVATING = 'activating'
        CANCELED = 'canceled'
        ENDED = 'ended'

        @classmethod
        def as_list(cls):
            return [getattr(cls, state) for state in vars(cls).keys() if state[0].isupper()]

        @classmethod
        def as_choices(cls):
            return (
                (state, state.capitalize()) for state in cls.as_list()
            )

    customer = models.OneToOneField(swapper.get_model_name('flexible_plans', 'Customer'), on_delete=models.CASCADE)
    plan = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Plan'), on_delete=models.CASCADE, related_name='+')
    trial_end = models.DateField(
        blank=True, null=True,
        help_text='The date at which the trial ends. '
                  'If set, overrides the computed trial end date from the plan.'
    )
    start_date = models.DateField(
        blank=True, null=True,
        help_text='The starting date for the subscription.'
    )
    cancel_date = models.DateField(
        blank=True, null=True,
        help_text='The date when the subscription was canceled.'
    )
    ended_at = models.DateField(
        blank=True, null=True,
        help_text='The date when the subscription ended.'
    )
    state = FSMField(
        choices=STATE.as_choices(), max_length=12, default=STATE.INACTIVE,
        protected=False, help_text='The state the subscription is in.'
    )
    data = JSONField(default=dict, blank=True, null=True)

    def clean_activation(self):
        errors = plan_validation(self.customer)
        if not errors['required_to_activate']:
            plan_validation(self.customer, on_activation=True)
            self.activate()
        else:
            self.deactivate()
        return errors

    def is_expired(self):
        if self.expire is None:
            return False
        else:
            return self.expire < date.today()

    def days_left(self):
        if self.expire is None:
            return None
        else:
            return (self.expire - date.today()).days

    # def activate(self):
    #     if not self.active:
    #         self.active = True
    #         self.save()
    #         subscription_activate.send(sender=self, customer=self.customer)
    #
    # def deactivate(self):
    #     if self.active:
    #         self.active = False
    #         self.save()
    #         subscription_deactivate.send(sender=self, customer=self.customer)

    # def initialize(self):
    #     if not self.is_active():
    #         if self.expire is None:
    #             self.expire = now() + timedelta(
    #                 days=getattr(settings, 'PLANS_DEFAULT_GRACE_PERIOD', 30)
    #             )
    #         self.activate()

    ##########################################################################
    # STATE MACHINE TRANSITIONS
    ##########################################################################
    @transition(field=state, source=[STATE.INACTIVE, STATE.CANCELED],
                target=STATE.ACTIVE)
    def activate(self, start_date=None, trial_end_date=None):
        if start_date:
            self.start_date = min(timezone.now().date(), start_date)
        else:
            if self.start_date:
                self.start_date = min(timezone.now().date(), self.start_date)
            else:
                self.start_date = timezone.now().date()
        subscription_activate.send(sender=self.__class__, subscription=self)
        # if self._should_activate_with_free_trial():
        #     if trial_end_date:
        #         self.trial_end = max(self.start_date, trial_end_date)
        #     else:
        #         if self.trial_end:
        #             if self.trial_end < self.start_date:
        #                 self.trial_end = None
        #         elif self.plan.trial_period_days:
        #             self.trial_end = self.start_date + timedelta(
        #                 days=self.plan.trial_period_days - 1)

    @transition(field=state, source=[STATE.ACTIVE], target=STATE.CANCELED)
    def cancel(self):
        subscription_deactivate.send(sender=self.__class__, subscription=self)

    ##########################################################################
    # PRIVATE METHODS
    ##########################################################################

    class Meta:
        abstract = True


class Subscription(BaseSubscription):
    """
    Concrete swappable class for user subscriptions to plans
    """

    class Meta:
        swappable = swapper.swappable_setting('flexible_plans', 'Subscription')

    def __str__(self):
        return "{0} {1}".format(self.customer, self.plan)
