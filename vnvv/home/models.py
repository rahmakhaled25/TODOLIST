
from django.db import models
from django.utils import timezone

class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDesc = models.TextField()
    time = models.DateTimeField(default=timezone.now)  # Set a default value

def __str__(self):
        return self.taskTitle
