from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env( 
    "DJANGO_SECRET_KEY",
    default="django-insecure-dw1g$r#66(z^-l@$2on+u*^nnd-p^s7d98je2(2s=w3ace6xso",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["https://localhost:8080"]