from rest_framework import serializers
from .models import Contributors, Projects, Issues, Comments
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ContributorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project', 'permission', 'role']


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'description', 'author',
                  'created_time']


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ['id', 'title', 'desc', 'tag', 'priority',
                  'status', 'author', 'assignee', 'created_time']


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type']