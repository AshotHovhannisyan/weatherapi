import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherapi.com/v1"

    def get_forecast_data(self, city, days):
        url = f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_temperature(self, data, day):
        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast = data['forecast']['forecastday'][day]
            temperature = forecast['day']['avgtemp_c']
            return temperature
        else:
            return None

    def get_humidity(self, data, day):
        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast = data['forecast']['forecastday'][day]
            humidity = forecast['day']['avghumidity']
            return humidity
        else:
            return None

    def get_wind_speed(self, data, day):
        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast = data['forecast']['forecastday'][day]
            wind_speed = forecast['day']['maxwind_kph']
            return wind_speed
        else:
            return None