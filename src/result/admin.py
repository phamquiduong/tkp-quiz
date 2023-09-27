from django.contrib import admin

from result.models import Result


class ResultnAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'num_correct')
    list_filter = ('contest', )
    search_fields = ('user',)


admin.site.register(Result, ResultnAdmin)
