from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

from .models import Task
from .serializers import TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-createdAt')
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

@api_view(['GET'])
def update_task_statuses(request):
    now = timezone.now()
    tasks = Task.objects.filter(status='ongoing', deadline__lt=now)
    updated_count = 0

    for task in tasks:
        task.status = 'failure'
        task.save()
        updated_count += 1

    return Response({"message": f"{updated_count} tasks updated to 'failure'"})
