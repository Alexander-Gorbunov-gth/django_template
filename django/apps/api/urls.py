from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from ..api import views


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path("api-token-auth/", auth_views.obtain_auth_token),
]
