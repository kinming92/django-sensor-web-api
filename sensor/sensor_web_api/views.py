from sensor_web_api.serializers import HumiditySerializer, SoundSerializer
from sensor_web_api.models import Sensor
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from sensor_web_api.serializers import SensorSerializer, TemperatureSerializer
from rest_framework import status
from datetime import datetime, date

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'sensors': reverse('sensor-list', request=request, format=format)
    })

@api_view(['POST'])
def data(request, format=None):

    today = date.today().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    date_time_data = { 'date': today, 'time': current_time }
    response = {'error': []}

    if 'temp_c' in request.data.keys():
        temperature_keys = ['sensor', 'temp_c', 'temp_f']
        temperature_data = { temperature_key: request.data[temperature_key] for temperature_key in temperature_keys }
        temperature_serializer = TemperatureSerializer(data=temperature_data|date_time_data)
        if temperature_serializer.is_valid():
            temperature_serializer.save()
            response['temperature'] = temperature_serializer.data
        response['error'].append(temperature_serializer.errors)
    
    if 'humidity' in request.data.keys():
        humidity_keys = ['sensor', 'humidity']
        humidity_data = { humidity_key: request.data[humidity_key] for humidity_key in humidity_keys}
        humidity_serializer = HumiditySerializer(data=humidity_data|date_time_data)
        if humidity_serializer.is_valid():
            humidity_serializer.save()
            response['humidity'] = humidity_serializer.data
        response['error'].append(humidity_serializer.errors)

    if 'noise' in request.data.keys():
        sound_keys = ['sensor', 'noise']
        sound_data = { sound_key: request.data[sound_key] for sound_key in sound_keys}
        sound_serializer = SoundSerializer(data=sound_data|date_time_data)
        if sound_serializer.is_valid():
            sound_serializer.save()
            response['sound'] = sound_serializer.data
        response['error'].append(sound_serializer.errors)

    return Response(response, status=status.HTTP_200_OK)


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]