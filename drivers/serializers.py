from rest_framework import serializers

from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name', 'birthday', 'country', 'wdc', 'total_wins', 'podiums', 'current_driver', 'total_points', 'season_points', 'image', 'description')