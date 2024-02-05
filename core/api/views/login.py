from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.serializers.login import LoginUserSerializer


class LoginUserView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post( self, request ):
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data, status = status.HTTP_200_OK)