from django.db import models

from contest.models import Contest


class Question(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)

    content = models.TextField()
    image = models.ImageField(null=True, blank=True)

    difficult_level = models.PositiveSmallIntegerField(default=0)
    is_select_multiple = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.contest} - Question {self.id}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    content = models.TextField()
    image = models.ImageField(null=True, blank=True)

    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.question} - Answer {self.id}'
