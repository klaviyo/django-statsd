from importlib import import_module

from django.conf import settings

for patch in getattr(settings, 'STATSD_PATCHES', []):
    import_module(patch).patch()
