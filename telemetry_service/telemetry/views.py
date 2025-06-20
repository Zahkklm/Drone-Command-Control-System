from rest_framework import viewsets
from .models import Drone, TelemetryData
from .serializers import DroneSerializer, TelemetryDataSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Drone model.
# Provides CRUD operations for Drone objects via REST API.
class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for TelemetryData model.
# Provides CRUD operations for TelemetryData objects via REST API.
class TelemetryDataViewSet(viewsets.ModelViewSet):
    queryset = TelemetryData.objects.all()
    serializer_class = TelemetryDataSerializer
    permission_classes = [IsAuthenticated]