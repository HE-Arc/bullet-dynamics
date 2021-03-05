from django.db import models

# Create your models here.
class Ammo(models.Model):    
    name = models.CharField(max_length=64)
    weight = models.DecimalField(max_digits=8, decimal_places=5)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bullet_weight = models.DecimalField(max_digits=8, decimal_places=5)
    cx = models.DecimalField(max_digits=8, decimal_places=5)

    
