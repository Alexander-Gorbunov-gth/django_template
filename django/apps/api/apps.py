from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'

    def ready(self) -> None:
        from apps.api import admin  # noqa: F401 (unused-import)