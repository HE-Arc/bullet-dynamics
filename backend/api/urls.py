from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

router = routers.DefaultRouter()
router.register(r'ammos', views.AmmoViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'cannons', views.CannonViewSet)
router.register(r'configs', views.ConfigViewSet)
router.register(r'params', views.ParamViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'init_speeds', views.InitSpeedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/sim/<str:username>/', views.ResultView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]
