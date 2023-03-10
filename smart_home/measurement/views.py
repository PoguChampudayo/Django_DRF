# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorSerializer, MeasurementSerializer

class AddSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
        
    

        
    
   