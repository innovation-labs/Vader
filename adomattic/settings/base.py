"""

                               ```````....`````
                          ```..-/+oosyddddso+/:..```
                        ``-/sdmNMMMMNNMMMMNNMMNNds/-``
                     ``./ymMMMMMMMMM.+.MMMNNMMMMMMMmy:``
                    ``/hNMMMMMMMMMM::++:::NNMMMMMMMMMNy-``
                   `.sNMMMMMMMMMMMMM::++::NNMMMMMMMMMMMmo.`
                  `.smmMMMMMMMMMMMMMNN``MNNMMMMMMMMMMNNNo.`
                 `.odsNMMMM adomattic NMMMNNMMMMMMMMMMdsmN+``
                ``:my-ooydNMMMMMMMMMMNNMMMNNMMMMNmmmmNd-sNm-``
                `.ym/ ```./shdmmNNMMMNNMMMNNMNho+/::::+./mMs.`
               ``-md. ``.:shmNNNNNNNNNNMMMNmdhhdmmmmy::-.yMm-``
               ``/Nh `-/oNMMMMMMMMMMNNNMMMNdmNMMMMMMMNdysdMN+``
              ```sMmshhoymdyso+++osyhdmmmNmmmhyyssssyyhhhdNMy.`
               ..yMMMmso+-.....-----..-::/:-...----..``.--+md.``
               ..dMMd/..``.-.````...--oddh+/:--.......`````:h/``
              ``-mNy.`` `--`   `.--:/..+hy//+++:`    `..` ``-o-`
              ``yNy.`` `.-`   `.+ss+.``/ys:.---.`      ..` ` -/.`
             ``/Ny``   `-.      ```````-o+.`````       `.`    .:`
            ``-mh.``   `.`  ```..--:+s::s:`-:-..````   ``      -.
           ``.hh.``        `-ooosyyo/:-:o:./yddho/:-`  ``      ``
           ``od:``       `.../+ooo+:/+osys/://+sssyo-``
          ``/d/``        `..`.``````.-yMMNs.``````..---`
         ``-do `               `.:-..:hmmmh:`` ```
        ``.ys``               `-:::-``--:+-.. `.--`               .-
        ``oy``               `...--.`:s:od:.-` `.`  ..`           .+.
       ``+y.``             `.-.```/s:od:od:+h:``   -:.`          ` +o``
      ``-y-``             `./- ..-hy/yd/sd:om/..``-:.`           ` :h-``
      ``s+ `               -s/`-//ssoyysyhsyhsso.-s+``            ` ds`.
      ``+: `               -s/.+ooossssssooo++//.-o/``           ```ds`.
        ``                  ` ``.-:///////////-`  `              `.oy.``
                                 ``-://////:--.`                `-/:.`
                                    ``.--.```                    ```


Oh! you found the pathway to the dark side of the source, my young aprentice.
Remember, The dark side of the source is a pathway to many abilities some
consider to be ..... unnatural.

Embrace it with your first lesson,

    "Without strife, your victory has no meaning.
     Without strife, you do not advance.
     Without strife, there is only stagnation."

Embrace these pearls of wisdom and get cracking ......


https://docs.djangoproject.com/en/1.7/topics/settings/
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
#from django.conf.directives import app
CONF_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(CONF_DIR, os.pardir)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$r^ufp^!he)i22(@yw#+%y&%-)t3cdvipxbz4#s)g^5gifitt-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    # import export
    'import_export',

    'registration',
    'taggit',
    'widget_tweaks',
    'corsheaders',

    #mandrill
    'djrill',

    # django photologue
    'photologue',
    'sortedm2m',
)

ADOMATIC_APPS = (
    'apps.common',
    'apps.users',
    'apps.companies',

    'apps.campaigns',
    'apps.impressions',
    'apps.brands',
    'apps.finances',

    # for front end
    'apps.dashboard',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + ADOMATIC_APPS

MIDDLEWARE_CLASSES = (
    'apps.impressions.middleware.ImpressionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adomattic.urls'

WSGI_APPLICATION = 'adomattic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Moved to local

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Static Url is to be set as per the machine
#STATIC_URL = '/static/'

# Media files (All the uploads)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Media Url is to be set as per the machine
#MEDIA_URL = '/media/'

# Authentication (and Registration-Redux)
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/users/auth/login/'
LOGOUT_URL = ''
LOGIN_REDIRECT_URL = '/dashboard/'

ACCOUNT_ACTIVATION_DAYS = 30


# For Registration process to be called from WordPress
REGISTRATION_API_KEY = 'WP_nEhj6FkTJNiFfiS5moVeUE'

# CORS Headers https://github.com/ottoyiu/django-cors-headers

#CORS_ORIGIN_REGEX_WHITELIST = (
#    '^(http?://)?(\w+\.)?adomattic\.com$',
#    '^(http?://)?localhost:9000$'
#)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken',
        'wp-api-key',
        'publisher-key',
        'access-control-allow-origin',
        'access-control-allow-credentials'
    )

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.core.context_processors.request",
        "django.contrib.messages.context_processors.messages"
    )


# Impression Engine
IMPRESSION_COOKIE_NAME = 'magneto'

# Madrill
MANDRILL_API_KEY = "US9U8XiepMg6nUVDaq5UeQ"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
ADOMATTIC_FROM = "Adomattic <noreply@adomattic.com>"

# Stripe
STRIPE_KEY = 'sk_live_ykBdrWZnCW4YddbDDxrwm0dm'

# GRAPPELLI SETTINGS
GRAPPELLI_ADMIN_TITLE = 'Adomattic Administration Console'

#MAX MIND GEO IP2 Database File Root
MAXMIND_DB_ROOT = os.path.join(CONF_DIR, 'ipdb')
MAXMIND_CITY_DB = MAXMIND_DB_ROOT + '/GeoLite2-City.mmdb'

try:
    from local import *
except ImportError:
    sys.exit('Unable to import environment specific settings, check if file local.py is properly placed')
