from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from authentication.models import CustomUser
import os
from django.conf import settings


class AuthenticationTest(APITestCase):



    def setUp(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant.settings')
        settings.configure()
        self.user = CustomUser.objects.create_user(
            email='testuser@gmail.com',
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.key)

    def test_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

    def test_get_users(self):
        url = reverse('users-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
