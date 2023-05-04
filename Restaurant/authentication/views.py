from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer, UserRegistrationSerializer, TokenRefreshSerializer
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomLoginView(generics.GenericAPIView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            refresh = CustomTokenObtainPairSerializer.get_token(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

# class TokenPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         refresh_token = response.data['refresh']
#         access_token = response.data['access']
#         response.data = {
#             'access_token': access_token,
#             'refresh_token': refresh_token,
#         }
#         return response


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