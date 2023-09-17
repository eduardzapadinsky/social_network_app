from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt

from .views import UserCreateView, PostCreateView, PostLikeView, AnalyticsView

router = routers.DefaultRouter()
# router.register('', UserCreateView)

app_name = "network"
urlpatterns = [
    # path('auth/', jwt., name='user_signup'),
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]
