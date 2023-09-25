import pandas as pd
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from authenticate.models import ClassRoom
from teacher.decorator.require_teacher import require_teacher

User = get_user_model()


@require_teacher
@require_GET
def class_room__student__list_view(request, class_room__id: int):
    class_room = ClassRoom.objects.get(id=class_room__id)
    context = {
        'class_room': class_room,
        'students': User.objects.filter(class_room=class_room),
    }
    return render(request, 'teacher/class_room-student.html', context)


@require_teacher
@require_POST
def class_room__student__import_view(request, class_room__id: int):
    class_room = ClassRoom.objects.get(id=class_room__id)
    file = request.FILES["student_file"]

    data_frame = pd.read_excel(file, index_col=False, dtype=str)

    if request.POST.get('is_delete_old', None):
        User.objects.filter(class_room=class_room).delete()

    for _, row in data_frame.iterrows():
        _email = row['Email']
        _password = row['Mật khẩu']
        _full_name = row['Họ và tên']
        try:
            User.objects.create_user(       # type: ignore
                email=_email,
                password=_password,
                full_name=_full_name,
                class_room=class_room,
            )
        except Exception:
            pass

    return redirect('teacher_class_room__student__list', class_room__id=class_room__id)


@require_teacher
@require_POST
def class_room__student__delete_view(_, class_room__id: int, student__id: int):
    User.objects.get(id=student__id).delete()
    return redirect('teacher_class_room__student__list', class_room__id=class_room__id)
