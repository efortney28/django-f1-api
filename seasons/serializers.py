from rest_framework import serializers
from .models import Season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'year', 'race1', 'race2', 'race3', 'race4', 'race5', 'race6', 'race7', 'race8', 'race9', 'race10',
            'race11', 'race12', 'race13', 'race14', 'race15', 'race16', 'race17', 'race18', 'race19', 'race20', 'race21',
            'race22', 'race23', 'race24', 'race25', 'wdc', 'wcc')
        