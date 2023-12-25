from typing import Any

from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_POST

from contest.forms import ContestForm
from contest.models import Contest
from teacher.decorator.require_teacher import require_teacher


@require_http_methods(['GET', 'POST'])
@require_teacher
def contest__list_create_view(request):
    contests = Contest.objects.all().order_by('-start_time')
    now = timezone.now()

    contest__name_filter: str | None = request.GET.get('contest__name_filter', None)
    if contest__name_filter:
        contests = contests.filter(name__contains=contest__name_filter.lower())

    context: dict[str, Any] = {
        'contests': contests,
        'contests_past': contests.filter(end_time__lt=now),
        'contests_present': contests.filter(start_time__lte=now, end_time__gte=now),
        'contests_future': contests.filter(start_time__gt=now),
        'contest__name_filter': request.GET.get('contest__name_filter', None),
    }

    if request.method == 'POST':
        data = request.POST.dict()
        data['name'] = data.get('name', '').capitalize()
        data['author'] = request.user
        form = ContestForm(data)
        if form.is_valid():
            form.save()
            return redirect('teacher_contest__list_create')
        context['form'] = form

    return render(request, 'teacher/contest.html', context)


@require_teacher
@require_POST
def contest__delete_view(_, contest__id: int):
    Contest.objects.get(id=contest__id).delete()
    return redirect('teacher_contest__list_create')
