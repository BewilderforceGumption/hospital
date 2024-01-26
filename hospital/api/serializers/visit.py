from rest_framework import serializers
from api.models import Visit, Schedule
from rest_framework.exceptions import ValidationError


class VisitCreateSerializer(serializers.ModelSerializer):
    # def validate_schedule(self, value):
    #     visit_count = value.visits.count()
    #     if 3 <= visit_count:
    #         raise ValidationError('Превышено максимальное количество мест')
    #     return value

    class Meta:
        model = Visit
        fields = ['patient', 'service', 'schedule']


class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    def validate_rating(self, value):
        if self.instance.rating_set:
            raise ValidationError('Вы уже поставили оценку')

    class Meta:
        model = Visit
        fields = ['rating']