from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


class HomeView(TemplateView):
    title = 'default'
    template_name = 'todolist/home.html'


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todolist/task_detail.html"
    get_context_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_form.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'todolist/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)







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


