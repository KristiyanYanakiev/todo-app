from django.contrib.auth import get_user_model
from django.db import models

from task.choices import Status

UserModel = get_user_model()
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.IN_PROGRESS
    )


