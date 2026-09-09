#Import Section
import pandas as pd
from src.Service.ReadService import ReadService
from src.Service.WriteService import WriteService
from src.Models.WeatherData import WeatherData


#Reading CSV from Data
df=pd.read_csv("../Data/WeatherData.csv")

#Object Instantiation



#Input Section
takingInput=int(input("Welcome to the PandaProject\n"
                      "What do you want to do?\n"
                      "1.Print first five readings\n"
                      "2.Print last five readings\n"
                      "3.Print data of specific city\n"
                      "4.Add Data to the CSV\n"
                      "Enter your choice:"))

#1st Function
if takingInput==1:
    readService = ReadService(df)
    readService.printFirstFive()

#2nd Function
elif takingInput==2:
    readService = ReadService(df)
    readService.printLastFive()

#3rd Function
elif takingInput==3:
    a=input("Enter city name\n")
    readService = ReadService(df)
    readService.printCityReport(a)

#4th Function
elif takingInput==4:
    date=input("Enter date in format YYYY-MM-DD\n")
    city=input("Enter city name\n")
    temperature_c=float(input("Enter temperature in C\n"))
    humidity_percent = float(input("Enter humidity in %\n"))
    rainfall_mm = float(input("Enter rainfall in mm\n"))
    wind_speed_kmh = float(input("Enter wind speed in km/h\n"))
    pressure_hpa = float(input("Enter pressure in hPa\n"))
    weather_condition=input("Enter weather condition\n")
    writeService = WriteService()
    weatherData = WeatherData(date,city,temperature_c,humidity_percent,rainfall_mm,wind_speed_kmh,pressure_hpa,weather_condition)
    writeService.addData(weatherData)







