from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from .models import UserModel, Post
from .serializers import UserSerializer, TokenSerializer, PostSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class LoginView(TokenViewBase):
    serializer_class = TokenSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # Override perform_create to set the post owner.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#
#
class PostLikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        # Check if the user has already liked the post
        if user in post.likes.all():
            return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.add(user)
        return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)


class PostUnlikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User has not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        likes_analytics = (
            Post.objects
            .filter(likes__isnull=False, created_at__gte=date_from, created_at__lte=date_to)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(likes_count=Count('likes'))
            .order_by('date')
        )

        analytics_data = [
            {'date': item['date'], 'likes_count': item['likes_count']}
            for item in likes_analytics
        ]

        return JsonResponse({'analytics': analytics_data})
