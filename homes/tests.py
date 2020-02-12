import json

from authtools.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from homes.models import House, Room, RoomState, Light, LightState, Thermostat, ThermostatState


class signal_test(TestCase):

    def setUp(self) -> None:
        self.house = House(name='house1')
        self.house.save()

        self.rooms, self.lights, self.thermostats = [], [], []

        room1 = Room(name='room1', house=self.house, current_temperature=25)
        room2 = Room(name='room2', house=self.house, current_temperature=28)
        room1.save()
        room2.save()
        self.rooms += room1, room2

        light1 = Light(name='light1', room=room1, state='off')
        light2 = Light(name='light2', room=room2, state='off')

        light1.save()
        light2.save()
        self.lights += light1, light2

        thermostat1 = Thermostat(name='thermostat1', house=self.house, current_temperature=28, temperature_set_point=26,
                                 mode='OFF')
        thermostat2 = Thermostat(name='thermostat2', house=self.house, current_temperature=22, temperature_set_point=24,
                                 mode='OFF')

        thermostat1.save()
        thermostat2.save()
        self.thermostats += thermostat1, thermostat2

    def test_create(self):
        room_observations = RoomState.objects.all()
        assert len(room_observations) == 2

        light_observations = LightState.objects.all()
        assert len(light_observations) == 2

        thermostat_observations = ThermostatState.objects.all()
        assert len(thermostat_observations) == 2

    def test_room_update(self):
        room = self.rooms[0]
        room.current_temperature = 20
        room.save()

        assert get_latest_observation(RoomState, room.name).current_temperature == room.current_temperature
        assert len(RoomState.objects.all()) == 3

        room = self.rooms[1]
        room.save()

        assert len(RoomState.objects.all()) == 3

    def test_light_update(self):
        light = self.lights[0]
        light.state = 'on'
        light.save()

        assert get_latest_observation(LightState, light.name).state == light.state
        assert len(LightState.objects.all()) == 3

        light = self.lights[1]
        light.save()

        assert len(LightState.objects.all()) == 3

    def test_thermostat_update(self):
        thermostat = self.thermostats[0]
        thermostat.mode = 'fan'
        thermostat.save()

        assert get_latest_observation(ThermostatState, thermostat.name).mode == thermostat.mode

        thermostat.mode = 'auto'
        thermostat.save()

        assert get_latest_observation(ThermostatState, thermostat.name).mode == thermostat.mode

        thermostat.current_temperature = 33
        thermostat.save()

        assert get_latest_observation(ThermostatState,
                                      thermostat.name).current_temperature == thermostat.current_temperature

        thermostat.temperature_set_point = 0
        thermostat.save()

        assert get_latest_observation(ThermostatState,
                                      thermostat.name).temperature_set_point == thermostat.temperature_set_point

        observation_count = len(ThermostatState.objects.all())
        thermostat = self.thermostats[1]
        thermostat.save()

        assert len(ThermostatState.objects.all()) == observation_count


class rest_test(APITestCase):

    # Create a house
    # Create two rooms
    # verify create/delete/update for rooms works
    # create lights
    # verify CDU for lights works
    # create thermostats
    # verify CDU for thermostats works

    def setUp(self) -> None:
        User.objects.create_user(name='testuser', email='testuser@example.com', password='testuser')
        assert self.client.login(username='testuser@example.com', password='testuser')



    def test_create_house(self):
        response = self.post('house_list', {'name': 'house1', 'rooms': []})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_detail_update_house(self):
        self.test_create_house()
        response = self.client.get(reverse('house_detail', args=[1]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {'id': 1, 'name': 'house1', 'rooms': []})

        response = self.client.put(reverse('house_detail', args=[1]), data=json.dumps({"name":"updatedHouse", 'rooms':[]}), content_type="application/json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {'id': 1, 'name': 'updatedHouse', 'rooms': []})

    def test_delete_house(self):
        self.test_create_house()
        response = self.client.delete(reverse('house_detail', args=[1]))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)



def get_latest_observation(observationModel, key):
    return observationModel.objects.filter(name=key).order_by('-timestamp').first()
