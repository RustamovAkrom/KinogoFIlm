import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import GoogleSocialAuthSerializer


logger = logging.getLogger(__name__)


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer
    permission_classes = (AllowAny, )

    @extend_schema(
            request=GoogleSocialAuthSerializer,
            responses={200: GoogleSocialAuthSerializer},
            summary="Authentication for Google",
            tags=['Social Auth'],
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)
    
__all__ = ("GoogleSocialAuthView", )
