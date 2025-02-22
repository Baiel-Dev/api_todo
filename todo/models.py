from django.db import models
from django.forms import CharField
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Priority(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)  # Заголовок задачи
    description = models.TextField(blank=True, null=True)  # Описание задачи (необязательное)
    completed = models.BooleanField(default=False)  # Статус выполнения задачи
    created_at = models.DateField(default=timezone.now)  # Дата создания задачи
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')  # null=True
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='tasks')
    def __str__(self):
        return self.title

