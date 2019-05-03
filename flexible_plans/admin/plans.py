from django.contrib import admin
import swapper


class PlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(swapper.load_model('flexible_plans', 'Plan'), PlanAdmin)
