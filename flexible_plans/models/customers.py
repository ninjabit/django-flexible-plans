from django.db import models
from django.conf import settings
import swapper


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER, on_delete=models.CASCADE)

    class Meta:
        # Setting model as swappable
        swappable = swapper.swappable_setting('flexible_plans', 'Customer')

