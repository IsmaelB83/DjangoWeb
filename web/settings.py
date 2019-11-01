# coding=utf-8
"""
Django settings for web project.
Generated by 'django-admin startproject' using Django 1.11.7.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# UPLOAD PASSWORDS FILE (secret, social keys, etc.)
JSON_DATA = open(BASE_DIR + '/passwords.json')
PASSWORDS = json.load(JSON_DATA)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = PASSWORDS["secret"]

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['laestanciaazul.com', 'www.laestanciaazul.com', 'localhost', '127.0.0.1', '46.101.5.178']
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_wysiwyg',
    'social_django',
    'ckeditor',
    'category',
    'gallery',
    'user',
    'discuss',
    'post',
    'history',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'category.context_processors.categories_pre_proc',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'laestanciaazul',
        'USER': 'trama',
        'PASSWORD': PASSWORDS["database_password"],
        'HOST': 'localhost',
        'PORT': '',
    }
}'''

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# this is the local folder for statics
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# this simulates the server where statics are stored
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn/")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn/")

SESSION_EXPIRE_AT_BROWSER_CLOSE = 'false'

SESSION_COOKIE_AGE = 60 * 60  # 60 minutos

DJANGO_WYSIWYG_FLAVOR = "ckeditor"

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'

# https://github.com/settings/developers
SOCIAL_AUTH_GITHUB_KEY = PASSWORDS["github"]["key"]
SOCIAL_AUTH_GITHUB_SECRET = PASSWORDS["github"]["secret"]
# https://apps.twitter.com
SOCIAL_AUTH_TWITTER_KEY = PASSWORDS["twitter"]["key"]
SOCIAL_AUTH_TWITTER_SECRET = PASSWORDS["twitter"]["secret"]
# https://developers.facebok.com/apps
SOCIAL_AUTH_FACEBOOK_KEY = PASSWORDS["facebook"]["key"]
SOCIAL_AUTH_FACEBOOK_SECRET = PASSWORDS["facebook"]["secret"]
# https://console.developers.google.com
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = PASSWORDS["google"]["key"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = PASSWORDS["google"]["secret"]

SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/user/register'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
