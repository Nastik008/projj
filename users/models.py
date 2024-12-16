from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
# Create your models here.


class StudentGroup(models.Model):
    """
    Модель группы студентов
    """
    name = models.CharField(max_length=12, verbose_name="Название")
    speciality = models.CharField(max_length=64, choices=[], verbose_name="Специальность")
    course = models.IntegerField(default=1)


class Task(models.Model):
    """
    Модель задачи ИП
    """
    number = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи")
    deadline = models.DateTimeField(verbose_name="Дедлайн")

    
class Team(models.Model):
    """
    Модель команды
    """
    number = models.IntegerField(verbose_name="Номер команды")
    name = models.CharField(max_length=255, verbose_name="Название команды", unique=True)
    project_topic = models.CharField(verbose_name="Тема проекта", max_length=255, null=True, blank=True)
    project_description = models.TextField(verbose_name="Описание проекта")
    completed_tasks = models.ManyToManyField(Task, verbose_name="Выполненные задачи", null=True, blank=True)
    max_users = models.IntegerField(verbose_name="Максимальное количество участников")


class UserProfile(models.Model):
    """
    Профиль пользователя с доп информацией
    """
    class TeamRoles(models.TextChoices):
        """
        Выборы ролей для команд
        """
        CAPTAIN = "Капитан", "Капитан"
        PARTICIPANT = "Участник", "Участник"

    class Roles(models.TextChoices):
        TRAINIG_DEPATMENT = "Учебный отдел", "Учебный отдел"
        TEACHER = "Преподаватель", "Преподаватель"
        STUDENT = "Студент", "Студент"

    # Общая часть
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE, blank=True)
    role = models.ForeignKey(Group, verbose_name="Роль", on_delete=models.CASCADE)
    tg = models.CharField(max_length=32, blank=True, null=True, verbose_name="Телеграм:")
    email = models.EmailField(max_length=32, blank=True, null=True, verbose_name="Почта:")
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name="Телефон:")
    # Часть студентов
    stud_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    team_role = models.CharField(verbose_name="Роль в команде", choices=TeamRoles.choices, blank=True, null=True, max_length=64)




