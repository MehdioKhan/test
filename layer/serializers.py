from rest_framework import serializers
from .models import Figure,Feature,Layer,POI


class FigureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Figure
        fields = ('id','title','icon','color',
                  'marker_shape','activity_status')


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id','title','activity_status')


class LayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layer
        fields = ('id','title','features','activity_status')


class POISerializer(serializers.ModelSerializer):

    class Meta:
        model = POI
        fields = ('id','title','figure','layer',
                  'longitude','latitude')

