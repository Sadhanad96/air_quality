import pandas as pd

# Load processed air quality and weather CSVs (files are in the same folder)
df_air = pd.read_csv("air_quality_processed.csv")
df_weather = pd.read_csv("weather.csv")

# Merge on City
df_merged = pd.merge(df_air, df_weather, on="City", how="inner")

# Save merged dataset
df_merged.to_csv("air_weather_merged.csv", index=False)
print("Merged Air Quality + Weather CSV saved. Shape:", df_merged.shape)
print(df_merged.head())
