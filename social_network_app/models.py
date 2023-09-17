from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserModel(AbstractUser):
    """
    toDo
    """
    created_at = models.DateTimeField(auto_now_add=True)
    last_time_login = models.DateTimeField(default=timezone.now)
    last_time_request = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(UserModel, related_name='liked_posts')
