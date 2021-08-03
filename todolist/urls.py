from django.contrib.auth.views import LogoutView
from django.urls import path

from todolist.views import TaskDetail, TaskCreate, task_list, TaskUpdate, TaskDelete, CustomLoginView

urlpatterns = [
    path('', task_list, name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

]