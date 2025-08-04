from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Suggestion


User = get_user_model()


class SuggestionHistoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass")

    def test_history_shows_message_when_empty(self):
        self.client.login(username="user1", password="pass")
        response = self.client.get(reverse("suggestion_history"))
        self.assertContains(response, "user1 have not made any suggestions")

    def test_history_shows_user_suggestions(self):
        Suggestion.objects.create(text="Test suggestion", created_by=self.user)
        self.client.login(username="user1", password="pass")
        response = self.client.get(reverse("suggestion_history"))
        self.assertContains(response, "Test suggestion")
