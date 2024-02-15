from flask import Flask, request, render_template
from weather import Weather
class App:
    """
    Represents a weather application.

    Args:
        weather: An instance of the Weather class.

    Attributes:
        weather: An instance of the Weather class.
        app: An instance of the Flask class.

    Methods:
        configure_routes: Configures the routes for the Flask app.
        get_weather: Retrieves weather data for a given city, state, and country.
        run: Runs the Flask app.

    """
    def __init__(self, weather):
        self.weather = weather
        self.app = Flask(__name__)
        self.configure_routes()

    def configure_routes(self):
            """
            Configures the routes for the weather app.

            The index route handles both GET and POST requests. If a POST request is made,
            it retrieves the city, state, and country from the form data and calls the
            get_weather method to fetch the weather data. The retrieved data is then passed
            to the index.html template for rendering.

            Returns:
                None
            """
            @self.app.route('/', methods=['GET', 'POST'])
            def index():
                data = None
                if request.method == 'POST':
                    city = request.form['city']
                    state = request.form['state']
                    country = request.form['country']
                    data = self.get_weather(city, state, country)
                return render_template('index.html', data=data)
            
    def get_weather(self, city, state, country):
        """
        Get the weather information for a specific city.

        Args:
            city (str): The name of the city.
            state (str): The name of the state.
            country (str): The name of the country.

        Returns:
            A dataclass object containing the weather information.
        """
        return self.weather.main(city, state, country)

    def run(self):
        self.app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    weather = Weather()
    app = App(weather)
    app.run()
