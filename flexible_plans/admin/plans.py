from django.contrib import admin
import swapper
from flexible_plans.admin.features import FeatureInline


class PlanAdmin(admin.ModelAdmin):
    inlines = (FeatureInline,)
    # fields = ('__all__',)
    # inlines = (FeatureInline,)


admin.site.register(swapper.load_model('flexible_plans', 'Plan'), PlanAdmin)
