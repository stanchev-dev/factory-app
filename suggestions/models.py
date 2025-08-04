from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Suggestion(models.Model):
    class StatusChoices(models.TextChoices):
        IN_PROCESS = 'in_process', 'In Process'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    text = models.TextField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_PROCESS,
    )
    yes_voters = models.ManyToManyField(
        UserModel, related_name="suggestions_yes", blank=True
    )
    no_voters = models.ManyToManyField(
        UserModel, related_name="suggestions_no", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - trivial string repr
        return self.text[:20]

    @property
    def yes_votes(self) -> int:
        return self.yes_voters.count()

    @property
    def no_votes(self) -> int:
        return self.no_voters.count()

