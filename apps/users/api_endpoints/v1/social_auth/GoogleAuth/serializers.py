import os

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ..register import register_social_user
from . import google_auth


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()
    

    def validate_auth_token(self, auth_token):
        user_data = google_auth.Google.validate(auth_token)
        print(user_data)
        try:
            user_data['sub']
        except Exception:
            raise serializers.ValidationError("The token is invalid or expired. Please login again.")
        
        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise serializers.ValidationError("oops, who are you?")
        
        user_id = user_data["sub"]
        email = user_data["email"]
        name = user_data["name"]
        provider = "google"

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name
        )
