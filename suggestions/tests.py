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


class SuggestionVoteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass")
        self.suggestion = Suggestion.objects.create(text="Test", created_by=self.user)
        self.client.login(username="user1", password="pass")

    def vote(self, vote):
        return self.client.get(reverse("vote_suggestion", args=[self.suggestion.id, vote]))

    def test_yes_vote_toggle(self):
        self.vote("yes")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.yes_votes, 1)
        self.vote("yes")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.yes_votes, 0)

    def test_no_vote_toggle(self):
        self.vote("no")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.no_votes, 1)
        self.vote("no")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.no_votes, 0)

    def test_switch_from_no_to_yes(self):
        self.vote("no")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.no_votes, 1)
        self.vote("yes")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.yes_votes, 1)
        self.assertEqual(self.suggestion.no_votes, 0)

    def test_switch_from_yes_to_no(self):
        self.vote("yes")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.yes_votes, 1)
        self.vote("no")
        self.suggestion.refresh_from_db()
        self.assertEqual(self.suggestion.no_votes, 1)
        self.assertEqual(self.suggestion.yes_votes, 0)
