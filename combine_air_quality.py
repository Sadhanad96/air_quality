import pandas as pd
import glob

# Get list of all CSV files in project folder
csv_files = glob.glob("*.csv")

# Combine all files into one DataFrame
df_list = []
for file in csv_files:
    df = pd.read_csv(file, low_memory=False)  # suppress dtype warnings
    df_list.append(df)

df_air = pd.concat(df_list, ignore_index=True)

# Save combined dataset
df_air.to_csv("air_quality_combined.csv", index=False)
print("Combined Air Quality CSV saved. Shape:", df_air.shape)
