from django.conf import settings


def default_avatar(request):
    """Provide DEFAULT_AVATAR_URL to all templates."""
    return {"DEFAULT_AVATAR_URL": settings.DEFAULT_AVATAR_URL}
