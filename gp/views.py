from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GP
from .serializers import GPSerializer

# GET all GPs
@api_view(['GET',])
def gp_list(request):
    gps = GP.objects.all()
    serializer = GPSerializer(gps, many=True)
    return Response(serializer.data)

# GET single GP
@api_view(['GET',])
def gp_detail(request, pk):
    try:
        gp = GP.objects.get(pk=pk)
    except GP.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GPSerializer(gp)
    return Response(serializer.data)
