from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views import generic
import logging

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User
from .serializers import (AmmoSerializer, CannonSerializer, ConfigSerializer,
                          InitSpeedSerializer, ParamSerializer,
                          PlatformSerializer, UserSerializer, SimulatorSerializer)

logger = logging.getLogger(__name__)

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
    #permission_classes = (IsAuthenticated,)
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

class ParamViewSet(viewsets.ModelViewSet):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class InitSpeedViewSet(viewsets.ModelViewSet):
    queryset = InitSpeed.objects.all()
    serializer_class = InitSpeedSerializer

class ResultView(generics.ListAPIView):
    serializer_class = SimulatorSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.get(username=username).config