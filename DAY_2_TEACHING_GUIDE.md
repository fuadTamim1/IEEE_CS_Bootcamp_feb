# Day 2: Python for Automation & Data Handling
## Tuesday Teaching Guide (2 Hours)

---

## 📋 Session Overview

**Date**: Tuesday, February 17, 2026  
**Time**: 5:00 PM - 7:00 PM  
**Duration**: 2 hours  
**Focus**: File operations, APIs, and real-world automation

---

## 🎯 Learning Objectives

By the end of this session, students will be able to:
- Read and write text files programmatically
- Work with structured data (CSV and JSON)
- Make API requests to external services
- Parse and save API responses
- Build automated data workflows
- Handle errors gracefully
- Create a complete automation script

---

## 📚 Session Outline

### Part 1: File Handling (5:00 - 5:45 PM) - 45 minutes

#### 5:00-5:15: Working with Text Files (15 min)
#### 5:15-5:30: CSV Files & Data Tables (15 min)
#### 5:30-5:45: JSON Files & Structured Data (15 min)

### Part 2: Automation Libraries & APIs (5:45 - 6:25 PM) - 40 minutes

#### 5:45-6:05: Automation Libraries (os, pathlib, time) (20 min)
#### 6:05-6:25: API Requests & External Data (20 min)

### Part 3: Live Demo (6:25 - 6:50 PM) - 25 minutes

#### 6:25-6:50: Weather API Automation Project (25 min)

### Part 4: Error Handling & Wrap-up (6:50 - 7:00 PM) - 10 minutes

#### 6:50-7:00: Error Handling & Q&A (10 min)

---

## 🎓 Detailed Teaching Plan

---

## Part 1: File Handling (5:00 - 5:45 PM)

### 5:00-5:15: Working with Text Files (15 min)

**Opening Hook:**
> "Day 1 was Python basics. Today, Python meets the REAL world - files, data, and the internet!"

**Teaching Points:**

#### Why File Handling Matters for Automation
- **Log files** - Track what your automation does
- **Configuration** - Store settings
- **Data processing** - Read input, write output
- **Reports** - Generate automated reports

---

#### Reading Text Files

**Live Demo:**

**File: `05_file_handling.py`**
```python
# Reading a text file - Method 1: Read all at once
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Better way: Using 'with' (automatically closes file)
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\n=== Reading Line by Line ===")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra whitespace

# Reading all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print(f"First line: {lines[0]}")
```

**Create `sample.txt` first:**
```text
Welcome to Python Automation!
This is line 2.
Python makes file handling easy.
We can read and write files effortlessly.
```

---

#### Writing Text Files

```python
# Writing to a file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("This is my automated output.\n")
    file.write("Python wrote this!\n")

print("File created: output.txt")

# Appending to a file (adds to existing content)
with open("output.txt", "a") as file:
    file.write("This line was appended.\n")

print("Content appended to output.txt")

# Practical example: Logging
def log_action(action):
    """Logs actions to a file with timestamp"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("automation_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {action}\n")

# Test the logger
log_action("Program started")
log_action("Processing file: data.csv")
log_action("File processed successfully")
print("Check automation_log.txt for logs!")
```

**Key Concepts:**
- **File modes:**
  - `"r"` - Read (file must exist)
  - `"w"` - Write (creates new or overwrites)
  - `"a"` - Append (adds to end)
- **`with` statement** - Auto-closes files (best practice!)
- **`.read()`** - Read entire file
- **`.readlines()`** - Read as list of lines
- **`.write()`** - Write to file

**Quick Practice (2 min):**
```python
# Students create a simple note-taking app
note = input("Enter a note: ")
with open("my_notes.txt", "a") as file:
    file.write(note + "\n")
print("Note saved!")
```

---

### 5:15-5:30: CSV Files & Data Tables (15 min)

**Teaching Points:**

#### What is CSV?
> "CSV (Comma-Separated Values) is like a spreadsheet in text format. It's how we store tabular data."

