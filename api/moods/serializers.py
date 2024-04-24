from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from .models import MoodLog


class MoodField(serializers.FloatField):
    """ mood field in request body """
    def __init__(self, **kwargs):
        kwargs['help_text'] = "Mood between 1 and 10"
        kwargs['validators'] = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ] + kwargs.get('validators', [])
        kwargs['required'] = True
        super().__init__(**kwargs)


class MoodLogSerializer(serializers.ModelSerializer):
    """response body for mood"""
    mood = MoodField()
    time = serializers.DateTimeField(help_text="Log time for the entry",
                                     read_only=True)
    user = serializers.PrimaryKeyRelatedField(help_text="User that created log entry",
                                              read_only=True)
    comment = serializers.CharField(max_length=256,
                                    allow_blank=True,
                                    allow_null=True,
                                    required=False,
                                    help_text="Optional comment about the mood")
    latitude = serializers.DecimalField(max_digits=9,
                                        decimal_places=6,
                                        min_value=Decimal('-180.000000'),
                                        max_value=Decimal('180.000000'),
                                        required=False,
                                        help_text="Latitude of the location")
    longitude = serializers.DecimalField(max_digits=9,
                                         decimal_places=6,
                                         min_value=Decimal('-180.000000'),
                                         max_value=Decimal('180.000000'),
                                         required=False,
                                         help_text="Longitude of the location")

    class Meta:
        model = MoodLog
        fields = ['id', 'user', 'mood', 'time', 'comment', 'latitude', 'longitude']
        read_only_fields = ('user', 'time')

    def create(self, validated_data):
        request_user = self.context['request'].user
        mood_log = MoodLog.objects.create(user=request_user, **validated_data)
        return mood_log


class MoodSerializer(serializers.Serializer):
    """ request body for mood """
    mood = MoodField()
