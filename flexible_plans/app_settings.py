from django.conf import settings

SUBSCRIPTION_PIPELINE = getattr(settings, 'FLEXIBLE_PLANS_SUBSCRIPTION_PIPELINE', [
    'flexible_plans.subscription_pipeline.CreateUser',
    'flexible_plans.subscription_pipeline.CreateCustomer',
    'flexible_plans.subscription_pipeline.CreatePaymentMethod',
    'flexible_plans.subscription_pipeline.CreateBillingInfo',
    'flexible_plans.subscription_pipeline.CreateSubscription',
])
