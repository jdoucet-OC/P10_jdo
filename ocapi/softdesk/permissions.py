from rest_framework import permissions
from .models import Contributors, Projects, Issues, Comments


class IsAuthor(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method == 'POST':
            return True
        elif Contributors.objects.filter(
                user=request.user, project=obj).exists():
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                permission = Contributors.objects.get(user=request.user,
                                                      project=obj).permission
                return permission == "author"
        else:
            return False


class IsContributor(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method in permissions.SAFE_METHODS\
                or request.method == 'POST':

            if isinstance(obj, Projects):
                project = obj
                return Contributors.objects.filter(user=request.user,
                                                   project=project).exists()
            elif isinstance(obj, Issues):
                project = obj.project
                return Contributors.objects.filter(user=request.user,
                                                   project=project).exists()
            elif isinstance(obj, Comments):
                project = obj.issue.project
                return Contributors.objects.filter(user=request.user,
                                                   project=project).exists()
        else:
            return obj.author == request.user