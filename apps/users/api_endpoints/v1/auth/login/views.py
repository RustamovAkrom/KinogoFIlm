from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .serializers import LoginSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        request=LoginSerializer,
        responses={200: LoginSerializer},
        description="Authentication user for email and password",
        tags=["Auth"],
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


__all__ = ("LoginView",)
