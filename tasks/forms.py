from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = "__all__"
        labels = {
            "task_description": "Description",
            "is_completed": "Completed"
        }
        
        widgets = {
            "task_description": forms.Textarea(attrs={"rows" : 5})
        }
