import os
import random

from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User


def generate_username(name, attempts=0):
    """Генерирует уникальное имя пользователя"""
    if attempts > 5:
        raise Exception("Too many attempts to generate a unique username")
    
    username = "".join(name.split(" ")).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username, attempts + 1)


def register_social_user(provider, user_id, email, name):
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": generate_username(name),
        }
    )
    if created:
        user.set_password(settings.SOCIAL_SECRET)
        user.is_verified = True
        user.save()

    authenticated_user = authenticate(email=user.email, password=settings.SOCIAL_SECRET)

    if authenticated_user is None:
        return {"error": "Authentication failed. Please try again."}

    return {
        "email": authenticated_user.email,
        "username": authenticated_user.username,
        "token": authenticated_user.tokens
    }
