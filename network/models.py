from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """
    toDo
    """
    # created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(UserModel, related_name='liked_posts')


class UserRequest(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
