from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from decimal import Decimal


class MoodLog(models.Model):
    # required fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    mood = models.FloatField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])

    time = models.DateTimeField(
        default=timezone.now)

    # optional fields
    comment = models.CharField(
        null=True,
        blank=True,
        max_length=256)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal('-180.000000')),
                    MaxValueValidator(Decimal('180.000000'))])

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal('-180.000000')),
                    MaxValueValidator(Decimal('180.000000'))])

    class Meta:
        ordering = ['time']  # ascending order, use `-time` for descending
        app_label = 'moods'
