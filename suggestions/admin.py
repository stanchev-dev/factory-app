from django.contrib import admin

from .models import Suggestion


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("text", "created_by", "status", "yes_votes", "no_votes", "created_at")
