# Generated by Django 4.2.5 on 2023-09-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_alter_classroom_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Quản lý lớp học', 'verbose_name_plural': 'Quản lý lớp học'},
        ),
    ]
