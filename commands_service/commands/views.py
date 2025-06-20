from rest_framework import viewsets, permissions
from .models import Command, MissionPlan
from .serializers import CommandSerializer, MissionPlanSerializer
from .permissions import IsOperatorOrAdmin

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOperatorOrAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(issued_by=self.request.user)

class MissionPlanViewSet(viewsets.ModelViewSet):
    queryset = MissionPlan.objects.all()
    serializer_class = MissionPlanSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOperatorOrAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)