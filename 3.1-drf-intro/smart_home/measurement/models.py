from django.db import models
from datetime import date
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    temperature = models.FloatField()
    measurement_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

