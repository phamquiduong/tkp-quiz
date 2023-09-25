from typing import Any

from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from authenticate.forms import ClassRoomForm
from authenticate.models import ClassRoom
from teacher.decorator.require_teacher import require_teacher


@require_http_methods(['GET', 'POST'])
@require_teacher
def class_room__list_create_view(request):
    classes_room = ClassRoom.objects.all().order_by('name')
    class_room__name_filter: str | None = request.GET.get('class_room__name_filter', None)
    if class_room__name_filter:
        classes_room = classes_room.filter(name__contains=class_room__name_filter.upper())

    context: dict[str, Any] = {'classes_room': classes_room}

    if request.method == 'POST':
        data = request.POST.dict()
        data['name'] = data.get('name', '').upper()
        form = ClassRoomForm(data)
        if form.is_valid():
            form.save()
            return redirect('teacher_class_room__list_create')
        context['form'] = form

    return render(request, 'teacher/class_room.html', context)


@require_teacher
@require_POST
def class_room__delete_view(_, class_room__id: int):
    ClassRoom.objects.get(id=class_room__id).delete()
    return redirect('teacher_class_room__list_create')
