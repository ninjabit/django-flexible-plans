import swapper
from django.db import models
from model_utils.models import TimeStampedModel
from datetime import date, timedelta, datetime


class BaseSubscription(TimeStampedModel):
    """
    Base class for user subscriptions to plans
    """
    plan = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Plan'))
    customer = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Customer'))

    expire = models.DateField(
        _('expire'), default=None, blank=True, null=True, db_index=True)
    active = models.BooleanField(_('active'), default=True, db_index=True)

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

    def clean_activation(self):
        errors = plan_validation(self.user)
        if not errors['required_to_activate']:
            plan_validation(self.user, on_activation=True)
            self.activate()
        else:
            self.deactivate()
        return errors

    class Meta:
        abstract = True


class Subscription(BaseSubscription):
    """
    Concrete swappable class for user subscriptions to plans
    """
    pass
