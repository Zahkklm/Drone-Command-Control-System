from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from telemetry.views import DroneViewSet, TelemetryDataViewSet

router = routers.DefaultRouter()
router.register(r'drones', DroneViewSet)
router.register(r'telemetry', TelemetryDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]