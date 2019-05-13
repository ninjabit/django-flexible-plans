# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from ..models.plans import Plan


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

