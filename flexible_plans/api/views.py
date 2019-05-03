from rest_framework import viewsets

from flexible_plans.api.serializers import PlanSerializer
from flexible_plans.models import Plan


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

