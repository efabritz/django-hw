from django import forms
from rest_framework import serializers
from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, allow_empty_file=True, required=False)

    class Meta:
        model = Measurement
        fields = ['temperature', 'measurement_date', 'image', 'sensor']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
