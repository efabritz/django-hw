# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, \
     RetrieveAPIView
from rest_framework.response import Response
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from measurement.models import Sensor, Measurement


class CreateListSensor(CreateAPIView, ListCreateAPIView):
     queryset = Sensor.objects.all()
     serializer_class = SensorSerializer


class ChangeShowSensor(RetrieveUpdateAPIView, ListCreateAPIView):
     queryset = Sensor.objects.all()
     serializer_class = SensorSerializer


class CreateMeasurement(CreateAPIView):
     queryset = Measurement.objects.all()
     serializer_class = MeasurementSerializer
