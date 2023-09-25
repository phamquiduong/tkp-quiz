from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_GET

from contest.models import Contest, Question
from student.decorator.require_student import require_student


@require_GET
@require_student
def home_view(request):
    now = timezone.now()
    contests_present = Contest.objects.all().order_by('name').filter(start_time__lte=now, end_time__gte=now)
    return render(request, 'student/home.html', {'contests_present': contests_present})


@require_GET
@require_student
def taking_exam_view(request, contest__id: int):
    now = timezone.now()
    contest = Contest.objects.get(id=contest__id, start_time__lte=now, end_time__gte=now)
    questions = Question.objects.filter(contest=contest)

    context = {
        'contest': contest,
        'questions': questions,
    }

    return render(request, 'student/taking_exam.html', context)
