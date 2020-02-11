from django.contrib import admin

from homes.models import House, Thermostat, Light, Room

admin.site.register(House)
admin.site.register(Thermostat)
admin.site.register(Light)
admin.site.register(Room)
