from django.contrib.auth.models import User, Group
from sensor_web_api.models import Sensor, Humidity, Temperature, Sound
from rest_framework import serializers



class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['location', 'city']

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['sensor', 'date', 'time', 'temp_c', 'temp_f']

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ['sensor', 'date', 'time', 'humidity']

class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['sensor', 'date', 'time', 'noise']