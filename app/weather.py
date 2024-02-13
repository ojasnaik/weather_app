import requests
from dotenv import load_dotenv
import os
from weather_data import WeatherData


class Weather:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')

    def get_lat_long(self, city_name, state_code, country_code, API_key):
        # Get the latitude and longitude of a location
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&&appid={API_key}').json()
        data = response[0]
        lat, lon = data['lat'], data['lon']
        return lat, lon

    def get_weather_data(self, lat, lon, API_key):
        # Get the weather data of a location
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
        data = WeatherData(
            main=response['weather'][0]['main'],
            description=response['weather'][0]['description'],
            icon=response['weather'][0]['icon'],
            temp=response['main']['temp']
        )
        
        return data

    def main(self, city_name, state_code, country_code):
        lat, lon = self.get_lat_long(city_name, state_code, country_code, self.api_key)
        weather_data = self.get_weather_data(lat, lon, self.api_key)
        return weather_data
