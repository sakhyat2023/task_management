from django.db import models
from task_category.models import CategoryModel


# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel, default=None)

    def __str__(self) -> str:
        return self.task_title
