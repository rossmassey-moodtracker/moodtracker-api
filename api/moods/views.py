from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import MoodLog
from .serializers import MoodLogSerializer


# Create your views here.
class MoodLogViewSet(viewsets.ModelViewSet):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer

    def get_queryset(self):
        """
        Only show logs made by current authenticated user.
        """
        user = self.request.user
        return MoodLog.objects.filter(user=user)

    def list(self, request):
        """
        Gets all the recorded mood log entries.
        """
        return super().list(request)

    def create(self, request, *args, **kwargs):
        """
        Create a new mood log entry.

        Expects a `mood` value between 1 and 10.
        """
        return super().create(request, *args, **kwargs)
