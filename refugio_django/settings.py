"""
Django settings for refugio_django project.
Configuración optimizada para despliegue en Render con PostgreSQL.
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- SEGURIDAD ---

# Clave Secreta: La toma de las variables de entorno de Render
# Si no la encuentra, usa una por defecto (solo para evitar errores, pero debes configurarla en Render)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-key-change-me-in-production')

# Debug: Falso para producción
DEBUG = False

# Hosts: Permitimos el dominio de Render
ALLOWED_HOSTS = ['*']


# --- APLICACIONES ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'usuarios',
    'animales',
    'adopciones',
    'productos',
    'servicios',
    'avisos',
    'rest_framework',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'refugio_django.urls'

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
                'django.template.context_processors.static', 
            ],
        },
    },
]

WSGI_APPLICATION = 'refugio_django.wsgi.application'


# --- BASE DE DATOS (PostgreSQL en Render) ---

# Render inyecta automáticamente la variable DATABASE_URL.
# dj_database_url la lee y configura la conexión por ti.
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True  # PostgreSQL en Render requiere SSL
    )
}


# --- VALIDACIÓN DE CONTRASEÑAS ---

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# --- INTERNACIONALIZACIÓN ---

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- ARCHIVOS ESTÁTICOS Y MEDIA (WHITENOISE) ---

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Compresión y almacenamiento eficiente para producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media (Archivos subidos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- OTROS ---

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
AUTH_USER_MODEL = 'usuarios.Usuario'

# --- SEGURIDAD CORS ---
# Permite que todos usen la API 
CORS_ALLOW_ALL_ORIGINS = True