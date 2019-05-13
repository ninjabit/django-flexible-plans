from django.views.generic import CreateView, DetailView, UpdateView

from flexible_plans.models import Subscription


class SubscriptionCreateView(CreateView):
    model = Subscription


class SubscriptionDetailView(DetailView):
    model = Subscription


class SubscriptionUpdateView(UpdateView):
    model = Subscription
