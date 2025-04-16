import requests
import pandas as pd
from datetime import datetime
import os

API_KEY =  'a692772815923047c420f3426b75cc7a'# 🔐 Replace with your OpenWeatherMap API key
CITIES = ['Jaffna', 'Colombo', 'Kandy']

weather_list = []

for city in CITIES:
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city},LK&appid={API_KEY}&units=metric'
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'city': city,
            'weather': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        weather_list.append(weather_data)
    else:
        print(f"Failed to fetch data for {city}")

df = pd.DataFrame(weather_list)
file_exists = os.path.isfile('weather_data.csv')
df.to_csv('weather_data.csv', mode='a', header=not file_exists, index=False)
print("Weather data saved to weather_data.csv")
