import os
import django_heroku
from decouple import config
import dj_database_url 


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

#https://www.youtube.com/watch?v=fQo9ivqX4xs
import cloudinary
import cloudinary.uploader
import cloudinary.api

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com', 'localhost']



# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'menus',
    'reservations',
    'cloudinary'
    
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'mysite.urls'

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
            ],
        },
    },
]

#https://docs.allauth.org/en/latest/installation/quickstart.html
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'mysite.wsgi.application'


# Database


import sys


# Configuration de la base de données
if 'test' in sys.argv:
    # Utilisation de SQLite pour les tests
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    # PostgreSQL pour le développement et la production
    DATABASES = {
        'default': dj_database_url.config(
            default='postgres://u13o8l34mi3nv2:pc6a399c096915def0d191bd397bb80397819a4844bfdd7e1be813615b1b3511c@c7u1tn6bvvsodf.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d6fo0p414q4spq'
        )
    }



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

ACCOUNT_EMAIL_VERIFICATION = 'none'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'studentinstitute2024@gmail.com'
EMAIL_HOST_PASSWORD = 'fmve ttzx tcjx luec'  # Utilise un mot de passe d'application
DEFAULT_FROM_EMAIL = 'studentinstitute2024@gmail.com'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True


django_heroku.settings(locals())


# Cloudinary -Django integration

cloudinary.config(
    cloud_name = "dbi9dhanq",
    api_key = "778114457955977",
    api_secret = "GytK3sofNmLZxc3ma8w8rZ-gTDk",


)