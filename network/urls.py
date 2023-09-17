from django.urls import path
from .views import UserCreateView, PostCreateView, PostLikeView, AnalyticsView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]
