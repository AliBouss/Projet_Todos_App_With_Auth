from django.urls import path

from todolist.views import TaskDetail, TaskCreate, task_list, TaskUpdate, TaskDelete

urlpatterns = [
    path('', task_list, name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),

]