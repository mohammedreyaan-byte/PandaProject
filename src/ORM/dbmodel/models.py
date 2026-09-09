from django.db import models


class DjangoWeatherData(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=100)

    temperature_c = models.FloatField()
    humidity_percent = models.FloatField()
    rainfall_mm = models.FloatField()
    wind_speed_kmh = models.FloatField()
    pressure_hpa = models.FloatField()

    weather_condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} - {self.date}"