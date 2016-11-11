import json
from datetime import datetime

attributes = {
    'description': lambda item: item['weather'][0]['description'],
    'temperature': lambda item: item['main']['temp'],
    'pressure': lambda item: item['main']['pressure'],
    'humidity': lambda item: item['main']['humidity']
}

def parse_forecast_json(filename):
    with open(filename) as file:
        json_data = json.load(file)

    result = {}
    for item in json_data['list']:
        date = item['dt_txt']
            result[date] = {}
        for attribute, get_attribute in attributes.items():
            result[date][attribute] = get_attribute(item)

    return result

def fetch_data(forecast, date, time, attribute=None):

    date_time = format_date(date, time)

    if date_time in forecast:
        weather_summary = forecast[date_time]
        if attribute:
            result = { attribute: weather_summary[attribute] }
        else:
            result = weather_summary
    else:
        result = error_response(date_time)

    return result

def error_response(date_time):
    return {"status": "error", "message": "No data for " + date_time}

def format_date(date, time):
    date = datetime.strptime(date + time, '%Y%m%d%H%M')
    return str(date)


