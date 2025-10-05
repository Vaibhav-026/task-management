from .models import TaskDetails
from rest_framework import serializers

class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDetails
        fields = '__all__'
