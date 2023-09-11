from django.contrib.auth import views as auth_views
from django.urls import path

from authenticate import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name="authenticate/login.html"), name='login')
]
