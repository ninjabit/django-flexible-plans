Documentation for the Code
**************************

.. automodule:: flexible_plans


Plan Models
=========================
There is the abstract BasePlan which leverages all the necessary functionalities
around the Plan definition and flow.
There is a concrete, swappable, Plan implementation to provide with a ready to use model.

* BasePlan
* Plan


.. automodule:: flexible_plans.models.plans
    :members:


Feature Models
=========================

There are a few Feature concrete, swappable subsclasses of the abstract BaseFeature to represent different types of features
with different logic:

* BaseFeature
* Feature
* MeteredFeature
* CumulativeFeature
* PermissionFeature


.. automodule:: flexible_plans.models.features
    :members:


Customer Models
=========================

There is a BaseCustomer abstract model which leverage the base and necessary
functionalities around registered and subscribed users.
There is a concrete, swappable, Customer model implementation to provide with a sensible starting point.


.. automodule:: flexible_plans.models.customers
    :members:


Subscription Models
=========================

There is a BaseSubscription class which leverage the basic flow and logic of users subscriptions to plans.
There is a concrete, swappable, Subscription model implementation to provide with a ready to use model.


.. automodule:: flexible_plans.models.subscriptions
    :members:


Views
=========================

All the CRUD views are defined and available.
Plus, specific views for the Plan management are available


API
=========================

API views and serializers base on djangorestframework are provided, to ease the support for a full featured
rest api
