import os

from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "1l!$kok*bhp*y9wp#&3q(q8sc&$y5iem=f0_ds2%l=iyc4w&k#"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "blog",
    "robots",
    "taggit",
    "taggit_helpers",
    "ckeditor",
    "axes",
    "location_field.apps.DefaultConfig",
    "django_countries",
    "colorfield",
    "adminsortable2",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = "bttrs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bttrs.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

SITE_ID = 1

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOCATION_FIELD = {
    "map.provider": "openstreetmap",
    "provider.openstreetmap.max_zoom": 18,
}

LANGUAGES = [
    ("ru", _("Russian")),
    ("en", _("English")),
]
