from django.db import models

from authenticate.models import User
from contest.models import Contest


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Học sinh")
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name="Bài thi")
    num_correct = models.PositiveSmallIntegerField(verbose_name="Số câu trả lời đúng")

    def __str__(self) -> str:
        return f"{self.user} - {self.contest} - {self.num_correct}"

    def get_score(self):
        return self.num_correct / self.contest.get_num_questions() * 10

    def get_score_round(self, ndigits: int = 1):
        return round(self.get_score(), ndigits)

    class Meta:
        verbose_name = "Kết quả cuộc thi"
        verbose_name_plural = "Kết quả cuộc thi"
