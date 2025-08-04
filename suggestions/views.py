from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Suggestion


@login_required
def suggestion_list(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Suggestion.objects.create(text=text, created_by=request.user)
            return redirect("suggestion_list")
    suggestions = Suggestion.objects.all().order_by("created_at")
    return render(request, "suggestions/list.html", {"suggestions": suggestions})


@login_required
def vote_suggestion(request, pk, vote):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if vote == "yes":
        if suggestion.yes_voters.filter(id=request.user.id).exists():
            suggestion.yes_voters.remove(request.user)
        else:
            suggestion.no_voters.remove(request.user)
            suggestion.yes_voters.add(request.user)
    elif vote == "no":
        if suggestion.no_voters.filter(id=request.user.id).exists():
            suggestion.no_voters.remove(request.user)
        else:
            suggestion.yes_voters.remove(request.user)
            suggestion.no_voters.add(request.user)
    return redirect("suggestion_list")


@login_required
def change_suggestion_status(request, pk, status):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if (
        request.user.role == "manager"
        and status
        in [
            Suggestion.StatusChoices.APPROVED,
            Suggestion.StatusChoices.REJECTED,
            Suggestion.StatusChoices.IN_PROCESS,
        ]
    ):
        suggestion.status = status
        suggestion.save()
    return redirect("suggestion_list")


@login_required
def suggestion_history(request):
    suggestions = Suggestion.objects.filter(created_by=request.user).order_by("-created_at")
    return render(request, "suggestions/history.html", {"suggestions": suggestions})


@login_required
def delete_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if request.user.role == "manager" and request.method == "POST":
        suggestion.delete()
    return redirect("suggestion_list")

