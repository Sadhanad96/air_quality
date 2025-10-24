import pandas as pd

# Load datasets
df_air = pd.read_csv('air_quality.csv')
df_weather = pd.read_csv('weather.csv')

# Filter only PM2.5
df_air_pm25 = df_air[df_air['Parameter'] == 'pm25']

# Aggregate average PM2.5 per city
avg_pm25 = df_air_pm25.groupby('City')['Value'].mean().reset_index()

# Merge with weather data
df_merged = pd.merge(avg_pm25, df_weather, on='City')

# Save integrated dataset
df_merged.to_csv('air_weather_merged.csv', index=False)
print("Merged dataset saved.")
print(df_merged)