**Example CSV:**
```csv
name,age,city,job
Alice,25,Dubai,Engineer
Bob,30,Abu Dhabi,Designer
Charlie,28,Sharjah,Developer
```

---

#### Working with CSV Files

**Live Demo:**

**File: `06_csv_demo.py`**
```python
import csv

# Create a sample CSV file
print("Creating sample CSV file...")
with open("employees.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city", "job"])
    writer.writerow(["Alice", 25, "Dubai", "Engineer"])
    writer.writerow(["Bob", 30, "Abu Dhabi", "Designer"])
    writer.writerow(["Charlie", 28, "Sharjah", "Developer"])

print("Created: employees.csv\n")

# Reading CSV file
print("=== Reading CSV ===")
with open("employees.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Get first line (header)
    print(f"Columns: {header}\n")
    
    for row in csv_reader:
        name, age, city, job = row
        print(f"{name} is {age} years old, works as {job} in {city}")

# Reading CSV as dictionary (better!)
print("\n=== Reading CSV as Dictionary ===")
with open("employees.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(f"{row['name']} - {row['job']}")

# Filtering data
print("\n=== Filtering: People in Dubai ===")
with open("employees.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        if row['city'] == "Dubai":
            print(f"{row['name']} works in Dubai")

# Writing filtered results to new CSV
print("\n=== Creating Filtered CSV ===")
with open("employees.csv", "r") as infile:
    csv_reader = csv.DictReader(infile)
    
    with open("engineers.csv", "w", newline='') as outfile:
        fieldnames = ["name", "age", "city", "job"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in csv_reader:
            if row['job'] == "Engineer":
                writer.writerow(row)

print("Created: engineers.csv (only engineers)")

# Practical automation example
print("\n=== Automation Example: Processing Sales Data ===")

# Create sample sales data
sales_data = [
    ["product", "quantity", "price"],
    ["Laptop", 5, 1200],
    ["Mouse", 20, 25],
    ["Keyboard", 15, 75],
    ["Monitor", 8, 300]
]

with open("sales.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

# Process sales data: Calculate total revenue
with open("sales.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    total_revenue = 0
    print("\nSales Report:")
    print("-" * 40)
    
    for row in csv_reader:
        product = row['product']
        quantity = int(row['quantity'])
        price = float(row['price'])
        revenue = quantity * price
        total_revenue += revenue
        print(f"{product}: {quantity} × ${price} = ${revenue}")
    
    print("-" * 40)
    print(f"Total Revenue: ${total_revenue}")

# Save report to file
with open("sales_report.txt", "w") as file:
    file.write("=== Sales Report ===\n")
    file.write(f"Total Revenue: ${total_revenue}\n")
    file.write(f"Generated: {datetime.datetime.now()}\n")

print("\nReport saved to: sales_report.txt")
```

**Key Concepts:**
- **`csv.reader()`** - Read CSV rows as lists
- **`csv.writer()`** - Write CSV rows
- **`csv.DictReader()`** - Read rows as dictionaries (cleaner!)
- **`csv.DictWriter()`** - Write dictionaries to CSV
- **`newline=''`** - Prevents blank rows on Windows

**Automation Connection:**
> "This is how automation systems process data! Export from Excel, process with Python, generate reports automatically."

---

### 5:30-5:45: JSON Files & Structured Data (15 min)

**Teaching Points:**

#### What is JSON?
> "JSON (JavaScript Object Notation) is the language of APIs. If CSV is a table, JSON is a smart filing cabinet with nested folders."

**Example JSON:**
```json
{
  "name": "Alice",
  "age": 25,
  "city": "Dubai",
  "skills": ["Python", "JavaScript", "SQL"],
  "active": true
}
```

---

#### Working with JSON Files

**Live Demo:**

