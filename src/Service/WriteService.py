#imports
import csv
from Models.WeatherData import WeatherData
from src.ORM.dbmodel.models import DjangoWeatherData


class WriteService:


#Using Data as an object from WeatherData template

    def addData(self, Data:WeatherData):
        with open("../Data/WeatherData.csv", "a") as file:
            weather = csv.writer(file)

            weather.writerow([
                Data.date,
                Data.city,
                Data.temperature_c,
                Data.humidity_percent,
                Data.rainfall_mm,
                Data.wind_speed_kmh,
                Data.pressure_hpa,
                Data.weather_condition
            ])
            #Django ORM used

            DjangoWeatherData.objects.create(
                date=Data.date,
                city=Data.city,
                temperature_c=Data.temperature_c,
                humidity_percent=Data.humidity_percent,
                rainfall_mm=Data.rainfall_mm,
                wind_speed_kmh=Data.wind_speed_kmh,
                pressure_hpa=Data.pressure_hpa,
                weather_condition=Data.weather_condition
            )



