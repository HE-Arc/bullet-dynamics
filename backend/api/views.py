from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views import generic

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User
from .serializers import (AmmoSerializer, CannonSerializer, ConfigSerializer,
                          InitSpeedSerializer, ParamSerializer,
                          PlatformSerializer, UserSerializer, SimulatorSerializer)

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
    permission_classes = (IsAuthenticated,)
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
'''
class UserConfigsView(views.APIView):
    serializer_class = ConfigSerializer

    def get(self):
        """
        Return a list of configs for a user.
        """
        configs = User.objects.filter(username=self.request.username).config
        return Response(configs)'''

class TestView(generic.ListView):


    def get_queryset(self):
        return ['yo', 'fdp']

"""
    def get(self):
        
        #Return the simulation data for each config.
        
        #simulatorData = {}
        #for config in self.request.configs:
            #simulatorData[config.id] = computeSimulatorData()
        #return Response(simulatorData)
        return Response("yo")
    
    def computeSimulatorData(config):
        #TODO replace with real values
        return Simulation.getResult(bullet_weight = 0.010 , init_speed=500)"""
