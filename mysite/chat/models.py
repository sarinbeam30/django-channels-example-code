import django
from django.db import models
from django.conf import settings
from datetime import datetime

class BluetoothModel(models.Model):
    mytime = datetime.now()
    mytime_format = mytime.strftime('%d-%m-%Y %H:%M:%S')

    Date = models.DateTimeField(default=django.utils.timezone.now)

    Device_name = models.TextField(max_length=50)

    Location = models.TextField(default='ECC Building')


    def __str__(self):
        return self.Device_name