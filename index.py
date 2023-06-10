from weatherapi import WeatherAPI
from dotenv import dotenv_values

# Load environment variables from .env file
env_variables = dotenv_values('.env')
api_key = env_variables['api_key']

weather_api = WeatherAPI(api_key)

city = "London"
forecast_days = 5

forecast_data = weather_api.get_forecast_data(city, forecast_days)

if forecast_data is not None:
    for day in range(forecast_days):
        temperature = weather_api.get_temperature(forecast_data, day)
        humidity = weather_api.get_humidity(forecast_data, day)
        wind_speed = weather_api.get_wind_speed(forecast_data, day)

        print(f"Day {day + 1}:")
        print(f"  Temperature in {city}: {temperature} °C")
        print(f"  Humidity in {city}: {humidity} %")
        print(f"  Wind Speed in {city}: {wind_speed} km/h")
        print()
else:
    print(f"Failed to fetch forecast data for {city}")