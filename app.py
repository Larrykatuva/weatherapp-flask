import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://samples.openweathermap.org/data/2.5/forecast?q={}&appid=b1b15e88fa797225412429c1c50c122a1'

    city = 'Nairobi'

    r = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : r['list'][0]['main']['temp'],
        'description' : r['list'][0]['weather'][0]['description'],
        'icon' : r['list'][0]['weather'][0]['icon'],
    }

    print(weather)

    return render_template('index.html', weather = weather)


if __name__ == "__main__":
    app.run(debug = True)    