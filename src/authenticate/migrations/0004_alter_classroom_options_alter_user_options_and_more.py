# Generated by Django 4.2.5 on 2023-09-16 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_alter_classroom_name_alter_classroom_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Lớp học', 'verbose_name_plural': 'Lớp học'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Người dùng', 'verbose_name_plural': 'Người dùng'},
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='year',
        ),
        migrations.AlterField(
            model_name='user',
            name='class_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authenticate.classroom', verbose_name='Lớp học'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Thời gian được tạo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Họ và tên'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Trạng thái hoạt động'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Truy cập được trang quản trị'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tên'),
        ),
    ]