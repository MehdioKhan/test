from rest_framework import serializers
from .models import Sensor,Hardware


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id','activity_status')


class HardwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hardware
        fields = ('id','title','device_id','ip','sim_card',
                  'sensor_count','activity_status')



