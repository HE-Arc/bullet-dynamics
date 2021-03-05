from rest_framework import serializers

from .models import Ammo

class AmmoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ammo
        fields = ('name', 'weight', 'price', 'bullet_weight', 'cx')