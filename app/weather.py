import requests
from dotenv import load_dotenv
import os
from weather_data import WeatherData

load_dotenv()
api_key = os.getenv('API_KEY')

def get_lan_long(city_name, state_code, country_code, API_key):
    # Get the latitude and longitude of a location
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&&appid={API_key}').json()
    data = response[0]
    lat, lon = data['lat'], data['lon']
    return lat, lon

def get_weather_data(lat, lon, API_key):
    # Get the weather data of a location
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
    data = WeatherData(
        main=response['weather'][0]['main'],
        description=response['weather'][0]['description'],
        icon=response['weather'][0]['icon'],
        temp=response['main']['temp']
    )
    
    return data

def main(city_name, state_code, country_code):
    lat, lon = get_lan_long(city_name, state_code, country_code, api_key)
    weather_data = get_weather_data(lat, lon, api_key)
    return weather_data

if __name__ == '__main__':
    lat, lon = get_lan_long('New York', 'NY', 'US', api_key)
    weather_data = get_weather_data(lat, lon, api_key)
    print(weather_data)
    