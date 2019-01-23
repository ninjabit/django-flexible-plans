# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'flexible_plans'
urlpatterns = [
    url(
        regex="^Plan/~create/$",
        view=views.PlanCreateView.as_view(),
        name='Plan_create',
    ),
    url(
        regex="^Plan/(?P<pk>\d+)/~delete/$",
        view=views.PlanDeleteView.as_view(),
        name='Plan_delete',
    ),
    url(
        regex="^Plan/(?P<pk>\d+)/$",
        view=views.PlanDetailView.as_view(),
        name='Plan_detail',
    ),
    url(
        regex="^Plan/(?P<pk>\d+)/~update/$",
        view=views.PlanUpdateView.as_view(),
        name='Plan_update',
    ),
    url(
        regex="^Plan/$",
        view=views.PlanListView.as_view(),
        name='Plan_list',
    ),
	url(
        regex="^PlanItem/~create/$",
        view=views.PlanItemCreateView.as_view(),
        name='PlanItem_create',
    ),
    url(
        regex="^PlanItem/(?P<pk>\d+)/~delete/$",
        view=views.PlanItemDeleteView.as_view(),
        name='PlanItem_delete',
    ),
    url(
        regex="^PlanItem/(?P<pk>\d+)/$",
        view=views.PlanItemDetailView.as_view(),
        name='PlanItem_detail',
    ),
    url(
        regex="^PlanItem/(?P<pk>\d+)/~update/$",
        view=views.PlanItemUpdateView.as_view(),
        name='PlanItem_update',
    ),
    url(
        regex="^PlanItem/$",
        view=views.PlanItemListView.as_view(),
        name='PlanItem_list',
    ),
	url(
        regex="^UserPlan/~create/$",
        view=views.UserPlanCreateView.as_view(),
        name='UserPlan_create',
    ),
    url(
        regex="^UserPlan/(?P<pk>\d+)/~delete/$",
        view=views.UserPlanDeleteView.as_view(),
        name='UserPlan_delete',
    ),
    url(
        regex="^UserPlan/(?P<pk>\d+)/$",
        view=views.UserPlanDetailView.as_view(),
        name='UserPlan_detail',
    ),
    url(
        regex="^UserPlan/(?P<pk>\d+)/~update/$",
        view=views.UserPlanUpdateView.as_view(),
        name='UserPlan_update',
    ),
    url(
        regex="^UserPlan/$",
        view=views.UserPlanListView.as_view(),
        name='UserPlan_list',
    ),
	]
