from rest_framework import serializers

from .models import Ammo

from .models import Platform

from .models import Cannon

from .models import Config

from .models import Param

from .models import User

from .models import InitSpeed

class AmmoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ammo
        fields = ('name', 'weight', 'price', 'bullet_weight', 'cx')

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('name', 'weight', 'price', 'length', 'standard_cannon_length')

class CannonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cannon
        fields = ('name', 'weight', 'price', 'length')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('name', 'cannon_id', 'ammo_id', 'platform_id')

class ParamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Param
        fields = ('name', 'height', 'angle')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'param_id')

class InitSpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InitSpeed
        fields = ('init_speed', 'cannon_id', 'ammo_id')