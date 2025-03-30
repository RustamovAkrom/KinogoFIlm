from django.urls import path

from apps.users.api_endpoints.v1 import social_auth, auth



urlpatterns = [
    path(
        "google-auth/",
        social_auth.GoogleSocialAuthView.as_view(),
        name="google-social-auth",
    ),
    path(
        "facebook-auth/",
        social_auth.FacebookSocialAuthView.as_view(),
        name="facebook-social-auth",
    ),
    path(
        "logout/",
        auth.logout.LogoutView.as_view(),
        name="logout",
    )
]
