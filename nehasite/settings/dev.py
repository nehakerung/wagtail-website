from django.conf.global_settings import INTERNAL_IPS

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3mtq!i!cwya8jz&=l=&x31tjjsp&7anq--7*@n=x2q8#0i)&ff"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar"
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1", "localhost")
try:
    from .local import *
except ImportError:
    pass
