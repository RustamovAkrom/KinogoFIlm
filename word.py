# from google.auth.transport import requests
# from google.oauth2 import id_token


# class Google:

#     @staticmethod
#     def validate(auth_token):
#         try:
#             idinfo = id_token.verify_oauth2_token(
#                 auth_token, requests.Request()
#             )
#             if "accounts.google.com" in idinfo['iss']:
#                 return idinfo
        
#         except Exception:
#             return "The token is either invalid or has expired"

# import facebook


# class Facebook:

#     @staticmethod
#     def validate(auth_token):
#         try:
#             graph = facebook.GraphAPI(access_token=auth_token)
#             profile = graph.request("/me?fields=name,email")
#             return profile
#         except Exception:
#             return "The Token is invalid or expired."
        

# value = Facebook.validate("EAAIC8KAoPAsBO9QqEClPkOwNHlRM5ZAdUzvIHucD9dT4c2G2eoZCywbVqeTwZAqbuPDEoAEslL3FM1JA2WUvgwOMqtZCPbz6FhS17CwaOCZCF4XcXtdApK4wOpYZAp5F4u23S152XvyzvZBd6K6AWBxAnelaX50vdySpDQBsPKLseg1TdrQaS1GvjURvmzJDLooxu9aoWZCYtYk6ctWRjS67ZB9YhET0MHQIgxNhhIDZB9b5cZA8G87m4WQ")
# print(value)

import os

print(os.environ.get("SOCIAL_SECRET"))