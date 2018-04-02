import os
from .base import *

# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = os.getenv('SECRET_KEY', 0)
DEBUG = False

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'social',
            'USER': 'http',
            'PASSWORD': 'boUnTNQm',
            'HOST': 'vshow.cfp43fliem3t.eu-central-1.rds.amazonaws.com',
            'PORT': 3306
        },
        'component': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'component',
            'USER': 'http',
            'PASSWORD': 'boUnTNQm',
            'HOST': 'vshow.cfp43fliem3t.eu-central-1.rds.amazonaws.com',
            'PORT': 3306
        }
    }