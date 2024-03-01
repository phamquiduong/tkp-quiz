from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=255, unique=True)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        db_table = 'groups'
