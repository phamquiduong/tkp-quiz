from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image

User = get_user_model()


class Contest(models.Model):
    COEFFICIENT = [
        (1, 'Hệ số 1'),
        (2, 'Hệ số 2'),
        (3, 'Hệ số 3'),
    ]

    name = models.CharField(max_length=255, unique=True, verbose_name='Tên cuộc thi')
    coefficient = models.PositiveSmallIntegerField(choices=COEFFICIENT, default=1, verbose_name='Hệ số')

    start_time = models.DateTimeField(verbose_name='Thời gian bắt đầu')
    end_time = models.DateTimeField(verbose_name='Thời gian kết thúc')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Người tạo cuộc thi')

    def __str__(self) -> str:
        return f'{self.name}'

    def get_num_questions(self):
        return Question.objects.filter(contest=self).count()

    class Meta:
        verbose_name = "Bài kiểm tra"
        verbose_name_plural = "Bài kiểm tra"


class Question(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name='Cuộc thi')

    content = models.TextField(verbose_name='Nội dung câu hỏi')
    image = models.ImageField(upload_to='contest/question/images/',
                              null=True, blank=True, verbose_name='Hình ảnh câu hỏi')

    difficult_level = models.PositiveSmallIntegerField(default=0, verbose_name='Độ khó')
    is_select_multiple = models.BooleanField(default=False, verbose_name='Cho phép chọn nhiều đáp án')

    def __str__(self) -> str:
        return f'{self.contest} - Question {self.id}'  # type: ignore

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 200:
                new_img = (200*img.width//img.height, 200)
                img = img.resize(new_img)
                img.save(self.image.path)

    class Meta:
        verbose_name = "Câu hỏi"
        verbose_name_plural = "Câu hỏi"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Câu hỏi')

    content = models.TextField(verbose_name='Nội dung câu trả lời')
    image = models.ImageField(upload_to='contest/answer/images/',
                              null=True, blank=True, verbose_name='Hình ảnh câu trả lời')

    is_correct = models.BooleanField(default=False, verbose_name='Đây là đáp án đúng')

    def __str__(self) -> str:
        return f'{self.question} - Answer {self.id}'  # type: ignore

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 200:
                new_img = (200*img.width//img.height, 200)
                img = img.resize(new_img)
                img.save(self.image.path)

    class Meta:
        verbose_name = "Câu trả lời"
        verbose_name_plural = "Câu trả lời"
