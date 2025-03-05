from rest_framework.permissions import BasePermission

from features.users.models import BaseUser


class IsAdminOrOwner(BasePermission):
    """
    Custom permission to allow only the user themselves or an admin to delete the account.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and (request.user.is_admin or request.user == obj)
        )

class IsBaseUser(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, BaseUser)

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin