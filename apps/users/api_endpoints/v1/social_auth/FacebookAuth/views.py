from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import FacebookSocialAuthSerializer


class FacebookSocialAuthView(GenericAPIView):
    serializer_class = FacebookSocialAuthSerializer
    permission_classes = (AllowAny, )

    def post(self, request):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = (serializer.validated_data)['auth_token']
        return Response(data, status=status.HTTP_200_OK)

    
__all__ = ("FacebookSocialAuthView", )
