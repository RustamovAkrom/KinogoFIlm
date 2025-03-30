from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token


class Google:

    @staticmethod
    def validate(auth_token):
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request(), settings.GOOGLE_CLIENT_ID
            )
            
            return idinfo
        
        except Exception as e:
            print(f"Google Auth Error: {e}")
            return "The token is either invalid or has expired"
