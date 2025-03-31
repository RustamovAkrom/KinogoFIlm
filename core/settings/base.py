import os  # noqa
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv, find_dotenv

from core.config import *  # noqa

load_dotenv(find_dotenv(".env"))

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

INSTALLED_APPS = [*THIRD_PARTY_APPS, *DEFAULT_APPS, *PROJECT_APPS]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "assets/templates")],
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

WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

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

LANGUAGE_CODE = "uz"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("uz", _("Uzbek")),
    ("ru", _("Russia")),
    ("en", _("English")),
)

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

MODELTRANSLATION_LANGUAGES = ("uz", "ru", "en")

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"

STATIC_URL = "static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("assets/static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("assets/staticfiles"))

MEDIA_URL = "media/"
MEDIA_ROOT = str(BASE_DIR.joinpath("assets/media"))

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

LOCALE_MIDDLEWARE_EXCLUDED_PATHS = ["/media/", "/static/"]

ADMIN_USERNAME = str(os.getenv("ADMIN_USERNAME"))
ADMIN_PASSWORD = str(os.getenv("ADMIN_PASSWORD"))
ADMIN_EMAIL = str(os.getenv("ADMIN_EMAIL"))

AUTH_USER_MODEL = "users.User"

GOOGLE_CLIENT_ID = str(os.getenv("GOOGLE_CLIENT_ID"))
FACEBOOK_APP_ID = str(os.getenv("FACEBOOK_APP_ID"))

SOCIAL_SECRET = "SOCIAL_SECRET"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "core.auth.EmailAuthBackend",
]

DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE")
