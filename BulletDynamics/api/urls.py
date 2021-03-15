# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ammo', views.AmmoViewSet)
router.register(r'platform', views.PlatformViewSet)
router.register(r'cannon', views.CannonViewSet)
router.register(r'config', views.ConfigViewSet)
router.register(r'param', views.ParamViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'init_speed', views.InitSpeedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]