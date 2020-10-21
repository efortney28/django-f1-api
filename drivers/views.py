from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer

# GET all drivers
@api_view(['GET',])
def drivers_list(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)

# GET single driver
@api_view(['GET',])
def driver_detail(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = DriverSerializer(driver)
    return Response(serializer.data)

# GET current drivers
@api_view(['GET'])
def current_driver_list(request):
    drivers = Driver.objects.filter(current_driver=True)
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)