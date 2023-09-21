from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """
    Custom User model for potential future features and extensions.
    """


class Post(models.Model):
    """
    Model for representing user-generated posts.
    This model represents user-generated posts with content, creation timestamp,
    and a many-to-many relationship with users who have liked the post.
    """

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(UserModel, related_name='liked_posts')


class UserRequest(models.Model):
    """
    Model for tracking user requests.
    This model is used for tracking user requests and storing timestamps to monitor user activity.
    """

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
