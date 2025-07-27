from django.contrib import admin
from .models import Machine, Suggestion


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'created_at')



