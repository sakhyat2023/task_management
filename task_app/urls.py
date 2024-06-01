from django.urls import path
from .import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("show_tasks/", views.show_tasks, name="show_tasks")
]
