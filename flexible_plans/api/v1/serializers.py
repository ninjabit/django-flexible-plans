from rest_framework import serializers
from swapper import load_model

Plan = load_model('flexible_plans', 'Plan')
Subscription = load_model('flexible_plans', 'Subscription')
Customer = load_model('flexible_plans', 'Customer')
Feature = load_model('flexible_plans', 'Feature')


class FeatureSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        depth = 1


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user', 'subscription')
