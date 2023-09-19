from django.shortcuts import redirect


def require_teacher(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_teacher():
            return view(request, *args, **kwargs)
        return redirect('auth_home')
    return wrapper
