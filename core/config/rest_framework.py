REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.ScopedRateThrottle",
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/min",
        "user": "1000/day",
        "story": "1000/day",
    },
    # "EXCEPTION_HANDLER": "apps.shared.exceptions.custom_exception_handler",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "KinogoFill.biz API",  # Название проекта
    "VERSION": "0.0.1",  # Версия API
    "DESCRIPTION": "API для управления контентом KinogoFill.biz",  # Описание API
    "SERVE_INCLUDE_SCHEMA": False,  # Отключает `/schema` (если не нужен)
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],  # Доступ к документации
    "SWAGGER_UI_SETTINGS": {
        "filter": True,  # Включает поиск по тегам
        "persistAuthorization": True,  # Сохраняет авторизацию между запросами
        "displayRequestDuration": True,  # Показывает длительность запроса
    },
    "SORT_OPERATIONS": False,  # Отключает автоматическую сортировку эндпоинтов (если важно)
    "COMPONENT_SPLIT_REQUEST": True,  # Разделяет схемы запроса и ответа
    "ENUM_NAME_OVERRIDES": {},  # Позволяет вручную переопределять имена enum'ов
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",  # Улучшает поддержку ENUM
    ],
}