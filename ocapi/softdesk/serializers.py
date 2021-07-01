from rest_framework import serializers
from .models import Users, Contributors, Projects, Issues, Comments


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ['id', 'user_id', 'project_id', 'permission', 'role']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type', 'author_user_id']


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['id', 'title', 'desc', 'tag', 'priority',
                  'project_id', 'status', 'author_user_id',
                  'assignee_user_id', 'created_time']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'description', 'author_user_id', 'issue_id',
                  'created_time']
