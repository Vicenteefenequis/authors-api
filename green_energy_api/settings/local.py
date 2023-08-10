from .base import * #noqa
from .base import env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="4SDHRhTfbVAipwc_A9hDPIM7jBZcrEuTN4AfuNgFXa_yzfKrEvc",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "vicente19981@live.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Green Energy"