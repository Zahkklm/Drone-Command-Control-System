from rest_framework import routers
from .views import CommandViewSet, MissionPlanViewSet

router = routers.DefaultRouter()
router.register(r'commands', CommandViewSet)
router.register(r'missions', MissionPlanViewSet)

urlpatterns = router.urls