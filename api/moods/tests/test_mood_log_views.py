from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.moods.models import MoodLog

User = get_user_model()


class MoodLogViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.first_user = User.objects.create_user(username='user1', password='pass1')
        cls.second_user = User.objects.create_user(username='user2', password='pass2')

        MoodLog.objects.create(user=cls.first_user, mood=1)
        MoodLog.objects.create(user=cls.first_user, mood=2)
        MoodLog.objects.create(user=cls.first_user, mood=3)

        MoodLog.objects.create(user=cls.second_user, mood=1)

    def setUp(self):
        self.client.login(username='user1', password='pass1')

    def test_read_mood_logs(self):
        url = reverse('moodlog-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # should only see `user1` logs
        self.assertEqual(len(response.data['results']), 3)

    def test_create_mood_log(self):
        url = reverse('moodlog-list')
        data = {'mood': 4}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mood'], 4)

    def test_create_mood_log_invalid_data(self):
        url = reverse('moodlog-list')

        # expect non-float to fail
        bad_data = {'mood': 'cat'}
        response = self.client.post(url, bad_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # expect values outside [1,10] to fail
        bad_data_2 = {'mood': -100}
        response = self.client.post(url, bad_data_2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        bad_data_3 = {'mood': 100}
        response = self.client.post(url, bad_data_3)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
