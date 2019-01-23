=====
Usage
=====

To use django-flexible-plans in a project, add it to your `INSTALLED_APPS`:

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
