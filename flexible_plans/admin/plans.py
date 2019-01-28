from django.contrib import admin
from flexible_plans.models import Plan
import swapper


class PlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(swapper.load_model('flexible_plans', 'Plan'), PlanAdmin)
