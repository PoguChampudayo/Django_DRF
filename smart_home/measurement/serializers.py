from rest_framework import serializers

from .models import Sensor, Measurement

        
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        depth = 1
        fields = ['id', 'name', 'description', 'measurements']
    
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'measurement_date']
