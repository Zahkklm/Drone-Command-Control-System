from django.contrib import admin
from .models import Drone, TelemetryData

admin.site.register(Drone)
admin.site.register(TelemetryData)