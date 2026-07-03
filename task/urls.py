from django.urls import path

from task.views import TasksList, ArchiveTasksView, TaskDetailsView, CreateTaskView, EditTask, DeleteTask

app_name = 'task'

urlpatterns = [

    path('list/', TasksList.as_view(), name='list'),
    path('archive/', ArchiveTasksView.as_view(), name='archive'),
    path('<int:pk>/details/', TaskDetailsView.as_view(), name='details'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('<int:pk>/edit/', EditTask.as_view(), name='edit-task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete-task')

]