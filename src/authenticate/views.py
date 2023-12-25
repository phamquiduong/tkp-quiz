from django.shortcuts import redirect
from django.views.decorators.http import require_GET


@require_GET
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_login')

    if request.user.is_teacher():
        return redirect('teacher_class_room__list_create')

    return redirect('student_home')
