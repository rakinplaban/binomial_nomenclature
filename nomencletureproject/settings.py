"""
Django settings for nomencletureproject project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import socket
# required for db choosing
from django.db import connections
from django.db.utils import OperationalError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@7m3(-5uhlwn1+&%ks5+x-*$sl*v1t0(77cc55nnt-bb!%^0-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'nomenclature',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 'allauth',
    # 'allauth.account',
    # 'django.contrib.sites',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # # 'allauth.socialaccount.providers.facebook',
    # 'crispy_forms',
    # 'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Add the account middleware:
    # "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'nomencletureproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nomencletureproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



# def check_local_db():
#     """Check if the local database is accessible."""
#     try:
#         db_conn = connections['default']
#         db_conn.cursor()  # Try to create a cursor to test the connection
#         return True  # Connection successful
#     except OperationalError:
#         return False  # Connection failed


if os.getenv('RENDER'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres.sfsdxlxpggvfcxdlynhj',
            'HOST': 'aws-0-us-east-1.pooler.supabase.com',
            'PORT': '6543',
            'PASSWORD': 'cuDgbF2lyCeIwC4u'
        }
    }
else:
    # Default to Docker configuration if not in Render
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nomencleture',
            'USER': 'postgres',
            'HOST': 'db_nomencleture',
            'PORT': '5432',
            'PASSWORD': 'qnr63363'
        }
    }


# DATABASES = {
    
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'nomencleture',
#         'USER': 'postgres',
#         'HOST': 'db_nomencleture',
#         'PORT': '5432',
#         'PASSWORD': 'qnr63363'
#     },

#     'live' : {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres.sfsdxlxpggvfcxdlynhj',
#         'HOST': 'aws-0-us-east-1.pooler.supabase.com',
#         'PORT': '6543',
#         'PASSWORD': 'cuDgbF2lyCeIwC4u'
#     }
    

#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     #     'NAME': 'postgres',
#     #     'USER': 'postgres',
#     #     'HOST': 'localhost',
#     #     'PORT': '5432',
#     #     'PASSWORD': 'qnr63363'
#     # }
# }


# if not os.getenv("USE_LOCAL_DB") and not check_local_db():
#     print("Local database not accessible. Switching to 'live' database.")
#     DATABASES['default'] = DATABASES['live']  # Use the 'live' database as default

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'nomenclature','static','images')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'nomenclature/static')
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    # 'allauth.account.auth_backends.AuthenticationBackend',
    
]

SITE_ID = 1



# SOCIALACCOUNT_PROVIDERS = {
#   'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'OAUTH_PKCE_ENABLED': True,
#         'CLIENT_ID': 'YOUR_CLIENT_ID',
#         'SECRET': 'YOUR_CLIENT_SECRET',
#     }
# }

# LOGIN_REDIRECT_URL = '/'

# CRISPY_TEMPLATE_PACK = 'bootstrap5'
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Change to 'mandatory' if you want email verification
# ACCOUNT_UNIQUE_EMAIL = True

# ACCOUNT_FORMS = {
#     'signup': 'path.to.CustomSignupForm',
# }


# Email settings (replace with your own email configuration)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Your email host
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'


LOGIN_URL = '/admin-panel/login/'
LOGIN_REDIRECT_URL = '/admin-panel/scientific-names/'  # Redirect after successful login

