from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from api.moods.models import MoodLog

User = get_user_model()


class MoodLogModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # seed data
        MoodLog.objects.create(user=cls.user, mood=1)
        MoodLog.objects.create(user=cls.user, mood=2)
        MoodLog.objects.create(user=cls.user, mood=3)

    def test_mood_log_creation(self):
        mood_entries = MoodLog.objects.all()

        # expect 3 entries
        self.assertEqual(mood_entries.count(), 3)

    def test_mood_log_ordered_by_time(self):
        MoodLog.objects.create(user=self.user, mood=4)
        first_object = MoodLog.objects.first()
        last_object = MoodLog.objects.last()

        # expect oldest to be first
        self.assertEqual(first_object.mood, 1)

        # expect most recent to be last
        self.assertEqual(last_object.mood, 4)

    def test_mood_validator(self):
        # expect values outside [1,10] to fail
        with self.assertRaises(ValidationError):
            MoodLog.objects.create(user=self.user, mood=11).full_clean()

        with self.assertRaises(ValidationError):
            MoodLog.objects.create(user=self.user, mood=-1).full_clean()
