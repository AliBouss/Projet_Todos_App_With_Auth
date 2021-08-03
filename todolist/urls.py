from django.urls import path

from todolist.views import TaskDetail, TaskCreate, task_list

urlpatterns = [
    path('', task_list, name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create")
]