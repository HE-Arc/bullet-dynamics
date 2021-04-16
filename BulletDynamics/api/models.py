from django.db import models
from django.contrib.auth.models import AbstractUser

class Ammo(models.Model):    
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bullet_weight = models.DecimalField(max_digits=6, decimal_places=3)
    cx = models.DecimalField(max_digits=6, decimal_places=3)
    class Meta:
        ordering = ['id']

class Platform(models.Model):
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=3)
    standard_cannon_length = models.DecimalField(max_digits=6, decimal_places=3)
    class Meta:
        ordering = ['id']

class Cannon(models.Model):    
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=3)
    ammo = models.ManyToManyField(Ammo, through='InitSpeed')
    class Meta:
        ordering = ['id']

class Config(models.Model):
    name = models.CharField(max_length=64)
    cannon = models.ForeignKey('Cannon', on_delete=models.SET_NULL, null=True)
    ammo = models.ForeignKey('Ammo', on_delete=models.SET_NULL, null=True)
    platform = models.ForeignKey('Platform', on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['id']

class Param(models.Model):
    name = models.CharField(max_length=64)
    height = models.DecimalField(max_digits=6, decimal_places=3)
    angle = models.DecimalField(max_digits=6, decimal_places=3)
    class Meta:
        ordering = ['id']

class User(AbstractUser):
    param = models.ForeignKey('Param', on_delete=models.SET_NULL, null=True) 
    config = models.ManyToManyField(Config)
    class Meta:
        ordering = ['id']

class InitSpeed(models.Model):
    cannon = models.ForeignKey('Cannon', on_delete=models.SET_NULL, null=True)
    ammo = models.ForeignKey('Ammo', on_delete=models.SET_NULL, null=True)
    init_speed = models.DecimalField(max_digits=6, decimal_places=3)
    class Meta:
        ordering = ['id']   
