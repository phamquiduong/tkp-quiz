import pandas as pd
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from contest.models import Contest, Question
from teacher.decorator.require_teacher import require_teacher


@require_teacher
@require_GET
def contest__question__list_view(request, contest__id: int):
    contest = Contest.objects.get(id=contest__id)
    context = {
        'contest': contest,
        'questions': Question.objects.filter(contest=contest),
    }
    return render(request, 'teacher/contest-question.html', context)


@require_teacher
@require_POST
def contest__question__import_view(request, contest__id: int):
    contest = Contest.objects.get(id=contest__id)
    file = request.FILES["question_file"]

    data_frame = pd.read_excel(file, index_col=False, dtype=str)

    if request.POST.get('is_delete_old', None):
        Question.objects.filter(contest=contest).delete()

    for _, row in data_frame.iterrows():
        _email = row['Email']
        _password = row['Mật khẩu']
        _full_name = row['Họ và tên']
        try:
            Question.objects.create_user(       # type: ignore
                email=_email,
                password=_password,
                full_name=_full_name,
                contest=contest,
            )
        except Exception:
            pass

    return redirect('teacher_contest__question__list', contest__id=contest__id)


@require_teacher
@require_POST
def contest__question__delete_view(_, contest__id: int, question__id: int):
    Question.objects.get(id=question__id).delete()
    return redirect('teacher_contest__question__list', contest__id=contest__id)
