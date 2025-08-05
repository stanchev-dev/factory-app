from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Inspection


@login_required
def inspection_list(request):
    """Allow managers to create and view inspections."""
    if getattr(request.user, "role", None) != "manager":
        return redirect("index")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        if title and due_date:
            try:
                Inspection.objects.create(
                    title=title,
                    description=description or "",
                    due_date=due_date,
                    created_by=request.user,
                )
                messages.success(request, "Inspection created successfully.")
            except Exception:
                messages.error(request, "Could not create inspection.")
            return redirect("inspection_list")
        messages.error(request, "Title and due date are required.")

    inspections = Inspection.objects.filter(created_by=request.user, checked=False).order_by("due_date")
    notifications = [
        {
            "title": i.title,
            "due_date": i.due_date.strftime("%Y-%m-%d"),
            "days_left": i.days_left,
        }
        for i in inspections
        if i.days_left <= 10
    ]
    context = {"inspections": inspections, "notifications": notifications}
    return render(request, "inspections/list.html", context)


@login_required
def inspection_check(request, pk):
    if getattr(request.user, "role", None) != "manager":
        return redirect("index")
    inspection = get_object_or_404(Inspection, pk=pk, created_by=request.user)
    if request.method == "POST":
        try:
            inspection.checked = True
            inspection.save()
            messages.success(request, "Inspection marked as completed.")
        except Exception:
            messages.error(request, "Could not update inspection.")
    return redirect("inspection_list")


@login_required
def inspection_history(request):
    if getattr(request.user, "role", None) != "manager":
        return redirect("index")
    history = Inspection.objects.filter(created_by=request.user, checked=True).order_by("due_date")
    context = {"history": history}
    return render(request, "inspections/history.html", context)


class InspectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allow managers to delete their inspections."""

    model = Inspection
    success_url = reverse_lazy("inspection_list")
    template_name = "inspections/delete.html"

    def test_func(self):
        user = self.request.user
        obj = self.get_object()
        return (
            getattr(user, "role", None) == "manager"
            and obj.created_by == user
            and obj.checked
        )
