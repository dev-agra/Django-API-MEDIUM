"""
WSGI config for mediumapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: chanegit in productoin
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mediumapi.settings.local")

application = get_wsgi_application()
