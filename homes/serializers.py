from rest_framework.serializers import HyperlinkedModelSerializer

from homes.models import House, Room, Thermostat, Light


class HouseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ['name']


class RoomSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'house', 'current_temperature']


class ThermostatSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Thermostat
        fields = ['name', 'house', 'mode', 'current_temperature', 'temperature_set_point']


class LightSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = ['name', 'room', 'state']
