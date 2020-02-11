from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from homes import views

urlpatterns = [
    path('house/', views.HouseList.as_view()),
    path('house/<str:pk>', views.HouseDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
