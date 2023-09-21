from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from contest.models import Answer, Contest, Question
from teacher.decorator.require_teacher import require_teacher


@require_teacher
@require_http_methods(['GET', 'POST'])
def contest__question__list_create_view(request, contest__id: int):
    contest = Contest.objects.get(id=contest__id)
    context = {
        'contest': contest,
        'questions': Question.objects.filter(contest=contest),
    }

    if request.method == 'POST':
        data = request.POST.dict()

        def validate_request_data(data: dict[str, str]):
            form: dict[str, dict[str, str | tuple]] = {k: {'value': v} for k, v in data.items()}
            form['errors'] = {}
            if not data.get('question_content', None):
                form['errors']['Nội dung câu hỏi'] = ('Nội dung câu hỏi không được để trống',)
            if (not data.get('ans_A', None) and not data.get('ans_B', None)
                    and not data.get('ans_C', None) and not data.get('ans_D', None)):
                form['errors']['Đáp án'] = ('Phải có ít nhất 1 đáp án có nội dung',)
            if data.get('ans_correct', None) not in ('A', 'B', 'C', 'D'):
                form['errors']['Đáp án đúng'] = ('Đáp án đúng không hợp lệ',)
            if (data['ans_correct'] == 'A' and not data.get('ans_A', None)
                or data['ans_correct'] == 'B' and not data.get('ans_B', None)
                or data['ans_correct'] == 'C' and not data.get('ans_C', None)
                    or data['ans_correct'] == 'D' and not data.get('ans_D', None)):
                form['errors']['__all__'] = ((f"Bạn chọn đáp án đúng là {data['ans_correct']}."
                                              f"Tuy nhiên đán án {data['ans_correct']} không có dữ liệu"),)
            return form

        form = validate_request_data(data)
        if not form['errors']:
            question = Question.objects.create(contest=contest, content=data['question_content'])
            if data['ans_A']:
                Answer.objects.create(question=question, content=data['ans_A'], is_correct=data['ans_correct'] == 'A')
            if data['ans_B']:
                Answer.objects.create(question=question, content=data['ans_B'], is_correct=data['ans_correct'] == 'B')
            if data['ans_C']:
                Answer.objects.create(question=question, content=data['ans_C'], is_correct=data['ans_correct'] == 'C')
            if data['ans_D']:
                Answer.objects.create(question=question, content=data['ans_D'], is_correct=data['ans_correct'] == 'D')

            return redirect('teacher_contest__question__list_create', contest__id=contest__id)
        else:
            context['form'] = form

    return render(request, 'teacher/contest-question.html', context)


@require_teacher
@require_POST
def contest__question__delete_view(_, contest__id: int, question__id: int):
    Question.objects.get(id=question__id).delete()
    return redirect('teacher_contest__question__list_create', contest__id=contest__id)
