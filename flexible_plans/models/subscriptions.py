import swapper
from datetime import date, timedelta, datetime
from django.conf import settings
from django.db import models
from django.utils.timezone import now

from model_utils.models import TimeStampedModel
from datetime import date
from django.utils.translation import gettext_lazy as _

from flexible_plans.signals import subscription_activate, subscription_deactivate
from flexible_plans.utils.validators import plan_validation


class BaseSubscription(TimeStampedModel):
    """
    Base class for user subscriptions to plans
    """
    customer = models.OneToOneField(swapper.get_model_name('flexible_plans', 'Customer'), on_delete=models.CASCADE)
    plan = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Plan'), on_delete=models.CASCADE, related_name='+')
    expire = models.DateField(
        _('expire'), default=None, blank=True, null=True, db_index=True)
    active = models.BooleanField(_('active'), default=True, db_index=True)

    def clean_activation(self):
        errors = plan_validation(self.customer)
        if not errors['required_to_activate']:
            plan_validation(self.customer, on_activation=True)
            self.activate()
        else:
            self.deactivate()
        return errors

    def is_active(self):
        return self.active

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

    def activate(self):
        if not self.active:
            self.active = True
            self.save()
            subscription_activate.send(sender=self, customer=self.customer)

    def deactivate(self):
        if self.active:
            self.active = False
            self.save()
            subscription_deactivate.send(sender=self, customer=self.customer)

    def initialize(self):
        if not self.is_active():
            if self.expire is None:
                self.expire = now() + timedelta(
                    days=getattr(settings, 'PLANS_DEFAULT_GRACE_PERIOD', 30)
                )
            self.activate()

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
