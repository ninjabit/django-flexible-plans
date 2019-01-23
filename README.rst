=============================
django-flexible-plans
=============================

.. image:: https://badge.fury.io/py/django-flexible-plans.svg
    :target: https://badge.fury.io/py/django-flexible-plans

.. image:: https://travis-ci.org/ninjabit/django-flexible-plans.svg?branch=master
    :target: https://travis-ci.org/ninjabit/django-flexible-plans

.. image:: https://codecov.io/gh/tobia.ghiraldini/django-flexible-plans/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tobia.ghiraldini/django-flexible-plans

Independent and reusable apps to build app a Subscription Plan System

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

Features
--------

* TODO

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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
