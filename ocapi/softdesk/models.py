from django.db import models
from django.conf import settings


class Projects(models.Model):
    """"""
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)
    type = models.CharField(max_length=128)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       null=True)


class Contributors(models.Model):
    """"""
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Projects,
                                   on_delete=models.CASCADE)
    permission = models.CharField(max_length=128)
    role = models.CharField(max_length=128)


class Issues(models.Model):
    """"""
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=4096)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project_id = models.ForeignKey(to=Projects,
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=128)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       related_name='author_id',
                                       null=True)

    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                         on_delete=models.SET_NULL,
                                         related_name='assignee_id',
                                         null=True)

    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """"""
    description = models.CharField(max_length=4096)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       null=True)

    issue_id = models.ForeignKey(to=Issues,
                                 on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)
