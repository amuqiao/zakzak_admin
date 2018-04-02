"""
WSGI config for zakzak_admin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
# -*-coding: utf-8 -*-
import os

from django.core.wsgi import get_wsgi_application

#  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zakzak_admin.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zakzak_admin.settings.local")

application = get_wsgi_application()
