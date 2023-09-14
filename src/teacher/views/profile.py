from django.shortcuts import render

from teacher.decorator.require_teacher import require_teacher


@require_teacher
def profile_view(request):
    return render(request, 'teacher/profile.html')
