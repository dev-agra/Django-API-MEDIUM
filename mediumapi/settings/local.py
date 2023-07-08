from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env( 
    "DJANGO_SECRET_KEY",
    default="django-insecure-dw1g$r#66(z^-l@$2on+u*^nnd-p^s7d98je2(2s=w3ace6xso",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "gammabytes.sup@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Medium API"
