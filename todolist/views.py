from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from todolist.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})


class TaskDetail(DetailView):
    model = Task
    template_name = "todolist/task_detail.html"
    get_context_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_form.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_form.html'


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')



"""
fonction based view

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'base/task_list.html', {'tasks': tasks})
    
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)

    return render(request, 'base/task_detail.html', {'tasks': tasks})

class based view

class TaskList(ListView):
    model = Task
    template_name = "base/task_list.html"
    get_context_name = "tasks"
"""


