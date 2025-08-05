from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


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
