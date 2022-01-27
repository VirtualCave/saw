import os
from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoApp',
        'USER': 'djangoApp',
        'PASSWORD': 'masterPassword1234!',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
}

SECRET_KEY = "5(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d"
STATIC_PATH = os.path.join(BASE_DIR, "/code/web-static")
