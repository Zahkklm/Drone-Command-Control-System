from rest_framework import serializers
from .models import Command, MissionPlan

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'

class MissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionPlan
        fields = '__all__'