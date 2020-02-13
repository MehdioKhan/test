from rest_framework import viewsets
from .models import Vehicle,VehicleGroup,Driver
from . import serializers


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DriverSerializer
    queryset = Driver.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleGroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VehicleGroupSerializer
    queryset = VehicleGroup.objects.all()