**File: `06_json_demo.py`**
```python
import json

# Creating JSON data
print("=== Creating JSON ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "Dubai",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_student": False,
    "projects": [
        {"name": "File Organizer", "status": "completed"},
        {"name": "Chatbot", "status": "in progress"}
    ]
}

# Writing JSON to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

print("Created: person.json\n")

# Reading JSON from file
print("=== Reading JSON ===")
with open("person.json", "r") as file:
    data = json.load(file)

print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"Skills: {', '.join(data['skills'])}")
print(f"Projects:")
for project in data['projects']:
    print(f"  - {project['name']}: {project['status']}")

# Converting Python dict to JSON string
print("\n=== JSON String ===")
json_string = json.dumps(person, indent=2)
print(json_string)

# Converting JSON string to Python dict
print("\n=== Parsing JSON String ===")
parsed = json.loads(json_string)
print(type(parsed))  # <class 'dict'>

# Practical example: Configuration file
print("\n=== Configuration File Example ===")
config = {
    "app_name": "File Organizer",
    "version": "1.0",
    "settings": {
        "auto_organize": True,
        "target_folder": "C:/Users/Downloads",
        "categories": {
            "images": [".jpg", ".png", ".gif"],
            "documents": [".pdf", ".docx", ".txt"],
            "media": [".mp4", ".mp3", ".avi"]
        }
    }
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("Created: config.json")

# Reading and using config
with open("config.json", "r") as file:
    app_config = json.load(file)

print(f"\nApp: {app_config['app_name']} v{app_config['version']}")
print(f"Auto-organize: {app_config['settings']['auto_organize']}")
print(f"Image extensions: {app_config['settings']['categories']['images']}")

# Practical example: Saving automation results
print("\n=== Automation Results ===")
automation_results = {
    "timestamp": "2026-02-17 18:30:00",
    "task": "File Organization",
    "files_processed": 47,
    "categories": {
        "images": 15,
        "documents": 22,
        "media": 8,
        "other": 2
    },
    "errors": [],
    "duration_seconds": 2.5,
    "status": "success"
}

with open("automation_results.json", "w") as file:
    json.dump(automation_results, file, indent=4)

print("Results saved to: automation_results.json")

# Reading and displaying results
with open("automation_results.json", "r") as file:
    results = json.load(file)

print(f"\n📊 Automation Report:")
print(f"Task: {results['task']}")
print(f"Status: {results['status'].upper()}")
print(f"Files processed: {results['files_processed']}")
print(f"Duration: {results['duration_seconds']}s")
print(f"\nBreakdown:")
for category, count in results['categories'].items():
    print(f"  {category}: {count} files")
```

**Key Concepts:**
- **`json.dump()`** - Write Python object to file
- **`json.load()`** - Read JSON file to Python object
- **`json.dumps()`** - Convert Python object to JSON string
- **`json.loads()`** - Parse JSON string to Python object
- **`indent=4`** - Makes JSON human-readable

**JSON vs CSV:**
```
CSV: Simple tables, spreadsheet data
JSON: Complex nested data, API responses, configs
```

**Quick Practice (2 min):**
```python
# Students create a profile saver
profile = {
    "name": input("Name: "),
    "age": int(input("Age: ")),
    "hobbies": input("Hobbies (comma-separated): ").split(",")
}

with open("my_profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("Profile saved!")
```

---

## Part 2: Automation Libraries & APIs (5:45 - 6:25 PM)

### 5:45-6:05: Automation Libraries (20 min)

**Teaching Points:**

#### Why Use Libraries?
> "Python's power comes from its libraries. Don't reinvent the wheel - use tools others built!"

---

#### The `os` and `pathlib` Libraries

**Live Demo:**

