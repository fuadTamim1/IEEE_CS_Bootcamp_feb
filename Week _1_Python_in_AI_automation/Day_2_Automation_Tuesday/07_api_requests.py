"""
DAY 2 - LESSON 7: Making API Requests
===================================

Learning Objectives:
- Understand what APIs are and how they work
- Learn how to make HTTP requests with the requests library
- Learn to handle JSON responses from APIs
- Practice working with real APIs
- Understand API authentication basics

Key Concepts:
- API: Application Programming Interface, allows programs to communicate
- HTTP: Protocol for transferring data over the internet
- requests library: Python library for making HTTP requests
- GET request: Retrieve data from a server
- POST request: Send data to a server
- JSON response: Data returned from API in JSON format
"""

# ===== SECTION 1: Installing requests library =====
print("=== REQUESTS LIBRARY ===\n")

print("To use the requests library, install it with:")
print("  pip install requests")
print()

# Check if requests is available
try:
    import requests
    print("✓ requests library is installed")
except ImportError:
    print("✗ requests library not found")
    print("  Install with: pip install requests")
    print()
    print("Continuing with examples that show how it would work...")


# ===== SECTION 2: Understanding HTTP Methods =====
print("\n=== HTTP METHODS ===\n")

print("""
HTTP Methods:
- GET: Retrieve data from server
- POST: Send data to server
- PUT: Update data on server
- DELETE: Delete data from server

Example API endpoints:
- GET /api/users - Get list of users
- GET /api/users/123 - Get user with ID 123
- POST /api/users - Create new user
- PUT /api/users/123 - Update user 123
- DELETE /api/users/123 - Delete user 123
""")


# ===== SECTION 3: Basic GET Request =====
print("\n=== BASIC GET REQUEST ===\n")

print("Code example - Simple GET request:")
code_example = """
import requests

# Make a GET request to an API
response = requests.get('https://api.example.com/users')

# Check if request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")
"""
print(code_example)


# ===== SECTION 4: Working with API Responses =====
print("\n=== API RESPONSES ===\n")

print("""
When you make an API request, you get a Response object with:

response.status_code
  - 200: OK (successful)
  - 404: Not Found
  - 500: Server Error

response.json()
  - Returns the response body as Python dictionary

response.text
  - Returns the response body as text

response.headers
  - Returns the response headers

response.url
  - Returns the URL that was requested
""")


# ===== SECTION 5: Example - OpenWeatherMap API (Simulated) =====
print("\n=== WEATHER API EXAMPLE (SIMULATED) ===\n")

# Simulating an API response
simulated_weather_response = {
    "coord": {"lon": 31.2454, "lat": 30.0444},
    "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
    "main": {
        "temp": 28.5,
        "feels_like": 27.8,
        "temp_min": 25.0,
        "temp_max": 31.0,
        "pressure": 1013,
        "humidity": 65
    },
    "wind": {"speed": 3.5},
    "clouds": {"all": 5},
    "sys": {"country": "EG", "sunrise": 1612345600, "sunset": 1612385600},
    "name": "Cairo"
}

print("Simulated Weather API Response for Cairo:")
print(f"City: {simulated_weather_response['name']}")
print(f"Temperature: {simulated_weather_response['main']['temp']}°C")
print(f"Feels like: {simulated_weather_response['main']['feels_like']}°C")
print(f"Condition: {simulated_weather_response['weather'][0]['main']}")
print(f"Humidity: {simulated_weather_response['main']['humidity']}%")
print(f"Wind Speed: {simulated_weather_response['wind']['speed']} m/s")


# ===== SECTION 6: Making Requests with Parameters =====
print("\n\n=== REQUESTS WITH PARAMETERS ===\n")

print("Code example - GET request with parameters:")
code_example = """
import requests

# Method 1: Add parameters in URL
url = 'https://api.example.com/search'
params = {'q': 'python', 'limit': 10}
response = requests.get(url, params=params)

# This creates URL: https://api.example.com/search?q=python&limit=10

# Method 2: Pass headers
headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get(url, params=params, headers=headers)
"""
print(code_example)


# ===== SECTION 7: POST Requests =====
print("\n=== POST REQUESTS ===\n")

print("Code example - POST request:")
code_example = """
import requests
import json

# Create new data
new_user = {
    'name': 'Ahmed Hassan',
    'email': 'ahmed@example.com',
    'age': 25
}

# Make POST request
url = 'https://api.example.com/users'
response = requests.post(url, json=new_user)

if response.status_code == 201:  # Created
    created_user = response.json()
    print(f"User created with ID: {created_user['id']}")
"""
print(code_example)


# ===== SECTION 8: Error Handling =====
print("\n=== ERROR HANDLING ===\n")

print("Code example - Handling API errors:")
code_example = """
import requests

try:
    response = requests.get('https://api.example.com/users', timeout=5)
    response.raise_for_status()  # Raise error for bad status codes
    data = response.json()
    print(data)
    
except requests.exceptions.Timeout:
    print("Request timed out")
    
except requests.exceptions.ConnectionError:
    print("Connection error")
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
    
except ValueError:
    print("Response is not JSON")
"""
print(code_example)


