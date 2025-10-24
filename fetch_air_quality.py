import requests
import pandas as pd

API_KEY = "e5ea90a8a473ff1a88de0af47e924714"  # replace with your key
url = "https://api.openaq.org/v3/measurements?country=IN&limit=500"
headers = {"X-API-Key": API_KEY}

response = requests.get(url, headers=headers)
data = response.json()

print("API Response:", data)  # For debugging

records = []
if 'results' in data:
    for item in data['results']:
        city = item.get('city', 'Unknown')
        location = item.get('location', 'Unknown')
        parameter = item.get('parameter', None)
        value = item.get('value', None)
        unit = item.get('unit', None)
        date_utc = item.get('date', {}).get('utc', None)
        records.append([city, location, parameter, value, unit, date_utc])
else:
    print("No 'results' found in the API response:", data)

if records:
    df_air = pd.DataFrame(records, columns=['City', 'Location', 'Parameter', 'Value', 'Unit', 'DateUTC'])
    df_air.to_csv('air_quality.csv', index=False)
    print("Air Quality Data saved.")
else:
    print("No data to save.")
