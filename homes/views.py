from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from homes.models import House, Room, Thermostat, Light, ThermostatState, RoomState, LightState
from homes.serializers import HouseSerializer, RoomSerializer, ThermostatSerializer, LightSerializer


@method_decorator(login_required, name='dispatch')
class ListView(ListCreateAPIView):
    pass


@method_decorator(login_required, name='dispatch')
class DetailView(RetrieveUpdateDestroyAPIView):
    pass


class HouseList(ListView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetail(DetailView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class RoomList(ListView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        room = serializer.validated_data
        dataPoint = RoomState(current_temperature=room['current_temperature'], name=room['name'],
                              timestamp=timezone.now())
        dataPoint.save()
        serializer.save()


class RoomDetail(DetailView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


    def perform_update(self, serializer):
        room = serializer.validated_data
        dataPoint = RoomState(current_temperature=room['current_temperature'], name=room['name'],
                              timestamp=timezone.now())
        dataPoint.save()
        serializer.save()


class ThermostatList(ListView):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer

    def perform_create(self, serializer):
        thermo = serializer.validated_data
        dataPoint = ThermostatState(mode=thermo['mode'], current_temperature=thermo['current_temperature'],
                                    temperature_set_point=thermo['temperature_set_point'], name=thermo['name'])
        dataPoint.save()
        serializer.save()


class ThermostatDetail(DetailView):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer

    def perform_update(self, serializer):
        thermo = serializer.validated_data
        dataPoint = ThermostatState(mode=thermo['mode'], current_temperature=thermo['current_temperature'],
                                    temperature_set_point=thermo['temperature_set_point'], name=thermo['name'])
        dataPoint.save()
        serializer.save()


class LightList(ListView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

    def perform_create(self, serializer):
        light = serializer.validated_data
        dataPoint = LightState(state=light['state'], name=light['name'])
        dataPoint.save()
        serializer.save()


class LightDetail(DetailView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

    def perform_update(self, serializer):
        light = serializer.validated_data
        dataPoint = LightState(state=light['state'], name=light['name'])
        dataPoint.save()
        serializer.save()
