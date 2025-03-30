import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()


from rest_framework_simplejwt.tokens import RefreshToken

token_in_blacklist = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzkxNDI1MCwiaWF0IjoxNzQzMzA5NDUwLCJqdGkiOiI3NTIwODQ1ZmEwZjc0OTJiOWU1ODU3NjhjNGFiZDhkYyIsInVzZXJfaWQiOjN9.vE-fgNC1qqk-bbnYxrQHWei8SMQgluZbj3CiHxxaj4Y"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzkxNTIxNCwiaWF0IjoxNzQzMzEwNDE0LCJqdGkiOiIzNmNiYTYxZjM2N2M0MjljODJjNzllNmI4Y2VhNzA5OCIsInVzZXJfaWQiOjN9.jYVArj9TFmcQLt_GiOIL64tKW0jtrStgF9vuEzHy5ok"
refresh = RefreshToken(token)
print(refresh.access_token)