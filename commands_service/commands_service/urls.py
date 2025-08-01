from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('commands.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Commands Service API",
      default_version='v1',
      description="API documentation for the commands microservice",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

