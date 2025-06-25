from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, update_task_statuses

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<uuid:id>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('update-status/', update_task_statuses),
]
