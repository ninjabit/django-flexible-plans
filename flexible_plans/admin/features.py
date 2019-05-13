from django.contrib import admin
import swapper
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from flexible_plans.models import PlanFeature

Feature = swapper.load_model('flexible_plans', 'Feature')
MeteredFeature = swapper.load_model('flexible_plans', 'MeteredFeature')
CumulativeFeature = swapper.load_model('flexible_plans', 'CumulativeFeature')
PermissionFeature = swapper.load_model('flexible_plans', 'PermissionFeature')


class FeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 1


@admin.register(Feature)
class FeatureAdmin(PolymorphicParentModelAdmin):
    base_model = Feature
    child_models = (MeteredFeature, CumulativeFeature, PermissionFeature)
    list_filter = (PolymorphicChildModelFilter,)


@admin.register(MeteredFeature)
class MeteredFeatureAdmin(PolymorphicChildModelAdmin):
    base_model = MeteredFeature


@admin.register(PermissionFeature)
class PermissionFeatureAdmin(PolymorphicChildModelAdmin):
    base_model = PermissionFeature


@admin.register(CumulativeFeature)
class CumulativeFeatureAdmin(PolymorphicChildModelAdmin):
    base_model = CumulativeFeature
