import django_filters
from .models import TaskDetails

class TaskFilters(django_filters.FilterSet):
    class Meta:
        model = TaskDetails
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'created_at': ['gte', 'lte', 'gt', 'lt'],
        }