from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from users.serializers import TaskManagerRegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TaskManagerRegisterSerializer
