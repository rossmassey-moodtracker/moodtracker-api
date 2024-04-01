from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from .models import MoodLog


class MoodField(serializers.FloatField):
    def __init__(self, **kwargs):
        kwargs['help_text'] = "Mood between 1 and 10"
        kwargs['validators'] = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ] + kwargs.get('validators', [])
        kwargs['required'] = True
        super().__init__(**kwargs)


class MoodLogSerializer(serializers.ModelSerializer):
    mood = MoodField()
    time = serializers.DateTimeField(help_text="Log time for the entry", read_only=True)
    user = serializers.PrimaryKeyRelatedField(help_text="User that created log entry", read_only=True)

    class Meta:
        model = MoodLog
        fields = ['id', 'user', 'mood', 'time']
        read_only_fields = ('user', 'time')

    def create(self, validated_data):
        request_user = self.context['request'].user
        mood_log = MoodLog.objects.create(user=request_user, **validated_data)
        return mood_log


class MoodSerializer(serializers.Serializer):
    mood = MoodField()
