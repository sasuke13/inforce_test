from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken


ROLES = (
    (0, 'Employee'),
    (1, 'Admin'),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):

    first_name = models.CharField(max_length=20, default=None)
    surname = models.CharField(max_length=20, default=None)
    email = models.CharField(max_length=100, unique=True, default=None)
    password = models.CharField(max_length=255, default=None)
    role = models.IntegerField(choices=ROLES, default=0)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    refresh = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"id: {self.id}, first_name: {self.first_name}, surname: {self.surname}, email: {self.email}"

    def generate_refresh_token(self):
        refresh = RefreshToken.for_user(self)
        self.refresh_token = str(refresh)
        self.save()
        return self.refresh_token