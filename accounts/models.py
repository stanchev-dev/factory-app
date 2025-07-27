from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        WORKER = 'worker', 'Worker'
        MANAGER = 'manager', 'Manager'

    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.WORKER,
    )

