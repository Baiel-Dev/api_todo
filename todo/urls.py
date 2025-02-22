from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskAPIList, CategoryAPIList, PriorityAPIList

router = DefaultRouter()
router.register(r'tasks', TaskAPIList)
router.register(r'category', CategoryAPIList)
router.register(r'priority', PriorityAPIList)

urlpatterns = [
    path('', include(router.urls)),
]