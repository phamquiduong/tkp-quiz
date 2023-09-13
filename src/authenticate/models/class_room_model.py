from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Tên lớp học')
    year = models.PositiveIntegerField(verbose_name='Năm học')

    def __str__(self):
        return f'{self.name}'
