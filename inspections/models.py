# inspections/models.py

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Inspection(models.Model):
    name = models.CharField(max_length=100)
    machine = models.ForeignKey('suggestions.Machine', on_delete=models.CASCADE)
    interval_days = models.PositiveIntegerField()
    last_performed = models.DateField()
    next_due = models.DateField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InspectionReport(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    performed_at = models.DateField()
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.inspection.name} @ {self.performed_at}"

