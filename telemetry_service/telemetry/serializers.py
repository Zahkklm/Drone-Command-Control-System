from rest_framework import serializers
from .models import Drone, TelemetryData

# Serializer for the Drone model.
# Converts Drone model instances to JSON and validates input data for Drone creation/update.
class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

# Serializer for the TelemetryData model.
# Handles serialization and validation for telemetry data records.
class TelemetryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetryData
        fields = '__all__'