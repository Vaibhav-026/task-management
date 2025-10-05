from django.db import models
from django.contrib.auth.models import AbstractUser

class TaskApplicationUser(AbstractUser):
    """"
    Task Manager application Model definition
    """
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.is_admin}"
