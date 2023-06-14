from weatherapi import WeatherAPI
class Main_data(WeatherAPI):
    city = "London"
    __forecast_days = 5
    def __init__(self, api_key):
        super().__init__(api_key)
    def index(self):
        return self.get_forecast_data(self.city, self.__forecast_days)
    def set(self,day):
        if "Yerevan" == self.city:
            self.__forecast_days = day
