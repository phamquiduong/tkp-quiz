from django.contrib.auth import views as auth_views
from django.urls import path

from authenticate.views import home_view, register_view

urlpatterns = [
    path('', home_view, name='auth_home'),
    path('register', register_view, name='auth_register'),
    path('login', auth_views.LoginView.as_view(template_name="authenticate/login.html"), name='auth_login'),
    path('logout', auth_views.LogoutView.as_view(next_page='auth_home'), name='auth_logout'),
]
