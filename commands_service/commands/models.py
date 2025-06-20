from django.db import models
from django.contrib.auth.models import User

class Command(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('ack', 'Acknowledged'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    COMMAND_TYPE_CHOICES = [
        ('takeoff', 'Takeoff'),
        ('land', 'Land'),
        ('move', 'Move'),
        ('custom', 'Custom'),
    ]
    drone_identifier = models.CharField(max_length=100)
    command_type = models.CharField(max_length=20, choices=COMMAND_TYPE_CHOICES)
    parameters = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    issued_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.command_type} for {self.drone_identifier} ({self.status})"

class MissionPlan(models.Model):
    name = models.CharField(max_length=100)
    drone_identifier = models.CharField(max_length=100)
    steps = models.JSONField()  # List of commands/waypoints
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mission {self.name} for {self.drone_identifier}"