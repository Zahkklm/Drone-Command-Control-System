from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests

class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        telemetry_url = "http://telemetry:8001/api/drones/"
        commands_url = "http://commands:8002/api/commands/"
        headers = {"Authorization": request.headers.get("Authorization", "")}

        try:
            drones = requests.get(telemetry_url, headers=headers, timeout=2).json()
        except Exception:
            drones = []

        try:
            commands = requests.get(commands_url, headers=headers, timeout=2).json()
        except Exception:
            commands = []

        return Response({
            "drone_count": len(drones),
            "active_commands": len(commands),
            "drones": drones,
            "commands": commands,
        })
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_summary_page(request):
    context = {
        "drone_count": 0,
        "active_commands": 0,
        "drones": [],
        "commands": [],
    }
    return render(request, "dashboard/summary.html", context)