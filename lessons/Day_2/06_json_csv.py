"""
DAY 2 - LESSON 6: JSON & CSV
=============================

Learning Objectives:
- Understand JSON format
- Learn CSV basics
- Practice data formatting
- Work with files using JSON & CSV
- Explore advanced operations
"""

import json
import csv

print("=== JSON & CSV ===\n")

# --------------------------------------------------
# 1️⃣ JSON Example (Dictionary → JSON)
# --------------------------------------------------
data = {
    "name": "Ahmed",
    "age": 25,
    "city": "Cairo"
}

# Convert to JSON string
json_string = json.dumps(data)
print(f"JSON String: {json_string}")

# Pretty JSON (formatted)
pretty_json = json.dumps(data, indent=4)
print("\nPretty JSON:\n", pretty_json)

# --------------------------------------------------
# 2️⃣ Save JSON to file
# --------------------------------------------------
with open("data.json", "w") as f:
    json.dump(data, f)

print("✅ JSON saved!")

# --------------------------------------------------
# 3️⃣ Load JSON from file
# --------------------------------------------------
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(f"Loaded JSON: {loaded_data}")

# Access JSON values
print("Name:", loaded_data["name"])
print("Age:", loaded_data["age"])

# --------------------------------------------------
# 4️⃣ JSON List Example
# --------------------------------------------------
users = [
    {"name": "Ali", "age": 28},
    {"name": "Sara", "age": 24},
    {"name": "Omar", "age": 30}
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("\n✅ users.json created!")

# --------------------------------------------------
# 5️⃣ Read JSON List
# --------------------------------------------------
with open("users.json", "r") as f:
    users_data = json.load(f)

print("Users list:")
for user in users_data:
    print(user["name"], "-", user["age"])

# --------------------------------------------------
# 6️⃣ CSV Example
# --------------------------------------------------
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

# --------------------------------------------------
# 7️⃣ Read CSV
# --------------------------------------------------
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --------------------------------------------------
# 8️⃣ CSV → Dictionary Reader
# --------------------------------------------------
print("\nCSV as Dictionaries:")

with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["City"])

# --------------------------------------------------
# 9️⃣ Write CSV from Dictionaries
# --------------------------------------------------
employees = [
    {"Name": "John", "Age": 30, "Department": "IT"},
    {"Name": "Lina", "Age": 27, "Department": "HR"},
    {"Name": "Mike", "Age": 35, "Department": "Finance"}
]

with open("employees.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "Department"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(employees)

print("\n✅ employees.csv created!")

# --------------------------------------------------
# 🔟 Convert CSV → JSON
# --------------------------------------------------
csv_data = []

with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_data.append(row)

with open("people.json", "w") as f:
    json.dump(csv_data, f, indent=4)

print("✅ Converted CSV → JSON!")

# --------------------------------------------------
# 1️⃣1️⃣ Convert JSON → CSV
# --------------------------------------------------
with open("users.json", "r") as f:
    json_data = json.load(f)

with open("users_converted.csv", "w", newline="") as f:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(json_data)

print("✅ Converted JSON → CSV!")

# --------------------------------------------------
print("\n✅ Lesson 6 Complete!")
