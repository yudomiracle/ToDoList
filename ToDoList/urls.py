from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.CreateTaskView.as_view(), name='task_create'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete')
]