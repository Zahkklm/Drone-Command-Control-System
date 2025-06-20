from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserProfile

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserProfile.ROLE_CHOICES, default='operator')

    class Meta:
        model = User
        fields = ('username', 'password', 'role')

    def create(self, validated_data):
        role = validated_data.pop('role', 'operator')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.profile.role = role
        user.profile.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.profile.role
        return token