**File: `07_automation_libraries.py`**
```python
import os
from pathlib import Path
import time
import datetime

print("=== Working with Directories ===")

# Current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in directory
print("\nFiles in current directory:")
files = os.listdir(current_dir)
for file in files[:10]:  # Show first 10
    print(f"  - {file}")

# Check if file/folder exists
if os.path.exists("sample.txt"):
    print("\nsample.txt exists!")
else:
    print("\nsample.txt not found")

# Creating directories
print("\n=== Creating Directories ===")
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Created: test_folder")

# Creating nested directories
if not os.path.exists("organized/images/2026"):
    os.makedirs("organized/images/2026")
    print("Created: organized/images/2026")

# File information
print("\n=== File Information ===")
if os.path.exists("sample.txt"):
    file_size = os.path.getsize("sample.txt")
    print(f"sample.txt size: {file_size} bytes")
    
    modified_time = os.path.getmtime("sample.txt")
    modified_date = datetime.datetime.fromtimestamp(modified_time)
    print(f"Last modified: {modified_date}")

# Getting file extension
print("\n=== File Extensions ===")
test_files = ["photo.jpg", "document.pdf", "script.py", "data.csv"]
for file in test_files:
    name, extension = os.path.splitext(file)
    print(f"{file} → Name: '{name}', Extension: '{extension}'")

# Pathlib (modern approach)
print("\n=== Using Pathlib (Modern) ===")
current = Path.cwd()
print(f"Current directory: {current}")

# Better file operations
file_path = Path("sample.txt")
if file_path.exists():
    print(f"File exists: {file_path.name}")
    print(f"File size: {file_path.stat().st_size} bytes")
    print(f"Extension: {file_path.suffix}")

# Creating paths safely
new_path = Path("organized") / "documents" / "2026"
print(f"Path created: {new_path}")

# Practical example: File organizer (simulation)
print("\n=== File Organizer Simulation ===")

def organize_files_simulation():
    """Simulates organizing files by extension"""
    # Simulate file list
    files = [
        "vacation.jpg",
        "report.pdf",
        "photo.png",
        "notes.txt",
        "song.mp3"
    ]
    
    categories = {
        'images': ['.jpg', '.png', '.gif'],
        'documents': ['.pdf', '.txt', '.docx'],
        'media': ['.mp3', '.mp4', '.avi']
    }
    
    for file in files:
        _, ext = os.path.splitext(file)
        
        for category, extensions in categories.items():
            if ext in extensions:
                print(f"Would move {file} → {category}/")
                break

organize_files_simulation()

# Time and scheduling
print("\n=== Time-Based Operations ===")

# Current time
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Measuring execution time
print("\n=== Performance Measurement ===")
start_time = time.time()

# Simulate work
total = 0
for i in range(1000000):
    total += i

end_time = time.time()
duration = end_time - start_time

print(f"Calculation took {duration:.4f} seconds")

# Practical: Automated backup with timestamp
print("\n=== Automated Backup Example ===")

def create_backup(filename):
    """Creates a backup with timestamp"""
    if os.path.exists(filename):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = os.path.splitext(filename)
        backup_name = f"{name}_backup_{timestamp}{ext}"
        print(f"Would backup: {filename} → {backup_name}")
    else:
        print(f"File not found: {filename}")

create_backup("config.json")
create_backup("employees.csv")
```

**Key Concepts:**
- **`os.getcwd()`** - Get current directory
- **`os.listdir()`** - List directory contents
- **`os.path.exists()`** - Check if path exists
- **`os.makedirs()`** - Create nested directories
- **`os.path.splitext()`** - Split filename and extension
- **`Path` from pathlib** - Modern, cleaner approach
- **`time.time()`** - Get current timestamp
- **`datetime`** - Work with dates and times

**Automation Connection:**
> "These are the building blocks of automation! Check files, create folders, measure performance - all automatic."

---

### 6:05-6:25: API Requests & External Data (20 min)

**Teaching Points:**

#### What is an API?
> "API (Application Programming Interface) = A way for programs to talk to each other. Like a waiter taking your order to the kitchen and bringing back food."

