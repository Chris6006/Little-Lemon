from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self,request,view):
        return bool (request.user.groups.filter(name="Manager").exists())

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)