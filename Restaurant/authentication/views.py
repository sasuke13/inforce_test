from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer, UserRegistrationSerializer, TokenRefreshSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class TokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data['refresh']
        access_token = response.data['access']
        response.data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return response


# class RefreshTokenView(generics.GenericAPIView):
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#         refresh_token = request.data.get('refresh_token')
#         if not refresh_token:
#             return Response({'refresh_token': 'Refresh token is required.'}, status=400)
#         try:
#             token = RefreshToken(refresh_token)
#             access_token = str(token.access_token)
#             return Response({'access_token': access_token})
#         except Exception:
#             return Response({'refresh_token': 'Invalid refresh token.'}, status=400)


class TokenRefreshView(APIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)