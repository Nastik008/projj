# Generated by Django 5.1.3 on 2024-11-30 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Название')),
                ('speciality', models.CharField(choices=[], max_length=64, verbose_name='Специальность')),
                ('course', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер команды')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название команды')),
                ('project_topic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тема проекта')),
                ('project_description', models.TextField(verbose_name='Описание проекта')),
                ('max_users', models.IntegerField(verbose_name='Максимальное количество участников')),
                ('completed_tasks', models.ManyToManyField(blank=True, null=True, to='users.task', verbose_name='Выполненные задачи')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телеграм:')),
                ('email', models.EmailField(blank=True, max_length=32, null=True, verbose_name='Почта:')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер:')),
                ('team_role', models.CharField(blank=True, choices=[('Капитан', 'Кап')], max_length=64, null=True, verbose_name='Роль в команде')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='Роль')),
                ('stud_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.studentgroup')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
