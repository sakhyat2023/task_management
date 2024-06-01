from django.shortcuts import render
from tasks.models import TaskModel

# Create your views here.
def home_page(req):
    return render(req, "index.html")

def show_tasks(req):
    tasks = TaskModel.objects.all()
    return render(req, "show_tasks.html", {"tasks": tasks})