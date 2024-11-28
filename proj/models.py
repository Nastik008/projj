from django.db import models
from django.contrib.auth.models import User, Group
#
# class Users(models.Model):
#     username = models.CharField(max_length=30, null=True, blank=True)
#     password = models.CharField(max_length=20, null=True, blank=True)
#     lfp_users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     role = models.CharField(max_length=25, null=True, blank=True)
#     role_in_team = models.CharField(max_length=15, null=True, blank=True)
#     group = models.CharField(max_length=15, null=True, blank=True)
#     cont_date = models.CharField(max_length=50, null=True, blank=True)
#     #use_ava = models.ImageField(upload_to="photos/%Y/%n/%d/")


class UserProfile(models.Model):
    class CommandRoles(models.TextChoices):
        CAPTAIN = "Капитан", "Капитан"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.CASCADE)
    command_role = models.CharField(max_length=128, choices=CommandRoles.choices, blank=True, null=True)
    stud_group = models.CharField()

class Task(models.Model):
    number = models.IntegerField(null=True, blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название команды")
    number = models.IntegerField(unique=True)
    topic = models.CharField(max_length=150, verbose_name="Тема проекта", null=True, blank=True)
    desc_proj = models.CharField(max_length=200, verbose_name="Описание проекта", null=True, blank=True)
    max_stud = models.IntegerField(default=5)
    completed_tasks = models.ManyToManyField(Task, blank=True)


def set_options(name, age, *args, **kwargs):
    pass


set_options("artem", 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, k=3, z=5, l=6)