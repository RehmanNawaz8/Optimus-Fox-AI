import csv
import os
import random
from datetime import datetime, timedelta
from fastapi import FastAPI
import uvicorn


# File and Constants Setup

CSV_FILE = 'weather.csv'
TEMP_THRESHOLD = 35.0
HEADERS = ['timestamp', 'temperature', 'humidity']


# Creating CSV 

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)


# Function to Simulate Data

def generate_weather_data():
    temperature = round(random.uniform(20.0, 40.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    timestamp = datetime.now().isoformat()
    
    # Alert for high temperature
    if temperature > TEMP_THRESHOLD:
        print(f"[ALERT] High temperature recorded: {temperature}°C at {timestamp}")
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, humidity])
    
    return {'timestamp': timestamp, 'temperature': temperature, 'humidity': humidity}


# Weekly Summary Report

def generate_weekly_summary():
    one_week_ago = datetime.now() - timedelta(days=7)
    temps = []

    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row_time = datetime.fromisoformat(row['timestamp'])
            if row_time >= one_week_ago:
                temps.append(float(row['temperature']))

    if not temps:
        return "No data for the last 7 days."

    return {
        "max_temp": max(temps),
        "min_temp": min(temps),
        "avg_temp": round(sum(temps) / len(temps), 2)
    }


# FastAPI Se

app = FastAPI()

@app.get("/current-weather")
def get_latest_weather():
    try:
        with open(CSV_FILE, mode='r') as file:
            rows = list(csv.DictReader(file))
            if not rows:
                return {"message": "No data logged yet."}
            return rows[-1]
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/weekly-summary")
def get_weekly_summary():
    summary = generate_weekly_summary()
    return summary


if __name__ == "__main__":
    # Simulate hourly data 
    print("Simulating hourly data entry...")
    data = generate_weather_data()
    print("Latest entry:", data)

    # Show weekly summary
    summary = generate_weekly_summary()
    print("\nWeekly Summary:", summary)

    # Start API 
    print("\nStarting FastAPI server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
