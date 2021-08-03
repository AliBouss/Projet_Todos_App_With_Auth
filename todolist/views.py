from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from todolist.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'base/task_list.html', {'tasks': tasks})


class TaskDetail(DetailView):
    model = Task
    template_name = "base/task_detail.html"
    get_context_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'


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


