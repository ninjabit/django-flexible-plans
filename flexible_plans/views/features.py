from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)
from ..models.features import Feature


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
