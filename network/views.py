from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
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
# class PostLikeView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def update(self, request, *args, **kwargs):
#         post = self.get_object()
#         user = request.user
#
#         if user in post.likes.all():
#             post.likes.remove(user)
#             return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
#         else:
#             post.likes.add(user)
#             return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)
#
#
# class AnalyticsView(generics.ListAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         date_from = self.request.query_params.get('date_from', None)
#         date_to = self.request.query_params.get('date_to', None)
#
#         queryset = Post.objects.annotate(like_count=Count('likes')).filter(
#             created_at__range=[date_from, date_to]
#         )
#
#         return queryset
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         data = {
#             'total_likes': queryset.aggregate(total_likes=Count('likes'))['total_likes'],
#             'analytics': [{
#                 'date': post.created_at.date(),
#                 'like_count': post.like_count
#             } for post in queryset]
#         }
#
#         return Response(data)
