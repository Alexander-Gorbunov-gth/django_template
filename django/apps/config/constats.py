from pathlib import Path

from .params import cfg


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = cfg.django.SECRET_KEY

DEBUG = cfg.django.DEBUG

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DATE_FORMAT = "%d.%m.%Y"

AUTH_USER_MODEL = "users.User"

DATE_INPUT_FORMATS = [
    "%d.%m.%Y",
]
