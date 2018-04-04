# -*-coding: utf-8 -*-

try:
    from .base import *
except Exception as exc:
    print("error")
    from zakzak_admin.zakzak_admin.settings.base import *

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY', 0)

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'social',
#             'USER': 'root',
#             'PASSWORD': 'k5p8uLRE',
#             'HOST': 'videoshow.ctnauqs33t62.rds.cn-north-1.amazonaws.com.cn',
#             'PORT': 3306
#         },
#         'component': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'component',
#             'USER': 'root',
#             'PASSWORD': 'k5p8uLRE',
#             'HOST': 'videoshow.ctnauqs33t62.rds.cn-north-1.amazonaws.com.cn',
#             'PORT': 3306
#         }
#     }
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'social',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': 3306
        },
        'component': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'component',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': 3306
        },
        'ejabberd': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ejabberd',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': 3306
        }
    }

if __name__ == '__main__':
    print('SECRET_KEY:{}'.format(SECRET_KEY))