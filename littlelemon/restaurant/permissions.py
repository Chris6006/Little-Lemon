from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
       if request.user.groups.filter(name='Manager').exists():
            return True

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)