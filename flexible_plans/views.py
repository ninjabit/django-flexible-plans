# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Plan,
	PlanItem,
	UserPlan,
)


class PlanCreateView(CreateView):

    model = Plan


class PlanDeleteView(DeleteView):

    model = Plan


class PlanDetailView(DetailView):

    model = Plan


class PlanUpdateView(UpdateView):

    model = Plan


class PlanListView(ListView):

    model = Plan


class PlanItemCreateView(CreateView):

    model = PlanItem


class PlanItemDeleteView(DeleteView):

    model = PlanItem


class PlanItemDetailView(DetailView):

    model = PlanItem


class PlanItemUpdateView(UpdateView):

    model = PlanItem


class PlanItemListView(ListView):

    model = PlanItem


class UserPlanCreateView(CreateView):

    model = UserPlan


class UserPlanDeleteView(DeleteView):

    model = UserPlan


class UserPlanDetailView(DetailView):

    model = UserPlan


class UserPlanUpdateView(UpdateView):

    model = UserPlan


class UserPlanListView(ListView):

    model = UserPlan

