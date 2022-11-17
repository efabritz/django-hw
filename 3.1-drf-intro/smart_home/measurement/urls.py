from django.urls import path
from .views import ChangeSensor, CreateSensor, CreateMeasurement, ShowSensorsList, ShowSensorInformation

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('create_sensor/', CreateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
    path('change_sensor/<pk>/', ChangeSensor.as_view()),
    path('sensors/', ShowSensorsList.as_view()),
    path('sensor/<pk>/', ShowSensorInformation.as_view()),
]
