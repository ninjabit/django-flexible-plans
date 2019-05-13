# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'flexible_plans'
urlpatterns = [
    path('', views.PlanListView.as_view(), name='plan_list'),
    path('<int:plan_id>/', views.PlanDetailView.as_view(), name='plan_detail'),
    path('<int:plan_id>/subscribe/', views.SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscription/', views.SubscriptionDetailView.as_view(), name='subscription_detail'),
    path('subscription/update/', views.SubscriptionUpdateView.as_view(), name='subscription_update'),
]
