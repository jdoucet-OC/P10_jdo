from rest_framework import viewsets, permissions, generics, status
from .serializers import (UsersSerializer, ContributorsSerializer,
                          ProjectsSerializer, IssuesSerializer,
                          CommentsSerializer)
from .models import Contributors, Projects, Issues, Comments
from django.contrib.auth.models import User
from rest_framework.response import Response
from .permissions import IsContributor, IsAuthor


class RegisterUser(generics.CreateAPIView):
    """"""
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]


class ContributorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contributors to be viewed or edited.
    """

    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """"""
        return Contributors.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        """"""
        try:
            user = User.objects.get(username=request.data['user'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        project = Projects.objects.get(id=kwargs['project_pk'])
        data = {'user': user.id,
                'project': project.id,
                'permission': 'contributor'}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Projects.objects.all().order_by('id')
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def create(self, request):
        """"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            author = Contributors(user=request.user,
                                  project=project,
                                  permission='author')
            author.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class IssuesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows issues to be viewed or edited.
    """
    serializer_class = IssuesSerializer
    permission_classes = [permissions.IsAuthenticated, IsContributor]

    def get_queryset(self):
        """"""
        return Issues.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        """"""
        author = request.user
        project = Projects.objects.get(id=kwargs['project_pk'])
        self.check_object_permissions(request, project)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(project=project,
                            author=author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """

    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated, IsContributor]

    def get_queryset(self):
        """"""
        return Comments.objects.filter(issue=self.kwargs['issues_pk'])

    def create(self, request, *args, **kwargs):
        """"""
        issue = Issues.objects.get(id=kwargs['issues_pk'])
        author = request.user
        serializer = self.serializer_class(data=request.data)
        self.check_object_permissions(request, issue.project)
        if serializer.is_valid(raise_exception=True):
            serializer.save(issue=issue,
                            author=author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
