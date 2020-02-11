from django.db import models
from model_utils import Choices


class NameBaseModel(models.Model):
    """
    Base model with common fields.
    """
    name = models.CharField(max_length=200, help_text='Name')

    class Meta:
        abstract = True


class House(NameBaseModel):
    """
    Store details about a house.
    """
    name = models.CharField(max_length=200, help_text='Name of the house.')

    def __str__(self):
        return self.name


class ThermostatData(NameBaseModel):
    MODES = Choices(
        ('off', 'Off'),
        ('fan', 'Fan'),
        ('auto', 'Auto'),
        ('cool', 'Cool'),
        ('heat', 'Heat'))
    mode = models.CharField(choices=MODES, default=MODES.off, max_length=5, help_text='Current mode of the thermostat.')
    current_temperature = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Current temperature at the thermostat.')
    temperature_set_point = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Temperature set point.')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Thermostat(ThermostatData):
    """
    Store thermostat data.
    """
    house = models.ForeignKey(House, related_name='thermostats', on_delete=models.CASCADE, help_text='Related house.')

    def __str__(self):
        return self.name


class ThermostatState(ThermostatData):
    timestamp = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return "{} - {} - current:{} - set:{} - {}".format(self.name, self.mode, self.current_temperature,
                                                           self.temperature_set_point, self.timestamp)


class RoomData(NameBaseModel):
    current_temperature = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        help_text='Current temperature at the thermostat.')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Room(RoomData):
    """
    Store room information.
    """
    house = models.ForeignKey(House, related_name='rooms', on_delete=models.CASCADE, help_text='Related house.')


class RoomState(RoomData):
    timestamp = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.current_temperature, self.timestamp)


class LightData(NameBaseModel):
    STATE = Choices(
        ('on', 'On'),
        ('off', 'Off'))
    state = models.CharField(choices=STATE, default=STATE.off, max_length=3, help_text='Current state of the light.')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Light(LightData):
    """
    Store room information.
    """
    room = models.ForeignKey(Room, related_name='lights', on_delete=models.CASCADE, help_text='Related room.')


class LightState(LightData):
    timestamp = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.state, self.timestamp)
