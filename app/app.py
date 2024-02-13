from flask import Flask, request, render_template
from weather import Weather
class App:
    def __init__(self, weather):
        self.weather = weather
        self.app = Flask(__name__)
        self.configure_routes()

    def configure_routes(self):
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
        return self.weather.main(city, state, country)

    def run(self):
        self.app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    weather = Weather()
    app = App(weather)
    app.run()
