# -*- coding: utf-8 -*-
from django.urls import path

from flexible_plans.views import PlanListView, PlanDetailView, SubscriptionCreateView, SubscriptionDetailView, \
    SubscriptionUpdateView

app_name = 'flexible_plans'
urlpatterns = [
    path('', PlanListView.as_view(), name='plan_list'),
    path('<int:pk>/', PlanDetailView.as_view(), name='plan_detail'),
    path('<int:pk>/subscribe/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionDetailView.as_view(), name='subscription_detail'),
    path('subscription/update/', SubscriptionUpdateView.as_view(), name='subscription_update'),
]
