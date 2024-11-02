from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from loguru import logger

from .models import models

from django.contrib.auth import get_user_model

user = get_user_model()

