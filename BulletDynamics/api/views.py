from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AmmoSerializer
from .models import Ammo


class AmmoViewSet(viewsets.ModelViewSet):
    queryset = Ammo.objects.all().order_by('name')
    serializer_class = AmmoSerializer