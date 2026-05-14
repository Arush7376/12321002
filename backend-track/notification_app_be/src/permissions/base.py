from rest_framework.permissions import BasePermission


class IsSystemUser(BasePermission):
    """Placeholder permission for internal service-to-service APIs."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
