from django.urls import path
from .views import ChangeShowSensor, CreateListSensor, CreateMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateListSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
    path('sensors/<pk>/', ChangeShowSensor.as_view()),
]
