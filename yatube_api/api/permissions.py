# yatube_api/api/permissions.py

from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
