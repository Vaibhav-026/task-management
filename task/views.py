from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import TaskDetails
from rest_framework import status
from django.contrib.auth.models import AnonymousUser

from django.shortcuts import get_object_or_404


from rest_framework.views import APIView
from .serializer import TaskDetailsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .filter import TaskFilters

class TaskPagination(PageNumberPagination):
    page_size = 10

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = TaskPagination
    filterset_class = TaskFilters

    def get_queryset(self):
        queryset = TaskDetails.objects.all().order_by('-created_at')
        return queryset

    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin is True:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Only Admin can delete posts"}, status=status.HTTP_204_NO_CONTENT)




class TaskManagerCustomerImplementationListView(APIView):
    model = TaskDetails

    def get(self, request, *args, **kwargs):
        completed = request.query_params.get("completed")
        title = request.query_params.get("title")
        description = request.query_params.get("description")
        tasks = self.model.objects.all().order_by('-created_at')
        if completed is not None:
            tasks = tasks.filter(completed=completed.lower() == "true")
        if title:
            tasks = tasks.filter(title__icontains=title)
        if description:
            tasks = tasks.filter(description__icontains=description)

        serializer = TaskDetailsSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TaskDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskManagerCustomerImplementation(APIView):
    model = TaskDetails
    def put(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(self.model, id=task_id)
        serializer = TaskDetailsSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return Response({"error": "You must be logged in."}, status=401)
        if not request.user.is_admin:
            return Response({"message": "Only Admin can delete posts"}, status=status.HTTP_204_NO_CONTENT)
        task = get_object_or_404(self.model, id=task_id)
        task.delete()
        return Response({"message": "Task deleted"}, status=status.HTTP_204_NO_CONTENT)