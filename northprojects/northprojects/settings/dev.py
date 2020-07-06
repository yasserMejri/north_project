from .base import * # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "q@0r5)wuwu^c(_sd-noqh=6b8i=v0h+r+li@1f641w)jk9c5wx" # noqa

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import * # noqa
except ImportError:
    pass
