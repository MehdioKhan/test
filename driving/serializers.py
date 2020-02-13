from rest_framework import serializers
from .models import Driver,Vehicle,VehicleGroup


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id','first_name','last_name','nid','tel')


class VehicleGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleGroup
        fields = ('id','group_name','activity_status')


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('id','title','number_plate','figure','vehicle_group',
                  'driver','state','activity_status','service_status')
