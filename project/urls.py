from authtools.views import LoginView
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from homes.views import RoomViewSet, ThermostatViewSet, LightViewSet

router = routers.DefaultRouter()
router.register(r'room', RoomViewSet)
router.register(r'thermostat', ThermostatViewSet)
router.register(r'light', LightViewSet)

urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^rest2/', include('homes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'/login/', LoginView().as_view())
]
