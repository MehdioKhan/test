from rest_framework import viewsets
from . import serializers
from .models import Figure,POI,Layer,Feature


class FigureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FigureSerializer
    queryset = Figure.objects.all()


class FeatureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeatureSerializer
    queryset = Feature.objects.all()


class LayerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LayerSerializer
    queryset = Layer.objects.all()


class POIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.POISerializer
    queryset = POI.objects.all()
