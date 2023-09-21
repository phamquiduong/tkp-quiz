# Generated by Django 4.2.5 on 2023-09-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_alter_answer_image_alter_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contest/answer/images/', verbose_name='Hình ảnh câu trả lời'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Tên cuộc thi'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contest/question/images/', verbose_name='Hình ảnh câu hỏi'),
        ),
    ]
