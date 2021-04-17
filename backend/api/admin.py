from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Ammo, Cannon, Config, InitSpeed, Param, Platform, User

# Register your models here.
admin.site.register(Ammo)
admin.site.register(Platform)
admin.site.register(Cannon)
admin.site.register(Config)
admin.site.register(Param)
admin.site.register(User, UserAdmin)
admin.site.register(InitSpeed)
