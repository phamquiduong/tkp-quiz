from django.shortcuts import redirect


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.is_superuser:
        return redirect('teacher_home')

    return redirect('student_home')
