from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from .models import UserModel, Post, UserRequest
from .serializers import UserSerializer, TokenSerializer, PostSerializer


class UserCreateView(generics.CreateAPIView):
    """
    This view allows users to register by providing a username and password.
    """

    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class LoginView(TokenViewBase):
    """
    This view allows users to obtain authentication tokens by providing valid credentials.
    """

    serializer_class = TokenSerializer


class PostCreateView(generics.CreateAPIView):
    """
    This view allows authenticated users to create posts.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Create a new post and set the owner
        """

        owner = self.request.user
        serializer.save(owner=owner)


class PostLikeView(generics.UpdateAPIView):
    """
    This view allows authenticated users to like a post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        """
        Like a post and return a response.
        """

        post = self.get_object()
        user = request.user

        # Check if the user has already liked the post
        if user in post.likes.all():
            return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.add(user)
        return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)


class PostUnlikeView(generics.UpdateAPIView):
    """
    This view allows authenticated users to unlike a post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        """
        Unlike a post and return a response.
        """

        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User has not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class AnalyticsView(APIView):
    """
    This view allows authenticated users to retrieve post analytics data
    aggregated by day within a specified date range.
    """

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


def get_user_activity_view(request, user_id):
    """
    This view allows users to retrieve activity data for a specific user,
    including their last login timestamp and the timestamp of their last request.
    """

    try:
        user_request_log = get_object_or_404(UserRequest, user_id=user_id)
        user = get_object_or_404(UserModel, id=user_id)

        response_data = {
            'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else None,
            'last_request_timestamp': user_request_log.timestamp,
        }

        return JsonResponse(response_data)
    except UserRequest.DoesNotExist:
        # Handle the case where there is no request log for the user
        return JsonResponse({'error': 'No request log found for this user.'}, status=404)
    except UserModel.DoesNotExist:
        # Handle the case where there is no user with the given user_id
        return JsonResponse({'error': 'User not found.'}, status=404)
    except Exception as e:
        # Handle any other unexpected exceptions
        return JsonResponse({'error': str(e)}, status=500)
