from django import forms
from task_category.models import CategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        
        labels = {
            "cta_name": "Category Name"
        }