from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        return render_template('base.html', weather=weather_data)
    return render_template('base.html')

def get_weather_data(city):
    API_KEY = '068b9448c8d37f37d18dd401e55f8aec'
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(URL)
    data = response.json()
    if data['cod'] == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather_data

    
if __name__ == '__main__':
    app.run(debug=True)