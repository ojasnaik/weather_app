import pytest
from unittest.mock import patch
from flask import template_rendered, request
from contextlib import contextmanager
from app import App
from weather import Weather
from weather_data import WeatherData

@pytest.fixture
def mock_weather_data():
    return WeatherData(main="Cloudy", description="overcast clouds", icon="03d", temp=68.0)

@pytest.fixture
def app_instance():
    weather = Weather()
    app = App(weather)
    app.app.config['TESTING'] = True
    return app.app

@pytest.fixture
def client(app_instance):
    return app_instance.test_client()

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@patch('weather.Weather.get_lat_long')
@patch('weather.Weather.get_weather_data')
def test_index_page_post(mock_get_weather_data, mock_get_lat_long, client, mock_weather_data, app_instance):
    mock_get_lat_long.return_value = (37.7749, -122.4194)
    mock_get_weather_data.return_value = mock_weather_data
    
    with captured_templates(app_instance) as templates:
        response = client.post('/', data={'city': 'San Francisco', 'state': 'CA', 'country': 'US'})
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == "index.html"
        assert 'data' in context
        assert context['data'].temp == 68.0
