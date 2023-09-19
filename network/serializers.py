from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.timezone import now

from .models import UserModel, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password']
        read_only_fields = ['id']


class TokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        user.last_login = now()
        user.save()
        return super().get_token(user)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'created_at', 'owner', 'likes')
