from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .models import List


class CreateTaskView(CreateView):
    """
    Этот класс view перенаправляет на шаблон формы где мы можем создать новую задачу
    """
    model = List
    fields = '__all__'
    template_name = 'form.html'
    success_url = '/tasks/{id}'


class TaskListView(ListView):
    """
    Этот класс view позволяет нам вывести весь список задач для просмотра
    """
    model = List
    context_object_name = 'list'
    paginate_by = 5
    template_name = 'task_list.html'

class TaskDetailView(DetailView):
    """
    С помощью этого класса view мы можем детально посмотреть про каждую задачу отдельно
    """
    model = List
    context_object_name = 'list'
    template_name = 'task_detail.html'

class TaskUpdateView(UpdateView):
    """
    Этот класс view позволяет нам редактировать уже существующею задачу не удаляя её
    """
    model = List
    fields = '__all__'
    success_url = '/tasks/{id}'
    template_name = 'form.html'

class TaskDeleteView(DeleteView):
    """
    С помощью этого класса view мы можем удалять уже выполненные задачи
    """
    model = List
    template_name = 'form.html'
    success_url = '/tasks/'
