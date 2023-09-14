import pandas as pd
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from authenticate.models import ClassRoom
from teacher.decorator.require_teacher import require_teacher
from teacher.forms.class_room_form import ClassRoomForm

User = get_user_model()


@require_teacher
def class_room(request):
    context = {}

    if request.method == 'POST':
        context['form'] = ClassRoomForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['form'] = None

    context['classes_room'] = ClassRoom.objects.all().order_by('-name')
    filter_class = request.GET.get('filter_class', None)
    if filter_class:
        context['classes_room'] = context['classes_room'].filter(name__contains=filter_class)

    return render(request, 'teacher/class.html', context=context)


@require_teacher
@require_GET
def remove_class_room(_, class_id: int):
    ClassRoom.objects.get(id=class_id).delete()
    return redirect('teacher_class')


@require_teacher
@require_GET
def class_room_student(request, class_id: int):
    context = {
        'class_id': class_id,
        'students': User.objects.filter(class_room__id=class_id),
    }
    return render(request, 'teacher/class_student.html', context)


@require_teacher
@require_POST
def class_room_student_import(request, class_id: int):
    class_room_obj = ClassRoom.objects.get(id=class_id)
    file = request.FILES["student_file"]

    data_frame = pd.read_excel(file, index_col=False, dtype=str)

    if request.POST.get('is_remove_old', None):
        User.objects.filter(class_room=class_room_obj).delete()

    for _, row in data_frame.iterrows():
        _email = row['Email']
        _password = row['Mật khẩu']
        _full_name = row['Họ và tên']
        try:
            User.objects.create_user(       # type: ignore
                email=_email,
                password=_password,
                full_name=_full_name,
                class_room=class_room_obj
            )
        except Exception:
            pass

    return redirect('teacher_class_student', class_id=class_id)
