from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

User = get_user_model()


@require_GET
def home_view(request):
    if not User.objects.all().exists():
        return render(request, 'authenticate/register.html')

    if not request.user.is_authenticated:
        return redirect('auth_login')

    if request.user.is_teacher():
        return redirect('teacher_class_room__list_create')

    return redirect('student_home')


@require_POST
def register_view(request):
    if User.objects.all().exists():
        return redirect('auth_home')

    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_superuser(email=email, password=password)   # type: ignore
    login(request, user)

    return redirect('auth_home')
