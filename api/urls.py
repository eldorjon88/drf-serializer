from django.urls import path
from .views import CategoryViewSet, TaskViewSet

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'})),
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'})),
]
