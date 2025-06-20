from django.urls import path
from .views import UserRegisterView, UserProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]