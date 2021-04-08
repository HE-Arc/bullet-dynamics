from django.db import models

# Create your models here.
class Ammo(models.Model):    
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=8, decimal_places=5)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bullet_weight = models.DecimalField(max_digits=8, decimal_places=5)
    cx = models.DecimalField(max_digits=8, decimal_places=5)

class Platform(models.Model):
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=8, decimal_places=5)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    length = models.DecimalField(max_digits=8, decimal_places=5)
    standard_cannon_length = models.DecimalField(max_digits=8, decimal_places=5)

class Cannon(models.Model):    
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=8, decimal_places=5)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    length = models.DecimalField(max_digits=8, decimal_places=5)
    ammo = models.ManyToManyField(Ammo, through='InitSpeed')

class Config(models.Model):
    name = models.CharField(max_length=64)
    cannon_id = models.ForeignKey('Cannon', on_delete=models.SET_NULL, null=True)
    ammo_id = models.ForeignKey('Ammo', on_delete=models.SET_NULL, null=True)
    platform_id = models.ForeignKey('Platform', on_delete=models.SET_NULL, null=True)

class Param(models.Model):
    name = models.CharField(max_length=64)
    height = models.DecimalField(max_digits=8, decimal_places=5)
    angle = models.DecimalField(max_digits=8, decimal_places=5)

class User(models.Model):
    name = models.CharField(max_length=64)
    param_id = models.ForeignKey('Param', on_delete=models.SET_NULL, null=True) 
    config = models.ManyToManyField(Config)

class InitSpeed(models.Model):
    cannon_id = models.ForeignKey('Cannon', on_delete=models.SET_NULL, null=True)
    ammo_id = models.ForeignKey('Ammo', on_delete=models.SET_NULL, null=True)
    init_speed = models.DecimalField(max_digits=8, decimal_places=5)

    
