import os
import random

from django.contrib.auth import authenticate
from django.conf import settings

from apps.users.models import User


def generate_username(name, attempts=0):
    if attempts > 5:
        raise Exception("Too many attempts to generate a unique username")
    
    username = "".join(name.split(" ")).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username, attempts + 1)


def register_social_user(provider, user_id, email, name):
    user = User.objects.filter(email=email).first()

    if user and user.is_superuser:
        return {"error": "Superuser cannot log in with social authentication."}
    
    if not user:
        user = User(
            email=email,
            username=generate_username(name),
            is_social_user=True,
            is_verified=True,
        )   
        user.set_password(settings.SOCIAL_SECRET)
        user.save()

    if not user.is_social_user:
        return {"error": "Please log in using email and password."}
    
    authenticated_user = authenticate(email=user.email, password=settings.SOCIAL_SECRET)
    print(authenticated_user)

    if not user.is_active:
        return {"error": "Your account is deactivated."}
    
    if not user.is_verified:
        return {"error": "Your email is not verified."}
    
    if authenticated_user is None:
        return {"error": "Authentication failed. Please try again."}

    return {
        "email": authenticated_user.email,
        "username": authenticated_user.username,
        "token": authenticated_user.tokens
    }
