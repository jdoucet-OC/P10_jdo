from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (UsersSerializer, ContributorsSerializer,
                          ProjectsSerializer, IssuesSerializer,
                          CommentsSerializer)
from .models import Users, Contributors, Projects, Issues, Comments


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContributorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributors.objects.all().order_by('id')
    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projects.objects.all().order_by('id')
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated]


class IssuesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Issues.objects.all().order_by('id')
    serializer_class = IssuesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]
