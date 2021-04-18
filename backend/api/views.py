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
    permission_classes = (IsAuthenticated,)
    queryset = Ammo.objects.all()
    serializer_class = AmmoSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class CannonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cannon.objects.all()
    serializer_class = CannonSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

class ParamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Param.objects.all()
    serializer_class = ParamSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class InitSpeedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InitSpeed.objects.all()
    serializer_class = InitSpeedSerializer

class ResultView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimulatorSerializer

    def get_queryset(self):
        username = self.request.GET.get('username','root')
        return User.objects.get(username=username).config
