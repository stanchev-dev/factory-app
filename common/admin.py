"""Admin registrations for shared models."""

from django.contrib import admin

from .models import Department, Machine


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "department", "last_maintenance")
    list_filter = ("department",)