**Real-World APIs:**
- Weather data (OpenWeather, WeatherAPI)
- Social media (Twitter, Instagram)
- AI models (OpenAI, Anthropic)
- Maps (Google Maps)
- Currency exchange rates

---

#### Making API Requests

**Live Demo:**

**File: `07_api_requests.py`**
```python
import requests
import json

print("=== Understanding APIs ===\n")

# Example 1: Public API (No key needed)
print("Example 1: Random User API")
print("-" * 40)

response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    data = response.json()
    user = data['results'][0]
    
    print(f"Name: {user['name']['first']} {user['name']['last']}")
    print(f"Email: {user['email']}")
    print(f"Country: {user['location']['country']}")
    print(f"✓ API request successful!\n")
else:
    print(f"✗ Error: {response.status_code}\n")

# Example 2: JSON Placeholder (Testing API)
print("Example 2: Getting Posts")
print("-" * 40)

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    post = response.json()
    print(f"Title: {post['title']}")
    print(f"Body: {post['body'][:100]}...")
    print(f"✓ Post retrieved!\n")

# Example 3: Multiple results
print("Example 3: Getting Multiple Posts")
print("-" * 40)

response = requests.get("https://jsonplaceholder.typicode.com/posts?_limit=5")
posts = response.json()

for post in posts:
    print(f"{post['id']}. {post['title']}")
print()

# Saving API response to file
print("Example 4: Saving API Data")
print("-" * 40)

response = requests.get("https://randomuser.me/api/?results=10")
users = response.json()

with open("random_users.json", "w") as file:
    json.dump(users, file, indent=4)

print("✓ Saved 10 random users to random_users.json\n")

# Processing saved data
print("Example 5: Processing Saved Data")
print("-" * 40)

with open("random_users.json", "r") as file:
    data = json.load(file)

print("User List:")
for user in data['results']:
    name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    print(f"  • {name} - {email}")
print()

# Practical example: Crypto prices (public API)
print("Example 6: Cryptocurrency Prices")
print("-" * 40)

response = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")

if response.status_code == 200:
    data = response.json()
    rates = data['data']['rates']
    
    print(f"Bitcoin Exchange Rates:")
    print(f"  USD: ${float(rates['USD']):,.2f}")
    print(f"  EUR: €{float(rates['EUR']):,.2f}")
    print(f"  GBP: £{float(rates['GBP']):,.2f}")
    print()

# Error handling in API calls
print("Example 7: Handling Errors")
print("-" * 40)

try:
    response = requests.get("https://api.example.com/invalid", timeout=5)
    response.raise_for_status()  # Raises error for bad status codes
except requests.exceptions.ConnectionError:
    print("✗ Connection error - Check your internet")
except requests.exceptions.Timeout:
    print("✗ Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"✗ HTTP error: {e}")
except Exception as e:
    print(f"✗ Unexpected error: {e}")

print()

# Best practices example
print("Example 8: Automated Data Collector")
print("-" * 40)

def fetch_and_save_data(url, filename):
    """Fetches data from API and saves to file"""
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"✓ Data saved to {filename}")
        return True
    
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

# Test the function
success = fetch_and_save_data(
    "https://jsonplaceholder.typicode.com/users",
    "users_data.json"
)

if success:
    print("\nAutomation successful!")
```

**Key Concepts:**
- **`requests.get()`** - Make GET request to API
- **`.status_code`** - HTTP status (200 = success)
- **`.json()`** - Parse JSON response
- **`timeout`** - Prevent hanging requests
- **`.raise_for_status()`** - Raise exception for errors
- **Try/except** - Handle API failures gracefully

**Status Codes:**
```
200 - OK (Success)
404 - Not Found
429 - Too Many Requests (Rate limit)
500 - Server Error
```

---

## Part 3: Live Demo - Weather API Automation (6:25 - 6:50 PM)

### 6:25-6:50: Complete Weather Automation Project (25 min)

**Teaching Strategy:**
- Build this live, step by step
- Explain each part as you code
- Students code along
- This is the highlight of Day 2!

