from django.db import models


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(
        "Запись создана", auto_now_add=True, blank=True
    )
    updated_at = models.DateTimeField(
        "Последнее изменение", auto_now=True, blank=True
    )

    class Meta:
        abstract = True