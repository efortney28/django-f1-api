from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer

# GET all teams
@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

# GET single team
@api_view(['GET'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TeamSerializer(team)
    return Response(serializer.data)

# GET current Teams
@api_view(['GET'])
def current_teams_list(request):
    teams = Team.objects.filter(current=True)
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)