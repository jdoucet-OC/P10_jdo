from django.db import models


class Users(models.Model):
    """"""
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)


class Contributors(models.Model):
    """"""
    user_id = models.ForeignKey(to=Users,
                                on_delete=models.CASCADE)
    project_id = models.IntegerField()
    permission = models.CharField(max_length=128)
    role = models.CharField(max_length=128)


class Projects(models.Model):
    """"""
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)
    type = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=Users,
                                       on_delete=models.CASCADE)


class Issues(models.Model):
    """"""
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=4096)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project_id = models.IntegerField()
    status = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=Users,
                                       on_delete=models.CASCADE,
                                       related_name='author_id')
    assignee_user_id = models.ForeignKey(to=Users,
                                         on_delete=models.CASCADE,
                                         related_name='assignee_id')
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """"""
    description = models.CharField(max_length=4096)
    author_user_id = models.ForeignKey(to=Users,
                                       on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issues,
                                 on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
