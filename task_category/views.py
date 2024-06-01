from django.shortcuts import render, redirect
from .forms import CategoryForm


# Create your views here.
def add_category(req):
    if req.method == "POST":
        cta_form = CategoryForm(req.POST)
        if cta_form.is_valid():
            cta_form.save()
            return redirect("show_tasks")
    else:
        cta_form = CategoryForm()
    return render(req, "add_category.html", {"form": cta_form})
