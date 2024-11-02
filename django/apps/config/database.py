from .params import get_settings

cfg = get_settings()


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": cfg.DB_NAME,
        "USER": cfg.DB_USER,
        "PASSWORD": cfg.DB_PASSWORD,
        "HOST": cfg.DB_HOST,
        "PORT": cfg.DB_PORT,
        "OPTIONS": {"options": f"-c search_path={cfg.DB_SCHEMAS}"},
    }
}
