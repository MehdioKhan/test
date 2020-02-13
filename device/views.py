from rest_framework import viewsets
from . import serializers
from .models import Sensor,Hardware


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SensorSerializer
    queryset = Sensor.objects.all()


class HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HardwareSerializer
    queryset = Hardware.objects.all()


