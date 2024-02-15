import pytest
from unittest.mock import patch
from weather import Weather
from weather_data import WeatherData

@pytest.fixture
def mock_response_data():
    return {
        "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}],
        "main": {"temp": 75.2}
    }

@pytest.fixture
def mock_geo_data():
    return [{"lat": 37.7749, "lon": -122.4194}]

def test_get_lat_long(mock_geo_data):
    api_key = "testapikey"
    with patch("requests.get") as mocked_get:        
        mocked_get.return_value.json.return_value = mock_geo_data

        weather = Weather()
        lat, lon = weather.get_lat_long("San Francisco", "CA", "US", api_key)
        
        mocked_get.assert_called_once()
        assert lat == 37.7749
        assert lon == -122.4194

def test_get_weather_data(mock_response_data):
    api_key = "testapikey"
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json.return_value = mock_response_data
        
        weather = Weather()
        weather_data = weather.get_weather_data(37.7749, -122.4194, api_key)
        
        assert isinstance(weather_data, WeatherData)
        assert weather_data.main == "Clear"
        assert weather_data.temp == 75.2

def test_main(mock_response_data, mock_geo_data):
    api_key = "testapikey"
    with patch("weather.Weather.get_lat_long") as mocked_get_lat_long, \
         patch("weather.Weather.get_weather_data") as mocked_get_weather_data:
        
        mocked_get_lat_long.return_value = (37.7749, -122.4194)
        mocked_get_weather_data.return_value = WeatherData(
            main=mock_response_data["weather"][0]["main"],
            description=mock_response_data["weather"][0]["description"],
            icon=mock_response_data["weather"][0]["icon"],
            temp=mock_response_data["main"]["temp"]
        )
        
        weather = Weather()
        result = weather.main("San Francisco", "CA", "US")
        
        assert isinstance(result, WeatherData)
        assert result.temp == 75.2
        assert result.main == "Clear"