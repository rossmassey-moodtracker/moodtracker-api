# Generated by Django 5.0.3 on 2024-04-24 02:09

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodlog',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='moodlog',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AddField(
            model_name='moodlog',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='moodlog',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
