from rest_framework import serializers
from .models import SensorData, IrrigationControl

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class IrrigationControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationControl
        fields = '__all__'
