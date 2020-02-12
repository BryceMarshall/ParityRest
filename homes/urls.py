from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from homes import views

urlpatterns = [
    path('house/', views.HouseList.as_view(), name='house_list'),
    path('house/<int:pk>', views.HouseDetail.as_view(), name='house_detail'),
    path('room/', views.RoomList.as_view(), name='room_list'),
    path('room/<int:pk>', views.RoomDetail.as_view(), name='room_detail'),
    path('light/', views.LightList.as_view(), name='light_list'),
    path('light/<int:pk>', views.LightDetail.as_view(), name='light_detail'),
    path('thermostat/', views.ThermostatList.as_view(), name='thermostat_list'),
    path('thermostat/<int:pk>', views.ThermostatDetail.as_view(), name='thermostat_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
