# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models.features import Feature
from .models.plans import Plan


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


class FeatureCreateView(CreateView):

    model = Feature


class FeatureDeleteView(DeleteView):

    model = Feature


class FeatureDetailView(DetailView):

    model = Feature


class FeatureUpdateView(UpdateView):

    model = Feature


class FeatureListView(ListView):

    model = Feature

