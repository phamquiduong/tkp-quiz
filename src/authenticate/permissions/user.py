from rest_framework import permissions
from rest_framework.request import Request


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.group.is_teacher
