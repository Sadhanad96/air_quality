import requests
import pandas as pd

API_KEY = "e5ea90a8a473ff1a88de0af47e924714"  # Replace with your API key
cities = ["Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai"]

records = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    temp = response['main']['temp']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    weather_desc = response['weather'][0]['description']
    records.append([city, temp, humidity, wind, weather_desc])

df_weather = pd.DataFrame(records, columns=['City', 'Temperature', 'Humidity', 'WindSpeed', 'Weather'])
df_weather.to_csv('weather.csv', index=False)
print("Weather Data saved.")
