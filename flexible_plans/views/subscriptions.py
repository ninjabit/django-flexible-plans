from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from flexible_plans.models import Subscription, Plan, Customer


class SubscriptionCreateView(CreateView):
    model = Subscription
    fields = ()
    success_url = reverse_lazy('plans:subscription_detail')

    def form_valid(self, form):
        plan = Plan.objects.get(pk=self.kwargs['pk'])
        form.instance.customer = self.request.user.customer
        form.instance.plan = plan
        return super(SubscriptionCreateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        current_customer = self.request.user.customer
        try:
            current_subscription = self.request.user.customer.subscription
            if current_customer and current_subscription:
                return redirect(self.success_url)
        except:
            pass
        return super(SubscriptionCreateView, self).get(request, *args, **kwargs)


class SubscriptionDetailView(LoginRequiredMixin, DetailView):
    model = Subscription

    def get_object(self, queryset=None):
        return self.request.user.customer.subscription


class SubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Subscription
    fields = ('plan',)
    success_url = reverse_lazy('plans:subscription_detail')

    def get_object(self, queryset=None):
        return self.request.user.customer.subscription
