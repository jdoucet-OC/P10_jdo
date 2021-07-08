from django.db import models
from django.conf import settings


class Projects(models.Model):
    """"""
    type_choice = [
        ('project', 'Project'),
        ('product', 'Product'),
        ('application', 'Application'),
    ]
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)
    type = models.CharField(max_length=128, choices=type_choice)


class Contributors(models.Model):
    """"""
    permission_choice = [
        ('author', 'Author'),
        ('contributor', 'Contributor'),
    ]
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    project = models.ForeignKey(to=Projects,
                                on_delete=models.CASCADE)
    permission = models.CharField(max_length=128,
                                  choices=permission_choice,
                                  default='contributor')
    role = models.CharField(max_length=128, default='role')


class Issues(models.Model):
    """"""
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=4096)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project = models.ForeignKey(to=Projects,
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=128)

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               related_name='author_id',
                               null=True)

    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 related_name='assignee_id',
                                 null=True)

    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """"""
    description = models.CharField(max_length=4096)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL,
                               null=True)

    issue = models.ForeignKey(to=Issues,
                              on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)