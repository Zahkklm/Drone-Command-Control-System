from django.urls import path
from .views import (
    UserRegisterView, UserProfileView, PasswordChangeView,
    PasswordResetRequestView, PasswordResetConfirmView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]