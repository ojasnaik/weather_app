from dataclasses import dataclass

@dataclass
class WeatherData:
    """Represents weather data for a specific location."""
    main: str
    description: str
    icon: str
    temp: float