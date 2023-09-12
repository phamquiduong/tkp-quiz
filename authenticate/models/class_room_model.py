from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
