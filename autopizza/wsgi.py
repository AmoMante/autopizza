"""
WSGI config for autopizza project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopizza.settings")

application = get_wsgi_application()

#Use whitenoise package to serve staticfiles on heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
