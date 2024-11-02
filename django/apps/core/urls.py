from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

handler403 = 'apps.pages.views.csrf_failure'
handler404 = "apps.pages.views.page_not_found"
handler500 = "apps.pages.views.server_error"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include("apps.pages.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("api/", include("apps.api.urls")),
    path("", include("apps.partner_pages.urls")),
]
