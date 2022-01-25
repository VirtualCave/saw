
from .base import *

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
    }
}
