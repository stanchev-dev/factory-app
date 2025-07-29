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
        suggestion.yes_votes += 1
    elif vote == "no":
        suggestion.no_votes += 1
    suggestion.save()
    return redirect("suggestion_list")

