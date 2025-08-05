"""Views for shared pages and simple CRUD helpers."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import DepartmentForm, MachineForm
from .models import Department, Machine

class HomeView(TemplateView):
    template_name = 'index.html'


@login_required
def department_list(request):
    """List departments and allow managers to create new ones."""

    form = DepartmentForm(request.POST or None)
    if request.method == "POST" and getattr(request.user, "role", None) == "manager":
        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully.")
            return redirect("department_list")
        messages.error(request, "Please correct the errors below.")
    departments = Department.objects.all().order_by("name")
    context = {"form": form, "departments": departments}
    return render(request, "common/departments.html", context)


@login_required
def machine_list(request):
    """List machines and allow managers to create them."""

    form = MachineForm(request.POST or None)
    if request.method == "POST" and getattr(request.user, "role", None) == "manager":
        if form.is_valid():
            form.save()
            messages.success(request, "Machine added successfully.")
            return redirect("machine_list")
        messages.error(request, "Please correct the errors below.")
    machines = Machine.objects.select_related("department").all().order_by("name")
    context = {"form": form, "machines": machines}
    return render(request, "common/machines.html", context)
