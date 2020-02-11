from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from homes import views

urlpatterns = [
    path('house/', views.HouseList.as_view()),
    path('house/<int:pk>', views.HouseDetail.as_view()),
    path('room/', views.RoomList.as_view()),
    path('room/<int:pk>', views.RoomDetail.as_view()),
    path('light/', views.LightList.as_view()),
    path('light/<int:pk>', views.LightDetail.as_view()),
    path('thermostat/', views.ThermostatList.as_view()),
    path('thermostat/<int:pk>', views.ThermostatDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
