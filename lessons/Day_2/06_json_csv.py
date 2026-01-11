"""
DAY 2 - LESSON 6: JSON & CSV
=============================

Learning Objectives:
- Understand JSON format
- Learn CSV basics
- Practice data formatting
"""

import json
import csv

print("=== JSON & CSV ===\n")

# JSON Example
data = {
    "name": "Ahmed",
    "age": 25,
    "city": "Cairo"
}

# Convert to JSON string
json_string = json.dumps(data)
print(f"JSON String: {json_string}")

# Save JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)
print("✅ JSON saved!")

# Load JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(f"Loaded JSON: {loaded_data}")

# CSV Example
print("\n--- CSV Example ---")
people = [
    ["Name", "Age", "City"],
    ["Ahmed", "25", "Cairo"],
    ["Fatima", "22", "Alexandria"],
    ["Ali", "28", "Giza"]
]

# Write CSV
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(people)
print("✅ CSV file created!")

# Read CSV
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("\n✅ Lesson 6 Complete!")
