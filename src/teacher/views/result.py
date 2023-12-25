from django.shortcuts import render
from django.views.decorators.http import require_GET

from authenticate.models import ClassRoom
from contest.models import Contest
from result.models import Result
from teacher.decorator.require_teacher import require_teacher


@require_teacher
@require_GET
def result_view(request):
    context = {
        'class_rooms': ClassRoom.objects.all().order_by('name'),
        'contests': Contest.objects.all().filter(author=request.user).order_by('-start_time')
    }

    try:
        context['results'] = Result.objects.filter(
            user__class_room__id=int(request.GET.get('class_room__id', None)),
            contest__id=int(request.GET.get('contest__id', None)),
        ).order_by('user__email')

        if request.GET.get('sort_by_point', '') == 'true':
            context['results'] = context['results'].order_by('-num_correct')
    except Exception:
        pass

    return render(request, 'teacher/result.html', context)
