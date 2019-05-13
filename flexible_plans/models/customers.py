import swapper
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


class BaseCustomer(TimeStampedModel):
    """
    BaseCustomer
    Abstract base class definition for the necessary customers features
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class Customer(BaseCustomer):
    """
    Customer Class related to user and referenced back from Subscription
    """

    @property
    def name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def __str__(self):
        return "{0} ({1})".format(self.user, self.name)

    class Meta:
        # Setting model as swappable
        swappable = swapper.swappable_setting('flexible_plans', 'Customer')
