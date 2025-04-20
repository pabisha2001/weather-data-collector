# 🌦️ Weather Data Engineering Project

This project collects real-time weather data from OpenWeatherMap API, cleans it, stores it in a SQLite database, and visualizes it using Python.

## 🚀 Project Structure

- **collectweather.py** – Collects weather data from the API
- **run_pipeline.py** – Orchestrates data collection, cleaning, and storing
- **store_weather.py** – Stores cleaned data into `weather_data.db`
- **visualize_weather.py** – Generates graphs for analysis
- **cleaned_weather_data.csv** – Cleaned output
- **weather_data.db** – SQLite database

## 📊 Visualizations
- Temperature over time
- Average temperature by city
- Humidity over time
- Wind speed vs temperature

## 🛠️ Technologies Used
- Python
- SQLite
- Pandas
- Matplotlib & Seaborn

## 💻 How to Run

```bash
# Collect, clean, and store weather data
python run_pipeline.py

# Visualize data
python visualize_weather.py
