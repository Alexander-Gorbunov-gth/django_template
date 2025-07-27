from .params import cfg


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": cfg.db.DB_NAME,
        "USER": cfg.db.DB_USER,
        "PASSWORD": cfg.db.DB_PASSWORD,
        "HOST": cfg.db.DB_HOST,
        "PORT": cfg.db.DB_PORT,
        "OPTIONS": {"options": f"-c search_path={cfg.db.DB_SCHEMAS}"},
    }
}
