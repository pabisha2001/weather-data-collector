import sqlite3
import pandas as pd

# Load data from CSV — force the right column names
column_names = ["timestamp", "city", "weather", "temperature", "humidity", "wind_speed"]
df = pd.read_csv("weather_data.csv", names=column_names, header=0)

# Connect to SQLite DB
conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    timestamp TEXT,
    city TEXT,
    weather TEXT,
    temperature REAL,
    humidity INTEGER,
    wind_speed REAL
)
''')

# Insert data
df.to_sql("weather", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Data inserted into weather_data.db")
