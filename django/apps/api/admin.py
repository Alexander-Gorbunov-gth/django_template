from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import models


class BaseAdmin(ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at"
    )
    search_fields = ("title", )
