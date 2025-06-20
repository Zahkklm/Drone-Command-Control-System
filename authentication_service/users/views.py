from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = user.profile
        return Response({
            "username": user.username,
            "role": profile.role,
        })