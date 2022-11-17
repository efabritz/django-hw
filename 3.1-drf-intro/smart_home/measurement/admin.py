from django.contrib import admin

from .models import Measurement, Sensor

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Measurement)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'measurement_date')
