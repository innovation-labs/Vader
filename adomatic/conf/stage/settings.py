from base import *

SITE_ID = 1

INSTALLED_APPS += (
    'rest_framework',
)

STATIC_URL = 'http://app.adomattic.com/static/'
MEDIA_URL = 'http://app.adomattic.com/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vader',
        'USER': 'django',
        'PASSWORD': 'DZn#kF^zdMcAsmytQEVKe7!w',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STRIPE_KEY = 'sk_live_ssqxfOddcsNs3wOElV6Oxoit '
