from django.contrib import admin

from homes.models import House, Thermostat, Light, Room, ThermostatState, RoomState, LightState

admin.site.register(House)
admin.site.register(Thermostat)
admin.site.register(Light)
admin.site.register(Room)
admin.site.register(ThermostatState)
admin.site.register(RoomState)
admin.site.register(LightState)

