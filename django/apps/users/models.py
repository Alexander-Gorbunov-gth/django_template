from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.api.models.models import ContactModel


class User(AbstractUser):
    contact = models.ForeignKey(
        ContactModel,
        related_name="user",
        verbose_name="Контакт в битрикс",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_top_manager = models.BooleanField("Топ мэнеджер", default=False)
