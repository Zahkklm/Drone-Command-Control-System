from django.contrib import admin
from django.urls import path, include
from . import auth_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(auth_api.urlpatterns)),
    path('api/', include('users.urls')),
]