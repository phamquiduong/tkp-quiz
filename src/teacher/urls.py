from django.urls import path

from teacher import views

urlpatterns = [
    path('', views.home, name='teacher_home'),

    # Classroom get and create
    path('class', views.class_room_view, name='teacher_class'),
    # Classroom delete
    path('class/<int:class_id>/remove', views.remove_class_room, name='teacher_class_remove'),

    # Classroom student get and create
    path('class/<int:class_id>/student', views.class_room_student, name='teacher_class_student'),
    path('class/<int:class_id>/student/import', views.class_room_student_import, name='teacher_class_student_import'),
    path('class/<int:class_id>/student/<int:student_id>/remove',
         views.class_student_remove, name='teacher_class_student_remove'),

    path('contest', views.contest, name='teacher_contest'),
    path('profile', views.profile, name='teacher_profile'),
]
