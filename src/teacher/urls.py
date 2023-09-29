from django.urls import path

from teacher.views.class_room import class_room__delete_view, class_room__list_create_view
from teacher.views.class_room__student import (class_room__student__delete_view, class_room__student__import_view,
                                               class_room__student__list_view)
from teacher.views.contest import contest__delete_view, contest__list_create_view
from teacher.views.contest__question import contest__question__delete_view, contest__question__list_create_view
from teacher.views.home import home_view
from teacher.views.result import result_view

urlpatterns = [
    path('', home_view, name='teacher_home'),

    path('class_room', class_room__list_create_view, name='teacher_class_room__list_create'),
    path('class_room/<int:class_room__id>/delete', class_room__delete_view, name='teacher_class_room__delete'),

    path('class_room/<int:class_room__id>/student', class_room__student__list_view,
         name='teacher_class_room__student__list'),
    path('class_room/<int:class_room__id>/student/import', class_room__student__import_view,
         name='teacher_class_room__student__import'),
    path('class_room/<int:class_room__id>/student/<int:student__id>/delete', class_room__student__delete_view,
         name='teacher_class_room__student__delete'),

    path('contest', contest__list_create_view, name='teacher_contest__list_create'),
    path('contest/<int:contest__id>/delete', contest__delete_view, name='teacher_contest__delete'),

    path('contest/<int:contest__id>/question', contest__question__list_create_view,
         name='teacher_contest__question__list_create'),
    path('contest/<int:contest__id>/question/<int:question__id>/delete', contest__question__delete_view,
         name='teacher_contest__question__delete'),

    path('result', result_view, name='teacher_result'),
]
