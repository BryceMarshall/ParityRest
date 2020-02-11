from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from homes.models import House, Room, Thermostat, Light


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'rooms']


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'house', 'current_temperature']


class ThermostatSerializer(ModelSerializer):
    class Meta:
        model = Thermostat
        fields = ['id', 'name', 'house', 'mode', 'current_temperature', 'temperature_set_point']


class LightSerializer(ModelSerializer):
    class Meta:
        model = Light
        fields = ['id', 'name', 'room', 'state']
