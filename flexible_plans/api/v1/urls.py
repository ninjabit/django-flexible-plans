from django.urls import path
from rest_framework import routers
from flexible_plans.api.v1.views import PlanViewSet, SubscriptionViewSet, CustomerViewSet

router = routers.SimpleRouter()
router.register(r'plans', PlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls
