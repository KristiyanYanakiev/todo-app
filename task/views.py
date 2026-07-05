from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from task.choices import Status
from task.forms import CreateTaskForm, UpdateTaskForm
from task.models import Task



class TasksList(ListView):
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_tasks'] = []
        context['tasks_in_progress'] = []
        context['completed_tasks'] = []

        for task in Task.objects.filter(owner=self.request.user):
            if task.status == Status.PENDING:
                context['pending_tasks'].append(task)
            elif task.status == Status.IN_PROGRESS:
                context['tasks_in_progress'].append(task)
            else:
                if task.updated_at >= timezone.now() - timedelta(days=7):
                    context['completed_tasks'].append(task)

        return context


class ArchiveTasksView(ListView):

    template_name = 'tasks/archive.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user, status=Status.COMPLETED)


class TaskDetailsView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/details.html'

    def get_context_date(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        referer = self.request.META.get('HTTP_REFERER', '')

        if 'archive' in referer:
            context['back_to_url'] = reverse('tasks:archive')
        else:
            context['back_to_url'] = reverse('tasks:list')

        return context

class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create-task.html'
    form_class = CreateTaskForm
    model = Task
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.owner = self.request.user
        task.save()

        return super().form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('common:home')
    template_name = 'tasks/edit-task.html'
    form_class = UpdateTaskForm


class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = 'tasks/confirm_delete.html'
    model = Task







