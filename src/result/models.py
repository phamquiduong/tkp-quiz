from django.db import models

from authenticate.models import User
from contest.models import Contest


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    num_correct = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.user} - {self.contest} - {self.num_correct}"

    def get_score(self):
        return self.num_correct / self.contest.get_num_questions() * 10
