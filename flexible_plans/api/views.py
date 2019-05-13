from rest_framework import viewsets
from flexible_plans.api.serializers import PlanSerializer, SubscriptionSerializer, CustomerSerializer
from swapper import load_model


Plan = load_model("flexible_plans", "Plan")
Subscription = load_model("flexible_plans", "Subscription")
Customer = load_model("flexible_plans", "Customer")


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
