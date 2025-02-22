from rest_framework import viewsets
from .models import Task,Category,Priority
from .serializers import TaskSerializer,CategorySerializer, PrioritySerializer

class TaskAPIList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryAPIList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PriorityAPIList(viewsets.ModelViewSet):
        queryset = Priority.objects.all()
        serializer_class = PrioritySerializer