from django.conf import settings
from django.conf.urls.i18n import i18n_patterns  # noqa: F401
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve


urlpatterns = []

if settings.DEBUG:
    from core.config.swagger import urlpatterns as swagger_patterns
    urlpatterns += swagger_patterns


# Main routes
urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("apps.shared.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("rosetta/", include("rosetta.urls")),
]

# Admin Panel (localization supported)
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
)

# Routes API (version 1)
urlpatterns += [
    path('api/v1/users/', include("apps.users.urls.v1")),
    path('api/v1/kinogo/', include("apps.kinogo.urls.v1")),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r"static/(?P<path>.*)", serve, {"document_root": settings.STATIC_ROOT}),
        re_path(r"media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
