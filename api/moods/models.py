from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class MoodLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mood = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']
        app_label = 'moods'
