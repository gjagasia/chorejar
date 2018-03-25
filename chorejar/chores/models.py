from django.db import models
from django.contrib.auth.models import User


class Jar(models.Model):
    """
    Containers for tasks that need to be done
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    refresh = models.IntegerField(default=168)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'chores'


class Task(models.Model):
    """
    Individual chores that need to be done
    """
    jar = models.ForeignKey(Jar, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    refresh = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'chores'


class TaskBlocker(models.Model):
    """
    Task blockers that prevent other tasks from refreshing
    Example: Empty the dishwasher
    Blocked by: Running the dishwasher
    Blocked by: Loading the dishwasher
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task')
    blocker = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='blocker')
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'chores'
