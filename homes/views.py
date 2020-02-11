from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from homes.models import House, Room, Thermostat, Light
from homes.serializers import HouseSerializer, RoomSerializer, ThermostatSerializer, LightSerializer

@method_decorator(login_required, name='dispatch')
class HouseList(ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

@method_decorator(login_required, name='dispatch')
class HouseDetail(RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ThermostatViewSet(viewsets.ModelViewSet):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer


class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer
