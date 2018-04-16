# noinspection PyUnresolvedReferences
from .settings_default import *

DATABASES = {
    'minicup': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'minicup',
        'USER': 'app',
        'PASSWORD': 'app',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'minicup_administration',
        'USER': 'app',
        'PASSWORD': 'app',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
}
