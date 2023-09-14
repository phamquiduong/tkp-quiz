from django.shortcuts import redirect
from django.views.decorators.http import require_GET


@require_GET
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_login')

    if request.user.is_superuser:
        return redirect('teacher_home')

    return redirect('student_home')
