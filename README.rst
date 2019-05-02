=============================
django-flexible-plans
=============================

.. image:: https://badge.fury.io/py/django-flexible-plans.svg
    :target: https://badge.fury.io/py/django-flexible-plans

.. image:: https://travis-ci.org/ninjabit/django-flexible-plans.svg?branch=master
    :target: https://travis-ci.org/ninjabit/django-flexible-plans

.. image:: https://codecov.io/gh/ninjabit/django-flexible-plans/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ninjabit/django-flexible-plans

Independent and reusable Plan, Subscription app used to build the Django Subscription Plan System

`Django-Subscription-Plan-System`_

.. _Django-Subscription-Plan-System: git@github.com:ninjabit/django-subscription-plan-system.git

Status
------
Under heavy development. Not ready for use yet. Please feel free to join and contribute.

Documentation
-------------

The full documentation is at https://django-flexible-plans.readthedocs.io.

Quickstart
----------

Install django-flexible-plans::

    pip install django-flexible-plans

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'flexible_plans.apps.FlexiblePlansConfig',
        ...
    )

Add django-flexible-plans's URL patterns:

.. code-block:: python

    from flexible_plans import urls as flexible_plans_urls


    urlpatterns = [
        ...
        url(r'^', include(flexible_plans_urls)),
        ...
    ]

Create Features PlanFeatures, Plans through the admin panel to let users activate their subscriptions.


Features
--------

Plans have Features that describe them and what their subscribers can do or their quotas
Users can subscribe to Plans and their Subscription can be activated, deactivated, renewed, prorated, upgraded or downgraded.


Roadmap
-------

* Configurable, swappable Plan Model, to customize the Plan Class behaviour
* Dynamic imports from other app in the ecosystem to handle all the other aspects of having a plan subscription system
* Multiple plan types, with support of any combination of quotas, features, permissions.
* Multiple plan/subscription provider support

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  `django-model-utils`_
*  `django-swappable-models`_
*  `django-countries`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage
.. _django-model-utils: https://github.com/jazzband/django-model-utils
.. _django-swappable-models: https://github.com/wq/django-swappable-models
.. _django-countries: https://github.com/SmileyChris/django-countries
