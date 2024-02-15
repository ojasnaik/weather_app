import requests
from dotenv import load_dotenv
import os
from weather_data import WeatherData


class Weather:
    """
    A class for retrieving weather data using the OpenWeatherMap API.

    Attributes:
    - api_key: The API key for accessing the OpenWeatherMap API.

    Methods:
    - get_lat_long: Retrieves the latitude and longitude of a location.
    - get_weather_data: Retrieves the weather data of a location.
    - main: Retrieves the weather data of a location based on city name, state code, and country code.
    """

    def __init__(self):
        """
        Initializes the Weather object by loading the API key from the environment variables.
        """
        load_dotenv()
        self.api_key = os.getenv('API_KEY')

    def get_lat_long(self, city_name, state_code, country_code, API_key):
        """
        Retrieves the latitude and longitude of a location.

        Parameters:
        - city_name: The name of the city.
        - state_code: The code of the state.
        - country_code: The code of the country.
        - API_key: The API key for accessing the OpenWeatherMap API.

        Returns:
        - lat: The latitude of the location.
        - lon: The longitude of the location.
        """
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&&appid={API_key}').json()
        data = response[0]
        lat, lon = data['lat'], data['lon']
        return lat, lon

    def get_weather_data(self, lat, lon, API_key):
        """
        Retrieves the weather data of a location.

        Parameters:
        - lat: The latitude of the location.
        - lon: The longitude of the location.
        - API_key: The API key for accessing the OpenWeatherMap API.

        Returns:
        - data: An instance of WeatherData containing the weather information.
        """
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
        data = WeatherData(
            main=response['weather'][0]['main'],
            description=response['weather'][0]['description'],
            icon=response['weather'][0]['icon'],
            temp=response['main']['temp']
        )
        
        return data

    def main(self, city_name, state_code, country_code):
        """
        Retrieves the weather data of a location based on city name, state code, and country code.

        Parameters:
        - city_name: The name of the city.
        - state_code: The code of the state.
        - country_code: The code of the country.

        Returns:
        - weather_data: An instance of WeatherData containing the weather information.
        """
        lat, lon = self.get_lat_long(city_name, state_code, country_code, self.api_key)
        weather_data = self.get_weather_data(lat, lon, self.api_key)
        return weather_data
