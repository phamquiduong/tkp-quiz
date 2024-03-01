from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authenticate.views import RegisterUserAPIView, UserAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView().as_view(), name='auth_refresh'),
    path('verify/', TokenVerifyView().as_view(), name='auth_verify'),

    path('register', RegisterUserAPIView.as_view(), name='auth_register'),
    path('user', UserAPIView.as_view())
]
