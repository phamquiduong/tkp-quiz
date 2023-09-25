from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from contest.models import Answer, Contest, Question
from result.models import Result
from student.decorator.require_student import require_student


@require_GET
@require_student
def home_view(request):
    now = timezone.now()
    results = Result.objects.filter(user=request.user)
    contests = Contest.objects

    contests_present = contests.filter(start_time__lte=now, end_time__gte=now)
    contests_present = ((contest, results.filter(contest=contest).first()) for contest in contests_present)

    contests_past = contests.filter(end_time__lte=now)
    contests_past = ((contest, results.filter(contest=contest).first()) for contest in contests_past)

    context = {
        'contests_present': contests_present,
        'contests_past': contests_past,
    }
    return render(request, 'student/home.html', context)


@require_GET
@require_student
def taking_exam_view(request, contest__id: int):
    now = timezone.now()
    contest = Contest.objects.get(id=contest__id)

    if (
        contest.start_time > now or contest.end_time < now
        or Result.objects.filter(user=request.user, contest=contest).exists()
    ):
        return redirect('auth_home')

    questions = Question.objects.filter(contest=contest)

    context = {
        'contest': contest,
        'questions': questions,
    }

    return render(request, 'student/taking_exam.html', context)


@require_POST
@require_student
def save_exam_result_view(request, contest__id: int):
    contest = Contest.objects.get(id=contest__id)

    if Result.objects.filter(user=request.user, contest=contest).exists():
        return redirect('auth_home')

    questions = Question.objects.filter(contest=contest).values_list('id')

    result = Result(user=request.user, contest=contest, num_correct=0)

    for question_id, in questions:
        answer_id = request.POST.get(f'question_{question_id}', None).replace('answer_', '')
        if Answer.objects.get(id=int(answer_id)).is_correct:
            result.num_correct += 1

    result.save()

    return render(request, 'student/result.html', {'result': result})
