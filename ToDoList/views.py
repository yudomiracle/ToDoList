from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.paginator import Paginator

from .models import List


class CreateTaskView(CreateView):
    model = List
    fields = '__all__'
    template_name = 'form.html'
    success_url = '/tasks/{id}'


class TaskListView(ListView):
    model = List
    context_object_name = 'list'
    paginate_by = 5
    template_name = 'task_list.html'

class TaskDetailView(DetailView):
    model = List
    context_object_name = 'list'
    template_name = 'task_detail.html'

class TaskUpdateView(UpdateView):
    model = List
    fields = '__all__'
    success_url = '/tasks/{id}'
    template_name = 'form.html'
