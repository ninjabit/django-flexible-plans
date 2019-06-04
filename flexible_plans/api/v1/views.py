from django.conf import settings
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from flexible_plans.api.v1.serializers import PlanSerializer, SubscriptionSerializer, CustomerSerializer
from swapper import load_model


Plan = load_model("flexible_plans", "Plan")
Subscription = load_model("flexible_plans", "Subscription")
Customer = load_model("flexible_plans", "Customer")


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    # permission_classes = ()


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated,])
    def subscription(self, request):
        user = request.user
        serializer = SubscriptionSerializer(user.customer.subscription)
        return Response({'subscription': serializer.data})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)


class CustomerSubscriptionCreateView(APIView):
    permission_classes = (permissions.AllowAny,)
    user_class = settings.AUTH_USER_MODEL

    def post(self, request, *args, **kwargs):
        user_data = {
            'email': kwargs.get('email'),
            'password': kwargs.get('password'),
        }
        subscription_data = {
            'plan_id': kwargs.get('pricing')
        }
        payment_data = {
            'payment_token': kwargs.get('payment')
        }
        billing_data = {
            'billing_name': kwargs.get('billingName'),
            'company_name': kwargs.get('companyName'),
            'company_address': kwargs.get('companyAddress')
        }
        user = self.user_class.objects.create(user_data)
        return Response(
            {
                'user': user,
                'customer': user.customer,
                'subscription': user.customer.subscription
            }
        )
