from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token




class WebhookPermission(BasePermission):
    """Доступ через апи ключ в вебхуке"""

    def has_permission(self, request, view):
        slug = view.kwargs.get("slug")
        if not slug:
            return False
        try:
            pers = Token.objects.get(key=slug)
            if pers:
                return True
            return False
        except Token.DoesNotExist:
            return False
