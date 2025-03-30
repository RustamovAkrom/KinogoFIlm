from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is deactivated")
        if not user.is_verified:
            raise serializers.ValidationError("User email is not verified. Please activate your account.")
        
        return {
            "email": user.email,
            "username": user.username,
            "tokens": user.tokens,
        }