# ===== SECTION 9: Real World Example - Weather API =====
print("\n=== REAL WORLD EXAMPLE: WEATHER DATA ===\n")

print("""
This example shows how to:
1. Make a request to a real weather API
2. Parse the JSON response
3. Display formatted weather information
4. Handle errors
""")

# Create a simulated weather fetcher
def get_weather_data_simulated(city):
    \"\"\"
    Simulate getting weather data from an API.
    In real scenario, this would use requests.get()
    \"\"\"
    # Simulated response
    weather_data = {
        "Cairo": {
            "temperature": 28.5,
            "condition": "Clear Sky",
            "humidity": 65,
            "wind_speed": 3.5
        },
        "Dubai": {
            "temperature": 32.0,
            "condition": "Sunny",
            "humidity": 45,
            "wind_speed": 4.2
        },
        "Alexandria": {
            "temperature": 25.0,
            "condition": "Partly Cloudy",
            "humidity": 75,
            "wind_speed": 5.1
        }
    }
    
    if city in weather_data:
        return weather_data[city]
    else:
        return None

# Use the function
cities = ["Cairo", "Dubai", "Alexandria"]
print("Current Weather:\n")
for city in cities:
    weather = get_weather_data_simulated(city)
    if weather:
        print(f"{city}:")
        print(f"  Temperature: {weather['temperature']}°C")
        print(f"  Condition: {weather['condition']}")
        print(f"  Humidity: {weather['humidity']}%")
        print(f"  Wind Speed: {weather['wind_speed']} m/s")
        print()


# ===== SECTION 10: Saving API Data to File =====
print("=== SAVING API DATA ===\n")

import json

# Simulated API response
api_data = {
    "users": [
        {"id": 1, "name": "Ahmed", "role": "Admin"},
        {"id": 2, "name": "Sara", "role": "User"},
        {"id": 3, "name": "Ali", "role": "User"}
    ]
}

# Save to JSON file
filename = "api_response.json"
with open(filename, 'w') as file:
    json.dump(api_data, file, indent=2)

print(f"✓ API response saved to {filename}")

# Read back and process
with open(filename, 'r') as file:
    loaded_data = json.load(file)

print(f"\nUsers from API:")
for user in loaded_data['users']:
    print(f"  {user['name']} ({user['role']})")


# ===== SECTION 11: API Rate Limiting and Best Practices =====
print("\n=== API BEST PRACTICES ===\n")

print("""
1. Rate Limiting
   - APIs often limit requests per minute/hour
   - Check API documentation for limits
   - Use delays between requests: time.sleep(1)

2. Authentication
   - Many APIs require API keys
   - Include in headers or parameters
   - Keep keys secure (don't commit to git)

3. Error Handling
   - Always check response status codes
   - Handle timeouts and connection errors
   - Provide meaningful error messages

4. Caching
   - Cache responses to avoid duplicate requests
   - Save data locally when possible

5. Testing
   - Test with small requests first
   - Use try-except blocks
   - Log all requests and responses

Example:
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers, timeout=5)
""")


# ===== SECTION 12: Practice - Data Collection Script =====
print("\n=== PRACTICE: DATA COLLECTION ===\n")

def collect_and_save_data():
    \"\"\"
    Example of collecting data from multiple sources
    and saving to a file.
    \"\"\"
    
    # Simulated data collection
    collected_data = {
        "timestamp": "2026-02-17T17:00:00",
        "sources": [
            {
                "name": "Weather API",
                "status": "Success",
                "records": 3,
                "data": [
                    {"city": "Cairo", "temp": 28.5},
                    {"city": "Dubai", "temp": 32.0},
                    {"city": "Alexandria", "temp": 25.0}
                ]
            },
            {
                "name": "News API",
                "status": "Success",
                "records": 5,
                "data": [
                    {"title": "Python 3.11 Released", "source": "TechNews"},
                    {"title": "AI Breakthroughs", "source": "ScienceDaily"}
                ]
            }
        ]
    }
    
    # Save to file
    output_file = "collected_data.json"
    with open(output_file, 'w') as file:
        json.dump(collected_data, file, indent=2)
    
    return output_file

output_file = collect_and_save_data()
print(f"✓ Data collection complete")
print(f"  Saved to: {output_file}")

# Verify
with open(output_file, 'r') as file:
    data = json.load(file)
    print(f"  Total sources: {len(data['sources'])}")
    for source in data['sources']:
        print(f"  - {source['name']}: {source['records']} records")


# ===== SECTION 13: Full Working Example =====
print("\n=== FULL WORKING EXAMPLE ===\n")

print("""
Here's a complete script structure for an API data fetcher:

```python
import requests
import json
from datetime import datetime

def fetch_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None

def save_weather_data(city, data):
    filename = f"{city}_weather.json"
    with open(filename, 'w') as file:
        json.dump({
            'city': city,
            'timestamp': datetime.now().isoformat(),
            'data': data
        }, file, indent=2)
    return filename

# Usage:
# api_key = 'your_api_key_here'
# weather = fetch_weather('Cairo', api_key)
# if weather:
#     save_weather_data('Cairo', weather)
```
""")

print("\n✅ Lesson 7 Complete!")
print("Next: Error Handling and Debugging")
