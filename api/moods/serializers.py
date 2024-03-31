from rest_framework import serializers
from .models import MoodLog


class MoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodLog
        fields = ['id', 'user', 'mood', 'time']
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        mood_log = MoodLog.objects.create(user=user, **validated_data)
        return mood_log