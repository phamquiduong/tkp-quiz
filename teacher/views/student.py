from django.shortcuts import render

from authenticate.models import ClassRoom
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

    context['classes_room'] = ClassRoom.objects.all()
    filter_class = request.GET.get('filter_class', None)
    if filter_class:
        context['classes_room'] = context['classes_room'].filter(name__contains=filter_class)

    return render(request, 'teacher/class.html', context=context)
