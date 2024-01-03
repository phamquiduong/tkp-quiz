import pandas as pd
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from unidecode import unidecode

from app_core.logger import logger
from authenticate.models import ClassRoom
from contest.models import Contest
from result.models import Result
from teacher.decorator.require_teacher import require_teacher


@require_teacher
@require_http_methods(['GET', 'POST'])
def result_view(request):
    context = {
        'class_rooms': ClassRoom.objects.all().order_by('name'),
        'contests': Contest.objects.all().filter(author=request.user).order_by('-start_time')
    }

    try:
        class_room__id = int(request.GET.get('class_room__id', None))
        contest__id = int(request.GET.get('contest__id', None))
        is_sort_point = request.GET.get('sort_by_point', '') == 'true'

        results = Result.objects \
            .filter(user__class_room__id=class_room__id, contest__id=contest__id) \
            .order_by(*(['-num_correct'] if is_sort_point else []), 'user__email')

        context.update({
            'class_room__id': class_room__id,
            'contest__id': contest__id,
            'sort_by_point': is_sort_point,
            'results': results,
        })

        if request.method == 'POST' and results.exists():
            return __export_excel_file(results)
    except Exception as ex:
        logger.error(f'Error exporting result. Detail: {type(ex)} {ex}\n')

    return render(request, 'teacher/result.html', context)


def __export_excel_file(results: BaseManager[Result]):
    result = results.first()
    file_name = f'TKP Quiz - Ket qua - {result.user.class_room.name} - {unidecode(result.contest.name)}'

    df = pd.DataFrame([[result.user.email, result.user.full_name, result.num_correct, result.get_score_round()]
                       for result in results], columns=['Email', 'Họ và tên', 'Số câu đúng', 'Điểm số'])

    response = HttpResponse(content_type="application/xlsx; charset=UTF-8")
    response['Content-Disposition'] = f'attachment; filename="{unidecode(file_name)}.xlsx"'
    with pd.ExcelWriter(response) as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
    return response
