from django.contrib.gis.gdal.prototypes.ds import GDAL_OF_ALL
from django.db import models
from django.views.decorators.http import require_GET


# Create your models here.
class TaskDetails(models.Model):
    """
    Model that will hold details of tasks in system
    """
    title = models.CharField(max_length=500, null=False)
    description = models.TextField(null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.description}"