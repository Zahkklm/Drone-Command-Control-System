from rest_framework import permissions

class IsOperatorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.auth and
            request.auth.get('role') in ['operator', 'admin']
        )