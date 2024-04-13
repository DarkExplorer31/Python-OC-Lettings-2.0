import os
import sentry_sdk
import logging
import logging.config
import dj_database_url

from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "oc_lettings_site",
    "lettings",
    "profiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
        }
    }
else:
    # Retrieve secret db password from environment variable
    db_password = os.getenv("DB_PASSWORD")
    db_hostname = os.getenv("DB_HOSTNAME")

    # Check if secret db password is defined
    if db_password and db_hostname:
        DATABASES = {
            "default": dj_database_url.config(
                default=f"postgres://main:{db_password}"
                + f"@{db_hostname}.frankfurt-postgres.render.com/oc_lettings_site_vaog"
            )
        }
    else:
        raise ValueError(
            "DB_PASSWORD and DB_HOSTNAME environment variable is not defined."
        )

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"

if not DEBUG:
    STORAGES = {
        "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"}
    }

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Configure logging
logger = logging.getLogger(__name__)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    # Loggers
    "loggers": {
        # Logger for Django components
        "django": {
            "handlers": ["console"],  # Handlers associated with this logger
            "level": "WARNING",  # Log level for this logger (WARNING)
            "propagate": True,  # Propagate messages to parent loggers
        },
        # Logger for the "oc_lettings_site" application
        "oc_lettings_site": {
            "handlers": ["console"],  # Handlers associated with this logger
            "level": "DEBUG",  # Log level for this logger (DEBUG)
            "propagate": False,  # Do not propagate messages to parent loggers
        },
        # Logger for the "lettings" application
        "lettings": {
            "handlers": ["console"],  # Handlers associated with this logger
            "level": "DEBUG",  # Log level for this logger (DEBUG)
            "propagate": False,  # Do not propagate messages to parent loggers
        },
        # Logger for the "profile" application
        "profile": {
            "handlers": ["console"],  # Handlers associated with this logger
            "level": "DEBUG",  # Log level for this logger (DEBUG)
            "propagate": False,  # Do not propagate messages to parent loggers
        },
    },
}

logging.config.dictConfig(LOGGING)

# Initialize Sentry
sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        enable_tracing=True,
        traces_sample_rate=0.1,
        profiles_sample_rate=0.1,
    )
else:
    logger.warning(
        "The SENTRY_DSN environment variable is not defined."
        + " Please contact the previous developer to obtain the link."
    )

# Retrieve secret key from environment variable
secret_key = os.getenv("SECRET_KEY")

# Check if secret key is defined
if secret_key:
    SECRET_KEY = secret_key
else:
    logger.error(
        "The SECRET_KEY environment variable is not defined. "
        + "Please contact the previous developer to obtain the link."
    )
