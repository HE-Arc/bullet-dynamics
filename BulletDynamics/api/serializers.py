from rest_framework import serializers

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User

class AmmoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ammo
        fields = '__all__'

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class CannonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cannon
        fields = '__all__'

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

class ParamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Param
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InitSpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InitSpeed
        fields = '__all__'
