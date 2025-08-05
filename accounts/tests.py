from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from unittest.mock import patch

from .forms import RegistrationForm


class ProfileImageURLTests(TestCase):
    def test_returns_default_when_blank(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="alice", password="password", profile_picture=""
        )
        self.assertEqual(user.profile_image_url, settings.DEFAULT_AVATAR_URL)

    def test_returns_custom_url_when_set(self):
        User = get_user_model()
        url = "/static/icons/custom.svg"
        user = User.objects.create_user(
            username="bob", password="password", profile_picture=url
        )
        self.assertEqual(user.profile_image_url, url)


class RegistrationFormTests(TestCase):
    def test_remote_image_url_validation_without_network(self):
        """Registration should succeed even if the image URL cannot be reached."""

        data = {
            "username": "charlie",
            "password1": "S0methingStr0ng!",
            "password2": "S0methingStr0ng!",
            "role": "worker",
            "secret_key": "",
            "profile_picture": "http://example.com/avatar.png",
        }

        # Simulate environments without network access by forcing urlopen to fail.
        with patch("accounts.forms.urlopen", side_effect=OSError("no network"), create=True):
            form = RegistrationForm(data)
            self.assertTrue(form.is_valid(), form.errors)
