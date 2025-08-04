from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        WORKER = 'worker', 'Worker'
        MANAGER = 'manager', 'Manager'

    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.WORKER,
    )
    profile_picture = models.URLField(
        default="/static/icons/default_avatar.svg",
    )

