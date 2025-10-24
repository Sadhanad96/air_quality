import pandas as pd

# Load combined CSV
df_air = pd.read_csv("air_quality_combined.csv", low_memory=False)

# Check available columns
print("Columns in CSV:", df_air.columns)

# Use PM2.5 column (adjust column name if different in your CSV)
pm_col = 'PM2.5'  # ensure this matches the CSV header exactly

# Select City and PM2.5
df_pm25 = df_air[['City', pm_col]].copy()

# Aggregate average PM2.5 per city
avg_pm25 = df_pm25.groupby('City')[pm_col].mean().reset_index()

# Save processed CSV
avg_pm25.to_csv("air_quality_processed.csv", index=False)
print("Processed PM2.5 CSV saved. Shape:", avg_pm25.shape)
print(avg_pm25.head())
