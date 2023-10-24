from django.urls import path

from student.views import change_password, home_view, save_exam_result_view, taking_exam_view

urlpatterns = [
    path('', home_view, name='student_home'),
    path('taking_exam/<int:contest__id>', taking_exam_view, name='student_taking_exam'),
    path('save_exam_result_view/<int:contest__id>', save_exam_result_view, name='student_save_exam_result'),
    path('change_password', change_password, name='student_change_password'),
]
