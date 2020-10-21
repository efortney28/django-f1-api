from rest_framework import serializers

from .models import Circuit

class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = ('id', 'name', 'image', 'turns', 'total_gp', 'location', 'description', 'first_gp_date')