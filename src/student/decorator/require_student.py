from django.shortcuts import redirect


def require_student(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_student():
            return view(request, *args, **kwargs)
        return redirect('auth_home')
    return wrapper
