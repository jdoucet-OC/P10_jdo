from rest_framework import viewsets, permissions, generics
from .serializers import (UsersSerializer, ContributorsSerializer,
                          ProjectsSerializer, IssuesSerializer,
                          CommentsSerializer)
from .models import Contributors, Projects, Issues, Comments
from django.contrib.auth.models import User


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContributorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Contributors.objects.filter(project=self.kwargs['project_pk'])


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projects.objects.all().order_by('id')
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IssuesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssuesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Issues.objects.filter(project=self.kwargs['project_pk'])


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comments.objects.filter(issue=self.kwargs['issues_pk'])


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]