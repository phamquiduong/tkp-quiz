from django.urls import path

from student.views import home_view, taking_exam_view

urlpatterns = [
    path('', home_view, name='student_home'),
    path('taking_exam/<int:contest__id>', taking_exam_view, name='student_taking_exam'),
]
