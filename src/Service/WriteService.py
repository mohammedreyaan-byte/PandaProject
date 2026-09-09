#imports
import csv
from Models.WeatherData import WeatherData


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



