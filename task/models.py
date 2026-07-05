from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from task.choices import Status

UserModel = get_user_model()



class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

    def grouped_by_status(self, user):
        tasks = self.for_user(user)
        return {
            'pending': tasks.filter(status=Status.PENDING),
            'in_progress': tasks.filter(status=Status.IN_PROGRESS),
            'completed': tasks.filter(
                status=Status.COMPLETED,
                updated_at__gte=timezone.now() - timedelta(days=7)
            )
        }


class Task(models.Model):
    objects = TaskManager()
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


