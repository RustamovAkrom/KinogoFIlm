from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from .serializers import LogoutSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    @extend_schema(
        request=LogoutSerializer,
        responses={200: {"description": "Successfully logged out"}}
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)

        if serializer.is_valid():
            try:
                refresh_token = serializer.validated_data['refresh_token']

                if not refresh_token:
                    return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
                
                token = RefreshToken(refresh_token)
                token.blacklist()

                return Response({"message": "successfully logged out"}, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

__all__ = ("LogoutView", )
