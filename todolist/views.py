from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from todolist.models import Task


class TaskList(ListView):
    model = Task
    template_name = "base/task_list.html"
    get_context_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    template_name = "base/task_detail.html"
    get_context_name = "task"


