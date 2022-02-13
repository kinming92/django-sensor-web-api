from django.db import models

class Sensor(models.Model):
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

class Temperature(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

class Sound(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    noise = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

class Humidity(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

class Weather(models.Model):
    date_time = models.DateTimeField()
    city = models.CharField(max_length=200)
    sunrise = models.TimeField()
    sunset = models.TimeField()
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    feels_like = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    dew_point = models.FloatField()
    clouds = models.FloatField()
    wind_speed = models.FloatField()
    wind_gust = models.FloatField()
    wind_deg = models.FloatField()
    weather_description = models.CharField(max_length=200)
    rain = models.FloatField()
    snow = models.FloatField()
    uvi = models.FloatField()
    visibility = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    
