from pathlib import Path
import os
from dotenv import load_dotenv   ##agregdo
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(" * Direccion base es: ", BASE_DIR)



SECRET_KEY = os.getenv("SECRET_KEY")
print(" * La llave secreta es: ", SECRET_KEY)


# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = os.getenv("DEBUG", "False") == "True"
print(" * MODO DESARROLLADOR: ", DEBUG)
#DEBUG = True   #(Variable por defecto por DJango)




ALLOWED_HOSTS = ['127.0.0.1', os.getenv("ALLOWED_HOSTS")]
print(" * HOSTGING PERMITIDOS: ", ALLOWED_HOSTS)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # movido, estagba despues  del statgggicfiles, debe ir antes
    'django.contrib.staticfiles',
    'AppHome'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WhiteNoise
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


ROOT_URLCONF = 'ProyTienda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyTienda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
print(' * La base de datos es:', DATABASES)


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'  ## Se le agrego / antes

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# Esto para el Railway, para que encuntre los elementos staticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'AppHome/static')]
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # opcional, si tienes una carpeta global


STATIC_ROOT = os.path.join(BASE_DIR,'/staticfiles/')
print(' * La ruta de staticfiles es:', STATIC_ROOT)