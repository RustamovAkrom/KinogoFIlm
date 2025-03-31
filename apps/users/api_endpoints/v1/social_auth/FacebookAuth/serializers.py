from rest_framework import serializers
from ..register import register_social_user
from . import facebook_auth


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""

    auth_token = serializers.CharField(required=True)

    def validate_auth_token(self, auth_token):
        user_data = facebook_auth.Facebook.validate(auth_token)

        if "error" in user_data:
            raise serializers.ValidationError("Invalid token. please login again.")

        try:
            user_id = user_data["id"]
            email = user_data["email"]
            name = user_data["name"]
            provider = "facebook"

            data = register_social_user(
                provider=provider, user_id=user_id, email=email, name=name
            )
            return data

        except Exception:

            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        except KeyError:
            raise serializers.ValidationError("Invalid response from Facebook.")
