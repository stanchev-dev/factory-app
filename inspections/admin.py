from django.contrib import admin
from .models import Inspection, InspectionReport


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'machine', 'next_due')


@admin.register(InspectionReport)
class InspectionReportAdmin(admin.ModelAdmin):
    list_display = ('inspection', 'performed_at', 'created_by')

