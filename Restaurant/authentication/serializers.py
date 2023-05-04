from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


from authentication.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'surname', 'email', 'password', 'role']

    def create(self, validated_data):
        try:
            CustomUser.objects.get(email=validated_data["email"])
            raise serializers.ValidationError({f"User with email - {validated_data['email']} - is already registered"})
        except CustomUser.DoesNotExist:
            pass
        user = CustomUser.objects.create(**validated_data)
        user.set_password(self.validated_data["password"])
        user.is_active = True
        if self.validated_data["role"] == 1:
            user.is_staff = True
            user.is_superuser = True
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.email
        # token['email'] = user.email
        token['password'] = user.password
        return token

# class CustomTokenObtainPairSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style= {"input_type": "password"}, write_only=True)
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#
#         if email and password:
#             try:
#                 user = CustomUser.objects.get(email=email)
#             except CustomUser.DoesNotExist:
#                 raise serializers.ValidationError('User with given email does not exist')
#             else:
#                 if not user.check_password(password):
#                     raise serializers.ValidationError('Invalid password')
#         else:
#             raise serializers.ValidationError('Email and password are required')
#
#         refresh = RefreshToken.for_user(user)
#
#         data = {}
#         data['access'] = str(refresh.access_token)
#         data['refresh'] = str(refresh)
#         user.refresh = data['refresh']
#         user.save()
#         return data


class TokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        data = {'access': str(refresh.access_token)}
        return data
