from rest_framework.permissions import AllowAny
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from apps.users.models import User
from .serializers import RegisterSerializer


@extend_schema(
    request=RegisterSerializer,
    responses={201: RegisterSerializer},
    description="User registration using email and password",
    tags=["Auth"],
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


__all__ = ("RegisterView",)
