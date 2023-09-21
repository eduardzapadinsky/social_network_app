from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import UserModel, Post


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer is used for serializing user data, including the user's ID,
    username, and password.
    """

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password']
        read_only_fields = ['id']

    @staticmethod
    def validate_password(value: str) -> str:
        """
        Hash value passed by the user.
        """

        return make_password(value)


class TokenSerializer(TokenObtainPairSerializer):
    """
    This serializer is used to obtain authentication tokens for users.
    """

    @classmethod
    def get_token(cls, user):
        """
        Get an authentication token for the user and update the last login timestamp.
        """

        user.last_login = now()
        user.save()
        return super().get_token(user)


class PostSerializer(serializers.ModelSerializer):
    """
    This serializer is used for serializing post data, including the post's ID,
    content, creation timestamp, owner, and likes.
    """

    class Meta:
        model = Post
        fields = ('id', 'content', 'created_at', 'owner', 'likes')
        read_only_fields = ('id', 'created_at', 'owner', 'likes')
