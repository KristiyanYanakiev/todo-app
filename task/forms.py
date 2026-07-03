from django import forms

from task.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'notes']


class UpdateTaskForm(CreateTaskForm):
    class Meta(CreateTaskForm.Meta):
        fields = ['title', 'notes', 'status']