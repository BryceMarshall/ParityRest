from authtools.views import LoginView
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework import routers


urlpatterns = [
    url(r'^rest/', include('homes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'/login/', LoginView().as_view())
]
