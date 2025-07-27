# inspections/models.py

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Inspection(models.Model):
    name = models.CharField(max_length=100)
    interval_days = models.PositiveIntegerField()
    last_performed = models.DateField()
    next_due = models.DateField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
