from django.contrib import admin

from contest.models import Answer, Contest, Question

# Register your models here.
admin.site.register([Contest, Question, Answer])
