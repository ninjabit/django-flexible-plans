from django.utils import timezone

from flexible_plans.policies.base import PlanChangePolicy


class ImmediateChangePlanPolicy(PlanChangePolicy):
    def change_plan(self, subscription, new_plan):
        subscription.valid_from = timezone.now()
        subscription.plan = new_plan
        subscription.save()

class EndOfMonthChangePlanPolicy(PlanChangePolicy):
    def change_plan(self, subscription, new_plan):
        end_of_month = timezone.now().month
