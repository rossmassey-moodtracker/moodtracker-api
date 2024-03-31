from rest_framework import serializers
from .models import MoodLog


class MoodLogSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )

    class Meta:
        model = MoodLog
        fields = ['id', 'user', 'mood', 'time']
