from rest_framework.routers import DefaultRouter
from resources.views import ResourceViewSet, TypeViewSet
router = DefaultRouter()
router.register(r'resources', ResourceViewSet, base_name="resources")
router.register(r'types', TypeViewSet, base_name="types")
urlpatterns = router.urls