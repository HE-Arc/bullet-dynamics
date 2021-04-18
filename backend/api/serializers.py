import logging

from django.db import models
from rest_framework import serializers

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User

from SimulationCore import SimulatorCore

logger = logging.getLogger(__name__)

class AmmoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Ammo
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Platform
        fields = '__all__'

class CannonSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Cannon
        fields = '__all__'

class ConfigSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Config
        fields = '__all__'

class ParamSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Param
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    #config = ConfigSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

class InitSpeedSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = InitSpeed
        fields = '__all__'

# Serializer that get the necassary data from the database and runs the simulation for each config of the current user
class SimulatorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    data = serializers.SerializerMethodField('run_simulation')
    class Meta:
        model = Config
        fields = ('id', 'name', 'data')

    def run_simulation(self, config):
        a = config.ammo
        c = config.cannon
        i = InitSpeed.objects.filter(cannon=c, ammo=a).get().init_speed

        simulator = SimulatorCore.Simulator()
        data = simulator.run(v0=float(i), mass=float(a.bullet_weight), cx=float(a.cx))

        return data

