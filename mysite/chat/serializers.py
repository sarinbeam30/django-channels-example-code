# Serializer ---> convert model instances to JSON

from django.db.models import fields
from rest_framework import serializers
from .models import BluetoothModel

class BluetoothModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BluetoothModel
        fields = ('Date', 'Device_name', 'Location')