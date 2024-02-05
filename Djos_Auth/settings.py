import os
from datetime import timedelta

import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
# Reading env
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #! External
    'rest_framework',
    'djoser',
    'corsheaders',
    'drf_spectacular',
    #? Internal
    'core'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Djos_Auth.urls"

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000'
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = "Djos_Auth.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USERNAME'),
        'PASSWORD': env('DATABASE_PASSWORD')
    }
}

# AUTHENTICATION_BACKENDS = [
#     'core.models.auth_backend.EmailOrUsernameModelBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

AUTH_USER_MODEL = 'core.User'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT", ),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
}

DJOSER = {
    # "LOGIN_FIELD": 'email',
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    'TOKEN_MODEL': None,       # To Delete User Must Set it to None
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    # 'ACTIVATION_URL':'auth/users/activation/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/?uid={uid}&token={token}',

    'SERIALIZERS':{
        'user_create_password_retype': 'core.serializers.Djoser.UserCreateSerializer',
        'user': 'core.serializers.Djoser.UserSerializer',
        #! Can change later
        'current_user': 'core.serializers.Djoser.UserSerializer',

        "activation": "core.serializers.Djoser.ActivationSerializer",

        "password_reset_confirm": "core.serializers.Djoser.PasswordResetConfirmSerializer",

        "password_reset_confirm_retype": "core.serializers.Djoser.PasswordResetConfirmRetypeSerializer",

        "username_reset_confirm": "core.serializers.Djoser.UsernameResetConfirmSerializer",

        "username_reset_confirm_retype": "core.serializers.Djoser.UsernameResetConfirmRetypeSerializer",

        # 'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },

    'EMAIL': {
        'activation': 'core.serializers.Djoser.ActivationEmail' ,
        'confirmation': 'core.serializers.Djoser.ConfirmationEmail' ,
        'password_reset': 'core.serializers.Djoser.PasswordResetEmail' ,
        'password_changed_confirmation': 'core.serializers.Djoser.PasswordChangedConfirmationEmail' ,
    } ,


}

CURRENT_SITE = env("CURRENT_SITE")
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'from@milad.com'