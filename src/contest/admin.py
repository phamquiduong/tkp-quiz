from django.contrib import admin

from contest.models import Answer, Contest, Question


class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'coefficient', 'start_time', 'end_time', 'author',)
    list_filter = ('coefficient', )
    search_fields = ('name',)
    ordering = ('start_time',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('contest', 'content', 'difficult_level')
    list_filter = ('contest', )
    search_fields = ('content',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'image', 'is_correct',)
    list_filter = ('question', )
    search_fields = ('content',)


admin.site.register(Contest, ContestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
