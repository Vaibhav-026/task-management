from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskManagerCustomerImplementation, TaskManagerCustomerImplementationListView

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('task-custom/', TaskManagerCustomerImplementationListView.as_view(), name='task-manager'),
    path('task-custom/<int:task_id>/', TaskManagerCustomerImplementation.as_view(), name='task-details'),
]
