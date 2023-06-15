
from dotenv import dotenv_values
from main_data import Main_data

# Load environment variables from .env file
env_variables = dotenv_values('.env')
api_key = env_variables['api_key']

# weather_api = WeatherAPI(api_key)
result = Main_data(api_key)


# forecast_data = weather_api.get_forecast_data(city, forecast_days)
city = result.city = 'Yerevan'
result.set(10)
forecast_days = result.get()
forecast_data = result.index()


temperature_data = []
humidity_data = []
wind_speed_data = []
if forecast_data is not None:
    for day in range(forecast_days):
        temperature_data.append(result.temperature(forecast_data, day))
        humidity_data.append(result.humidity(forecast_data, day))
        wind_speed_data.append(result.wind_speed(forecast_data, day))
print(temperature_data)
print(humidity_data)
print(wind_speed_data)