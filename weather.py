# Import packages
import os
import urllib.request
import json


def weather():
    # Uses OpenWeatherMap API to construct a message
    # Assigning API secret keys
    api = os.environ['api']
    # Assigning city
    city = 'sudbury'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={api}'
    response = urllib.request.urlopen(url)  #Opening url in python
    result = json.loads(response.read())

    temp_c = round(result['main']['temp'] - 273.15, 2)
    # Returns weather info message
    return f"Weather Info:\nThe temperature in {city.title()} is {temp_c}C."
