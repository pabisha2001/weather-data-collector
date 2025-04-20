import sqlite3

def test_db_connection():
    try:
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM weather")
        count = cursor.fetchone()[0]
        assert count > 0, "No weather data found in database."
        print(f"✅ Database test passed: {count} records found.")
    except Exception as e:
        print("❌ Test failed:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    test_db_connection()
