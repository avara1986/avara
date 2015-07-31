from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from resources.views import ResourceViewSet, TypeViewSet


router = DefaultRouter()
router.register(r'resources', ResourceViewSet, base_name="resources")
router.register(r'types', TypeViewSet, base_name="types")
urlpatterns = router.urls
urlpatterns += patterns('',
                        url(r'^token-auth/', views.obtain_auth_token),
                        )