---

**Live Project:**

**File: `weather_automation.py`**
```python
"""
Weather API Automation
Fetches weather data and saves it to files
Demonstrates: API requests, JSON, file handling, error handling
"""

import requests
import json
from datetime import datetime
import os

# Configuration
API_KEY = "your_api_key_here"  # Get free key from openweathermap.org
CITIES = ["Dubai", "Abu Dhabi", "London", "New York", "Tokyo"]

def get_weather(city, api_key):
    """Fetches weather data for a city"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return None

def format_weather_report(city, weather_data):
    """Formats weather data into readable report"""
    if not weather_data:
        return f"No data available for {city}"
    
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    report = f"""
{'=' * 50}
Weather Report: {city}
{'=' * 50}
Temperature: {temp}°C (Feels like {feels_like}°C)
Conditions: {description.title()}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
{'=' * 50}
    """
    return report

def save_weather_data(city, weather_data, folder="weather_data"):
    """Saves weather data to JSON file"""
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{city}_{timestamp}.json"
    
    with open(filename, "w") as file:
        json.dump(weather_data, file, indent=4)
    
    print(f"✓ Saved data to {filename}")

def generate_summary_report(all_weather_data):
    """Generates a summary of all cities"""
    report_lines = [
        "=" * 60,
        "WEATHER SUMMARY REPORT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 60,
        ""
    ]
    
    for city, data in all_weather_data.items():
        if data:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            report_lines.append(f"{city:20} {temp:6.1f}°C  {description}")
        else:
            report_lines.append(f"{city:20} {'Data unavailable':^20}")
    
    report_lines.append("=" * 60)
    report = "\n".join(report_lines)
    
    # Save to file
    with open("weather_summary.txt", "w") as file:
        file.write(report)
    
    return report

def main():
    """Main automation function"""
    print("\n🌤️  Weather Automation Starting...")
    print(f"Fetching weather for {len(CITIES)} cities\n")
    
    all_weather_data = {}
    
    # Fetch weather for each city
    for city in CITIES:
        print(f"Fetching weather for {city}...")
        weather_data = get_weather(city, API_KEY)
        
        if weather_data:
            all_weather_data[city] = weather_data
            
            # Display report
            report = format_weather_report(city, weather_data)
            print(report)
            
            # Save individual city data
            save_weather_data(city, weather_data)
        else:
            all_weather_data[city] = None
            print(f"✗ Failed to get weather for {city}\n")
    
    # Generate summary
    print("\nGenerating summary report...")
    summary = generate_summary_report(all_weather_data)
    print("\n" + summary)
    print("\n✓ Weather automation completed!")
    print("Check 'weather_data' folder and 'weather_summary.txt'")

if __name__ == "__main__":
    main()
```

---

**Teaching Process:**

**Step 1: Explain the Goal (2 min)**
> "We're building a system that automatically fetches weather for multiple cities, saves the data, and creates a summary report. This is real automation!"

**Step 2: API Setup (3 min)**
- Show how to get free API key from openweathermap.org
- Explain API documentation
- Show example API URL

**Step 3: Build Functions One by One (15 min)**

1. **`get_weather()` function** (4 min)
   - Explain URL building
   - Show params dictionary
   - Demonstrate try/except

2. **`format_weather_report()` function** (3 min)
   - Parse JSON structure
   - Extract relevant data
   - Format nicely

3. **`save_weather_data()` function** (3 min)
   - Create folder if needed
   - Generate timestamped filename
   - Save JSON

4. **`generate_summary_report()` function** (3 min)
   - Loop through all cities
   - Format table-like output
   - Save to text file

5. **`main()` function** (2 min)
   - Orchestrate everything
   - Show progress
   - Error handling

**Step 4: Run and Demo (3 min)**
- Execute the script
- Show live API calls
- Display results
- Show created files

