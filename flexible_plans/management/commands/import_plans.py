from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    import_plans Management Command

    Usage: from the project shell invoke the admin command

    .. code-block:: bash

    $ python manage.py import_plans <provider_name>

    where <provider_name> must match with the providers' name configured in settings (all lowercase)

    """
    help = ''

    def handle(self, *args, **options):
        pass



