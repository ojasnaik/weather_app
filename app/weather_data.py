from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temp: float