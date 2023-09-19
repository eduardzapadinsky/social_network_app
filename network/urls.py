from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserCreateView, LoginView, PostCreateView, PostLikeView, PostUnlikeView, AnalyticsView

app_name = "network"
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('auth/', LoginView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('post/<int:pk>/dislike/', PostUnlikeView.as_view(), name='post_dislike'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]
