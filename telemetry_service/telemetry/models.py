from django.db import models

# Drone model represents a physical drone in the system.
class Drone(models.Model):
    identifier = models.CharField(max_length=100, unique=True)  # Unique drone identifier (e.g., serial number)
    model = models.CharField(max_length=100)                    # Drone model name/type
    owner = models.CharField(max_length=100)                    # Owner or operator of the drone
    created_at = models.DateTimeField(auto_now_add=True)        # Timestamp when the drone was registered

    def __str__(self):
        return self.identifier

# TelemetryData model stores telemetry records sent by drones.
class TelemetryData(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name='telemetry')  # Link to the drone
    timestamp = models.DateTimeField(auto_now_add=True)                                   # When the data was received
    latitude = models.FloatField()                                                        # Latitude position
    longitude = models.FloatField()                                                       # Longitude position
    altitude = models.FloatField()                                                        # Altitude in meters
    speed = models.FloatField()                                                           # Speed in m/s or km/h
    battery_status = models.FloatField()                                                  # Battery percentage or voltage
    sensor_data = models.JSONField()                                                      # Additional sensor data as JSON

    def __str__(self):
        return f"{self.drone.identifier} @ {self.timestamp}"