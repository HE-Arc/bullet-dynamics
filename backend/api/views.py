from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AmmoSerializer
from .models import Ammo

from .serializers import PlatformSerializer
from .models import Platform

from .serializers import CannonSerializer
from .models import Cannon

from .serializers import ConfigSerializer
from .models import Config

from .serializers import ParamSerializer
from .models import Param

from .serializers import UserSerializer
from .models import User

from .serializers import InitSpeedSerializer
from .models import InitSpeed

class AmmoViewSet(viewsets.ModelViewSet):
    queryset = Ammo.objects.all().order_by('id')
    serializer_class = AmmoSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('id')
    serializer_class = PlatformSerializer

class CannonViewSet(viewsets.ModelViewSet):
    queryset = Cannon.objects.all().order_by('id')
    serializer_class = CannonSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all().order_by('id')
    serializer_class = ConfigSerializer

class ParamViewSet(viewsets.ModelViewSet):
    queryset = Param.objects.all().order_by('id')
    serializer_class = ParamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class InitSpeedViewSet(viewsets.ModelViewSet):
    queryset = InitSpeed.objects.all().order_by('id')
    serializer_class = InitSpeedSerializer