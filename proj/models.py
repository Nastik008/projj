from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    lfp_users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=25, null=True, blank=True)
    role_in_team = models.CharField(max_length=15, null=True, blank=True)
    group = models.CharField(max_length=15, null=True, blank=True)
    cont_date = models.CharField(max_length=50, null=True, blank=True)
    #use_ava = models.ImageField(upload_to="photos/%Y/%n/%d/")

class Team(models.Model):
    name_team = models.CharField(max_length=50, null=True, blank=True)
    number_team = models.IntegerField(null=True, blank=True, unique=True)
    topic = models.CharField(max_length=150, null=True, blank=True)
    desc_proj = models.CharField(max_length=200, null=True, blank=True)
    max_stud = models.IntegerField(null=True, blank=True)
    compl_task = models.TextField(null=True, blank=True)

class Tasks(models.Model):
    num_task = models.IntegerField(null=True, blank=True)
    deadline = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    task_desc = models.TextField(null=True, blank=True)