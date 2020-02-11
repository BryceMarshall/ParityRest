from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from homes.models import House, Room, Thermostat, Light
from homes.serializers import HouseSerializer, RoomSerializer, ThermostatSerializer, LightSerializer


class HouseList(ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetail(RetrieveUpdateDestroyAPIView):

    def get_object(self, pk):
        try:
            return House.objects.get(name=pk)
        except:
            raise Http404

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    _lookup_field = 'name'


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ThermostatViewSet(viewsets.ModelViewSet):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer


class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer
