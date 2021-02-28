from datetime import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import BluetoothModel

from rest_framework import serializers

from celery import shared_task
from celery.schedules import *

@shared_task
def realtime_task():
    # time_s = time.time()
    # list_model = BluetoothModel.objects.all()
    # list_model_json = serializers.Serializer('json', list_model)

    # print("json" ,list_model_json)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'core-realtime-data',
        {
            'type': 'log_message',
            'message': "event_trigered_from_views"
        }
    ) 
    