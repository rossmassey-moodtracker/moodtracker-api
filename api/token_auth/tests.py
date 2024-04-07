from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class UserViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create two users
        cls.user1 = User.objects.create_user(username='user1', password='password1')
        cls.user2 = User.objects.create_user(username='user2', password='password2')

        # create token for one user
        cls.token = Token.objects.create(user=cls.user1)

    def test_login(self):
        url = reverse('login')
        data = {'username': 'user1', 'password': 'password1'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertEqual(response.data['user']['username'], 'user1')

    def test_login_fail(self):
        url = reverse('login')
        data = {'username': 'user2', 'password': 'wrongpassword'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_signup(self):
        url = reverse('signup')
        data = {'username': 'newuser', 'password': 'newpassword', 'email': 'newuser@example.com'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')

    def test_signup_fail(self):
        url = reverse('signup')
        # user that already exists
        data = {'username': 'user1', 'password': 'password1', 'email': 'user1@example.com'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_validity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('test_token')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Token is valid'})

    def test_token_invalidity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'invalidtoken')
        url = reverse('test_token')
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
