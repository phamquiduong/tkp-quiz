from django.db import models


class Contest(models.Model):
    COEFFICIENT = [
        1, 'Hệ số 1',
        2, 'Hệ số 2',
        3, 'Hệ số 3',
    ]

    name = models.CharField(max_length=255)
    coefficient = models.PositiveSmallIntegerField(choices=COEFFICIENT)
