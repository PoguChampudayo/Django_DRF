from rest_framework import serializers

from .models import Sensor, TemperatureMeasurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
    
class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['id', 'sensor_id', 'temperature', 'measurement_date']
