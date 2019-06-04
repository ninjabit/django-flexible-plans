from django.forms import ModelForm

from flexible_plans.models import Subscription


class SubscriptionModelForm(ModelForm):
    class Meta:
        model = Subscription

