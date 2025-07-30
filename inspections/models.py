# inspections/models.py

from datetime import date

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Inspection(models.Model):
    """Represents an inspection task created by a manager."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):  # pragma: no cover - trivial string representation
        return self.title

    @property
    def days_left(self) -> int:
        """Return the remaining days until the inspection's due date."""
        return (self.due_date - date.today()).days
