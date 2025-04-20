import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect('weather_data.db')

# Read the data
df = pd.read_sql_query("SELECT * FROM weather", conn)
conn.close()

# Print column names and sample values
print("Columns in the database:", df.columns)
print(df.head())

# Drop rows where timestamp column equals the string "timestamp"
df = df[df['timestamp'] != 'timestamp']

# Convert timestamp to datetime safely
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Drop rows with invalid timestamps (NaT)
df = df.dropna(subset=['timestamp'])

# Set timestamp as index
df.set_index('timestamp', inplace=True)

# Plot temperature over time
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.index, y='temperature', marker='o')
plt.title('Temperature Over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
