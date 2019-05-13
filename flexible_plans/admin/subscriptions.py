from django.contrib import admin
import swapper
from fsm_admin.mixins import FSMTransitionMixin


Subscription = swapper.load_model('flexible_plans', 'Subscription')


@admin.register(Subscription)
class SubscriptionAdmin(FSMTransitionMixin, admin.ModelAdmin):
    pass
