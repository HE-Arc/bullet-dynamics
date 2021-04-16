from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User
from .serializers import (AmmoSerializer, CannonSerializer, ConfigSerializer,
                          InitSpeedSerializer, ParamSerializer,
                          PlatformSerializer, UserSerializer)

class AmmoViewSet(viewsets.ModelViewSet):
    queryset = Ammo.objects.all()
    serializer_class = AmmoSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class CannonViewSet(viewsets.ModelViewSet):
    queryset = Cannon.objects.all()
    serializer_class = CannonSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    psermission_classes = (IsAuthenticated,)
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

class ParamViewSet(viewsets.ModelViewSet):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InitSpeedViewSet(viewsets.ModelViewSet):
    queryset = InitSpeed.objects.all()
    serializer_class = InitSpeedSerializer
