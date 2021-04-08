from django.contrib import admin
from .models import Ammo
from .models import Platform
from .models import Cannon
from .models import Config
from .models import Param
from .models import User
from .models import InitSpeed

# Register your models here.
admin.site.register(Ammo)
admin.site.register(Platform)
admin.site.register(Cannon)
admin.site.register(Config)
admin.site.register(Param)
admin.site.register(User)
admin.site.register(InitSpeed)