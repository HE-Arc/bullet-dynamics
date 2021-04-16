from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User
from .serializers import (AmmoSerializer, CannonSerializer, ConfigSerializer,
                          InitSpeedSerializer, ParamSerializer,
                          PlatformSerializer, UserSerializer)


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
    psermission_classes = (IsAuthenticated,)
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
