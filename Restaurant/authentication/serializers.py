from rest_framework import serializers

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

