"""
WSGI config for myblogger project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblogger.settings")

application = get_wsgi_application()
# whitenoise adds capability to serve 'static' files
application = DjangoWhiteNoise(application)
