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
]
