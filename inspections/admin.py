from django.contrib import admin

from .models import Inspection


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ("name", "interval_days", "last_performed", "next_due", "created_by")
