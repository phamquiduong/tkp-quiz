from django.contrib.auth import login
from django.db.models import Count, OuterRef
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from contest.models import Answer, Contest, Question
from result.models import Result
from student.decorator.require_student import require_student


@require_GET
@require_student
def home_view(request):
    now = timezone.now()
    results = Result.objects.filter(user=request.user, contest__id=OuterRef('id'))
    contests = Contest.objects.annotate(
        num_question=Count('question'),
        num_correct=results.values('num_correct')[:1])

    contests_join = contests.filter(start_time__lte=now, end_time__gte=now, num_correct__isnull=True)
    contests_joined = contests.filter(num_correct__isnull=False).order_by('-start_time')

    context = {
        'contests_join': contests_join,
        'contests_joined': contests_joined,
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
        awser = request.POST.get(f'question_{question_id}', None)
        if awser is not None:
            answer_id = awser.replace('answer_', '')
            if Answer.objects.get(id=int(answer_id)).is_correct:
                result.num_correct += 1

    result.save()

    return render(request, 'student/result.html', {'result': result})


@require_http_methods(["GET", "POST"])
@require_student
def change_password(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password', None)
        if password is not None:
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('student_change_password')

    return render(request, 'student/change_password.html')
