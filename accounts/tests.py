from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


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


class RegistrationImageUploadTests(TestCase):
    def test_uploaded_image_used_in_profile(self):
        image = SimpleUploadedFile(
            "avatar.png", b"filecontent", content_type="image/png"
        )
        self.client.post(
            reverse("register"),
            {
                "username": "charlie",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
                "role": "worker",
                "profile_picture": image,
            },
        )
        User = get_user_model()
        user = User.objects.get(username="charlie")
        self.assertNotEqual(user.profile_picture, settings.DEFAULT_AVATAR_URL)
        self.assertTrue(user.profile_picture.endswith('.png'))
