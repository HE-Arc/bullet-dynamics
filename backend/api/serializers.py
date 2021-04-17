from rest_framework import serializers

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User

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
