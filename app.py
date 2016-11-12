from flask import Flask, jsonify
from helper import parse_json, fetch_data

forecast = parse_json('forecast.json')

app = Flask(__name__)

@app.route('/weather/london/<date>/<time>/')
def weather_summary(date, time):
    data = fetch_data(forecast, date, time)
    return jsonify(data)

@app.route('/weather/london/<date>/<time>/<attr>/')
def weather_attribute(date, time, attr):
    data = fetch_data(forecast, date, time, attr)
    return jsonify(data)

@app.errorhandler(Exception)
def all_exception_handler(error):
   return jsonify({"status": "error"})

if __name__ == '__main__':
    app.run(debug=True)