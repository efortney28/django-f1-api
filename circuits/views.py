from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Circuit
from .serializers import CircuitSerializer

# GET all circuits
@api_view(['GET',])
def circuit_list(request):
    circuits = Circuit.objects.all()
    serializer = CircuitSerializer(circuits, many=True)
    return Response(serializer.data)

# GET single circuit
@api_view(['GET',])
def circuit_detail(request, pk):
    try:
        circuit = Circuit.objects.get(pk=pk)
    except Circuit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CircuitSerializer(circuit)
    return Response(serializer.data)