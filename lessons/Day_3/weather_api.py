# V1

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=31.95&longitude=35.91&current_weather=true"

try:
    response = requests.get(url, timeout=10) # Added timeout
    if(response.status_code != 200):
        raise ValueError("Unknown Error!")
    response.raise_for_status() # Check for HTTP errors (404, 500, etc.)
    data = response.json()
    
    current = data["current_weather"]
    print(f"Amman Temperature: {current['temperature']}°C")
    print(f"Wind Speed: {current['windspeed']} km/h")

except Exception as e:
    print(f"Error fetching weather: {e}")
    
    
# V2

import requests
from datetime import datetime

def fetch_and_save():
    url = "https://api.open-meteo.com/v1/forecast?latitude=31.95&longitude=35.91&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["current_weather"]
        
        # Prepare the data string
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        weather_info = f"[{timestamp}] Amman: {data['temperature']}°C, Wind: {data['windspeed']}km/h"
        
        print(weather_info)
        
        # Save to file (Append mode 'a')
        with open("weather_log.txt", "a") as file:
            file.write(weather_info + "\n")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

fetch_and_save()


# V3

import requests
import json
from datetime import datetime

# Weather codes from Open-Meteo documentation
WEATHER_CODES = {0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast"}

def get_weather_advanced(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "timezone": "auto"
    }
    api_url = "https://api.open-meteo.com/v1/forecast"
    
    try:
        res = requests.get(api_url, params=params, timeout=5)
        res.raise_for_status()
        data = res.json()["current_weather"]
        
        # Structure the data
        report = {
            "time": datetime.now().isoformat(),
            "temp": data["temperature"],
            "wind": data["windspeed"],
            "condition": WEATHER_CODES.get(data["weathercode"], "Unknown")
        }
        
        save_to_json(report)
        return report

    except requests.exceptions.HTTPError as err:
        return f"HTTP error: {err}"
    except Exception as e:
        return f"Unexpected error: {e}"

def save_to_json(data):
    try:
        with open("weather_history.json", "r+") as f:
            history = json.load(f)
            history.append(data)
            f.seek(0)
            json.dump(history, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("weather_history.json", "w") as f:
            json.dump([data], f, indent=4)

# Run it
result = get_weather_advanced(31.95, 35.91)
print(f"Advanced Report: {result}")