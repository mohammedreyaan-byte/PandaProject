#Import Section
import pandas as pd
from Service.PandaService import printFirstFive,printLastFive

#Reading CSV from Data
df=pd.read_csv("../Data/WeatherData.csv")


#Input Section
takingInput=int(input("Welcome to the PandaProject\n"
                      "What do you want to do?\n"
                      "1.Read the CSV file\n"
                      "2.Write the CSV file\n"
                      "Enter your choice:"))

if takingInput==1:
    printFirstFive(df)
elif takingInput==2:
    printLastFive(df)




