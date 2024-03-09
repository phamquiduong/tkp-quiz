from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authenticate.views import GroupsAPIView, GroupsListAPIView, RegisterUserAPIView, UserAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView().as_view(), name='auth_refresh'),
    path('verify/', TokenVerifyView().as_view(), name='auth_verify'),

    path('register', RegisterUserAPIView.as_view(), name='auth_register'),
    path('user', UserAPIView.as_view(), name='auth_get_user_info'),
    path('groups', GroupsListAPIView.as_view()),
    path('groups/<int:pk>/', GroupsAPIView.as_view()),
]
