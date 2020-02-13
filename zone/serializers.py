from rest_framework import serializers
from base.serializers import ListSerializer
from .models import State


class StateListSerializer(ListSerializer,serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id','name','company','activity_status')


class StateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('name','company','activity_status')
