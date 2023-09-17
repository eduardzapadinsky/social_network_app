from rest_framework import serializers
from .models import UserModel, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'created_at', 'last_time_login', 'last_time_request')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'created_at', 'owner', 'likes')
