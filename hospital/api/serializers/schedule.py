from rest_framework import serializers
from api.models import Schedule
from rest_framework.exceptions import ValidationError


class ScheduleSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs = ['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_start
        ).exists

        if exists:
            raise ValidationError('Возникла накладка')