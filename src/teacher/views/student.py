from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

from authenticate.models import ClassRoom, User
from teacher.decorator.require_teacher import require_teacher
from teacher.forms.class_room_form import ClassRoomForm


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
        'students': User.objects.filter(class_room__id=class_id)
    }
    return render(request, 'teacher/class_student.html', context)
