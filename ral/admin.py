from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(hotel)
class hoteladmin(admin.ModelAdmin):
    list_display = ["palce","pizza","burger"]

@admin.register(palce)
class placeadmin(admin.ModelAdmin):
    list_display = ["name","address"]

@admin.register(waiter)
class waiteradmin(admin.ModelAdmin):
    list_display = ["name","hotel"]