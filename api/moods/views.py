from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import MoodLog
from .serializers import MoodLogSerializer, MoodSerializer


class MoodLogViewSet(viewsets.ModelViewSet):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer

    def get_queryset(self):
        """
        Only show logs made by current authenticated user.
        """
        user = self.request.user
        return MoodLog.objects.filter(user=user)

    @extend_schema(
        responses={201: MoodLogSerializer},
    )
    def list(self, request):
        """
        Gets all the recorded mood log entries.
        """
        return super().list(request)

    @extend_schema(
        request=MoodLogSerializer,
        responses={201: MoodLogSerializer}
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new mood log entry.
        """
        mood_serializer = MoodLogSerializer(data=request.data)

        if mood_serializer.is_valid():
            mood_data = mood_serializer.validated_data
            mood_log_serializer = MoodLogSerializer(data=mood_data, context={'request': request})

            if mood_log_serializer.is_valid():
                mood_log_serializer.save()
                return Response(mood_log_serializer.data, status=status.HTTP_201_CREATED)

        return Response(mood_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
