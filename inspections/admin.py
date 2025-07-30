from django.contrib import admin

from .models import Inspection


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ("title", "due_date", "created_by")
