import sys
from django.conf import settings


def import_providers_modules(submodule=None):
    providers = getattr(settings, 'PAYMENT_PROVIDERS', [])
    modules = {}
    for provider_name in providers:
        fqmn = provider_name
        if submodule:
            fqmn = '%s.%s' % (fqmn, submodule)
        __import__(fqmn)
        module = sys.modules[fqmn]
        modules[provider_name] = module
    return modules
