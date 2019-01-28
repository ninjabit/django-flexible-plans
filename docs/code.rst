Documentation for the Code
**************************

.. automodule:: flexible_plans


Plan Models
=========================

The Plan Model is a concrete, swappable subclass of the abstract BasePlan.

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


Views
=========================

All the CRUD views are defined and available.
Plus, specific views for the Plan management are available
