from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task_app.urls")),
    path("task_category/", include("task_category.urls")),
    path("tasks/", include("tasks.urls")),
]
