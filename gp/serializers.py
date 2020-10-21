from rest_framework import serializers

from .models import GP

class GPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GP
        fields = ('id', 'name', 'circuit', 'start_date', 'winning_driver', 'winning_constructor', 'second_place_driver', 'third_place_driver')