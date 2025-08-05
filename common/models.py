"""Domain models for shared factory entities."""

from django.db import models


class Department(models.Model):
    """Represents a department within the factory."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple string repr
        return self.name


class Machine(models.Model):
    """Represents a machine that belongs to a department."""

    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="machines"
    )
    last_maintenance = models.DateField(null=True, blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple string repr
        return self.name

