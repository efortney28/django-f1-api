from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'description', 'logo', 'founded', 'season_driver1', 'season_driver2', 'season_points', 'total_points', 'total_wins', 'total_titles')
        