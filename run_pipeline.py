import schedule
import time
import os

def job():
    os.system("python3 collect_weather.py")

schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
