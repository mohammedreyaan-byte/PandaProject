#Services


class ReadService:
    def __init__(self,df):
        self.df=df

    def printFirstFive(self):
        print(self.df.head())

    def printLastFive(self):
        print(self.df.tail())

    def printCityReport(self,a):
        result=self.df[self.df["city"]==a]
        print(result[["date", "weather_condition"]])






