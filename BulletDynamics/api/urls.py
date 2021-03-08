# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ammos', views.AmmoViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'cannons', views.CannonViewSet)
router.register(r'configs', views.ConfigViewSet)
router.register(r'params', views.ParamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'init_speeds', views.InitSpeedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]