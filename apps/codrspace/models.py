from django.db import models
from django.contrib.auth.models import User

class CodrSpace(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    git_access_token = models.CharField(max_length=75, null=True)
    user = models.OneToOneField(User)
