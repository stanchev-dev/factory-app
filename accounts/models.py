from django.conf import settings
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
    profile_picture = models.CharField(
        max_length=255,
        blank=True,
        default=settings.DEFAULT_AVATAR_URL,
    )


    @property
    def profile_image_url(self) -> str:
        """Return the user's profile image or the default avatar."""
        return self.profile_picture or settings.DEFAULT_AVATAR_URL

