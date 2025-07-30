from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
            Inspection.objects.create(
                title=title,
                description=description or "",
                due_date=due_date,
                created_by=request.user,
            )
            return redirect("inspection_list")

    inspections = Inspection.objects.filter(created_by=request.user).order_by("due_date")
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
