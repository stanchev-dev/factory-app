# inspections/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

UserModel = get_user_model()

class Inspection(models.Model):
    """Represents an inspection task created by a manager."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):  # pragma: no cover - trivial string representation
        return self.title

    @property
    def days_left(self) -> int:
        """Return the remaining days until the inspection's due date."""
        # Use Django's timezone utilities to respect the configured time zone
        return (self.due_date - timezone.localdate()).days
