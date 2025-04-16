# 🌦️ Weather Data Collection Project

This project collects real-time weather data for a specific city (Jaffna, Sri Lanka) using the OpenWeatherMap API. The data is fetched and stored in a structured format (CSV file) for future analysis or visualization.

---

## 📌 Features

- Fetches live weather data (temperature, humidity, wind speed, etc.)
- Stores data in a CSV file with timestamps
- Easy to run and modify
- Clean and readable Python code

---

## 📁 Project Structure

Weather_Project/ ├── collect_weather.py # Main script to collect and save weather data ├── weather_data.csv # Output CSV file with collected data └── README.md # Project documentation


---

## 🛠️ Technologies Used

- Python 3
- `requests` for API calls
- `pandas` for data handling
- OpenWeatherMap API

---

## 📦 Requirements

Before running the script, install the required packages:

```bash
pip install requests pandas

🚀 How to Run
bash
Copy
Edit
python collect_weather.py
The script will:

Connect to the OpenWeatherMap API

Fetch current weather info for Jaffna

Save the result to weather_data.csv

🔐 API Key
Make sure you replace the API_KEY in collect_weather.py with your own OpenWeatherMap API key:

python
Copy
Edit
API_KEY = 'your_api_key_here'
You can get one for free at: https://openweathermap.org/api

📈 Future Plans (Epics)
Epic 2: Build a real-time weather dashboard

Epic 3: Automate data collection with a scheduler

Epic 4: Analyze historical weather data

🤝 Contributing
Feel free to fork this repo, create a feature branch, and open a pull request!

📧 Contact
If you have questions, email me at: your.email@example.com
Or connect via LinkedIn





