from django.shortcuts import render

from teacher.decorator.require_teacher import require_teacher


@require_teacher
def contest(request):
    return render(request, 'teacher/contest.html')
