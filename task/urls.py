from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('task/', TaskListCreate.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]
