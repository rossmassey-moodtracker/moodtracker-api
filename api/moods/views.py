from django.shortcuts import render
from rest_framework import viewsets
from .models import MoodLog
from .serializers import MoodLogSerializer

# Create your views here.
class MoodLogViewSet(viewsets.ModelViewSet):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer
