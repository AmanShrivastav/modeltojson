from django.contrib import admin
from .models import Userdetail
from .models import Activity
# Register your models here.

admin.site.register([Userdetail, Activity])




