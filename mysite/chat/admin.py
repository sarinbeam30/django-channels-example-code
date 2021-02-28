from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BluetoothModel)
class BluetoothModelAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Device_name', 'Location')