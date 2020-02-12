from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from homes.models import House, Room, Thermostat, Light
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


class RoomDetail(DetailView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ThermostatList(ListView):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer


class ThermostatDetail(DetailView):
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer


class LightList(ListView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer


class LightDetail(DetailView):
    queryset = Light.objects.all()
    serializer_class = LightSerializer
