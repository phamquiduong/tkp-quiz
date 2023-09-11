from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Contest(models.Model):
    COEFFICIENT = [
        (1, 'Hệ số 1'),
        (2, 'Hệ số 2'),
        (3, 'Hệ số 3'),
    ]

    name = models.CharField(max_length=255)
    coefficient = models.PositiveSmallIntegerField(choices=COEFFICIENT, default=1)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
