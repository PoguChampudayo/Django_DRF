from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
class TemperatureMeasurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, to_field='id', on_delete=models.CASCADE)
    temperature = models.FloatField()
    measurement_date = models.DateField(auto_now_add=True)
    

