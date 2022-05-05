from rest_framework.permissions import BasePermission


class HasStore(BasePermission):
    message = "You dont have permission"

    def has_permission(self, request, view):
        if not hasattr(request.user,'store'):
            return False
        return True