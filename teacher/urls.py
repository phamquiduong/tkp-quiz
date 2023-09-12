from django.urls import path

from teacher import views

urlpatterns = [
    path('', views.home, name='teacher_home'),
    path('class', views.class_room, name='teacher_class'),
    path('contest', views.contest, name='teacher_contest'),
    path('profile', views.profile, name='teacher_profile'),
]
