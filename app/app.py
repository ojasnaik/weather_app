
from weather import main as get_weather
from flask import Flask, render_template, request
from dataclasses import asdict
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('index.html')
    if request.method == 'GET':
        return asdict(get_weather("San Jose", "CA", "US"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)