from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Season
from .serializers import SeasonSerializer

# GET all Seasons
@api_view(['GET'])
def season_list(request):
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)
    return Response(serializer.data)

# GET single Season
@api_view(['GET'])
def season_detail(request, year):
    try:
        season = Season.objects.get(year=year)
    except Season.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = SeasonSerializer(season)
    return Response(serializer.data)