**Step 5: Discussion (2 min)**
- How could we extend this?
- What other APIs could we use?
- How would we schedule this to run daily?

---

**Backup Plan (if API key issues):**
```python
# Use mock data instead
def get_weather_mock(city):
    """Returns mock weather data for demo"""
    mock_data = {
        "Dubai": {"main": {"temp": 35, "feels_like": 38, "humidity": 60}, 
                  "weather": [{"description": "sunny"}],
                  "wind": {"speed": 3.5}},
        "London": {"main": {"temp": 15, "feels_like": 13, "humidity": 75},
                   "weather": [{"description": "cloudy"}],
                   "wind": {"speed": 5.2}}
    }
    return mock_data.get(city)
```

---

## Part 4: Error Handling & Wrap-up (6:50 - 7:00 PM)

### 6:50-7:00: Error Handling & Q&A (10 min)

**Teaching Points:**

#### Error Handling Essentials (5 min)

```python
# Basic try/except
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")

# File handling with errors
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found - creating new file")
    with open("data.txt", "w") as file:
        file.write("New file created")

# API with errors (complete example)
import requests

def safe_api_call(url):
    """Makes API call with comprehensive error handling"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.ConnectionError:
        return None, "No internet connection"
    except requests.exceptions.Timeout:
        return None, "Request timed out"
    except requests.exceptions.HTTPError as e:
        return None, f"HTTP error: {e}"
    except ValueError:
        return None, "Invalid JSON response"
    except Exception as e:
        return None, f"Unexpected error: {e}"

# Usage
data, error = safe_api_call("https://api.example.com/data")
if error:
    print(f"Error: {error}")
else:
    print(f"Success: {data}")
```

**Key Concepts:**
- Always handle potential errors in automation
- Specific exceptions before general Exception
- Provide helpful error messages
- Log errors for debugging

---

### Review Key Concepts (3 min)

**Today We Learned:**
- ✅ File handling (text, CSV, JSON)
- ✅ Automation libraries (os, pathlib, time)
- ✅ API requests and data fetching
- ✅ Building complete automation workflows
- ✅ Error handling for robust code

**Connection to Final Project:**
> "You now have everything you need for the File Organizer project! You can read folders, move files, and log results."

---

### Preview Day 3 (1 min)

> "Thursday is about the big picture - where does Python fit in AI? What libraries power AI? What's your next step?"

- AI/ML workflow explained
- Overview of AI libraries
- Automation pipelines
- Career roadmap
- Project work time

---

### Q&A (1 min)

Open floor for questions

---

## 📊 Teaching Tips for Day 2

### Pacing
- **File handling can drag** - Keep examples short
- **API demo is the star** - Allocate extra time if needed
- **Students love seeing real data** - Make it visual

### Common Issues

**"My API isn't working!"**
- Have backup mock data ready
- Check API key is correct
- Verify internet connection
- Show how to read API error messages

**"I get FileNotFoundError!"**
- Explain absolute vs relative paths
- Show how to check current directory
- Use os.path.exists() before reading

**"CSV looks weird in Notepad!"**
- Open in Excel or VS Code for better view
- Explain newline parameter
- Show proper way to view CSV

### Engagement Tips
- Make API calls interactive (students suggest cities)
- Show real-world automation examples
- Celebrate when API returns data
- Compare manual vs automated workflows

---

## ✅ Success Checklist

After Day 2, students should:
- [ ] Read and write files confidently
- [ ] Parse CSV and JSON data
- [ ] Make API requests
- [ ] Build automated workflows
- [ ] Handle errors properly
- [ ] See practical applications

---

## 📝 Materials for Day 3

**Prepare:**
- NumPy/Pandas overview slides
- AI workflow diagram
- n8n demo (optional)
- Roadmap visual
- Project starter files

**Remind students:**
- Final project due after Day 3
- Two options available
- Need to choose soon

---

**You've got this! Day 2 is where Python becomes powerful! 🚀**
