import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Show entries where timestamp = 'timestamp'
print("Before cleanup:")
for row in cursor.execute("SELECT * FROM weather WHERE timestamp = 'timestamp'"):
    print(row)

# Delete bad row(s) where timestamp is 'timestamp'
cursor.execute("DELETE FROM weather WHERE timestamp = 'timestamp'")
conn.commit()

# Confirm deletion
print("\nAfter cleanup:")
for row in cursor.execute("SELECT * FROM weather WHERE timestamp = 'timestamp'"):
    print(row)

conn.close()
