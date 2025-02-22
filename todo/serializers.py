from rest_framework import serializers
from .models import Task, Category,Priority

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id','title','description','completed','created_at','category','priority']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields = "__all__"

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"
