from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def add_task(req):
    if req.method == "POST":
        task_form = TaskForm(req.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("show_tasks")
    else:
        task_form = TaskForm()
        task_form.fields.pop("is_completed")
    return render(req, "add_task.html", {"form": task_form})

def edit_task(req, id):
    data = TaskModel.objects.get(pk=id)
    if req.method == "POST":
        task = TaskForm(req.POST, instance=data)
        if task.is_valid():
            task.save()
            return redirect("show_tasks")
    else:
        task = TaskForm(instance=data)
    return render(req, "edit_task.html", {"form": task})

def delete_task(req, id):
    data = TaskModel.objects.get(pk=id)
    data.delete()
    return redirect("show_tasks")



