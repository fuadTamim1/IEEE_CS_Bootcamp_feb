"""
DAY 2 - LESSON 6: JSON and CSV Data Formats
=========================================

Learning Objectives:
- Understand JSON format and its structure
- Learn how to read and write JSON files
- Understand CSV format and its uses
- Learn how to work with CSV files
- Practice converting between formats

Key Concepts:
- JSON: JavaScript Object Notation, human-readable data format
- CSV: Comma-Separated Values, tabular data format
- json module: Python's built-in JSON support
- csv module: Python's built-in CSV support
- Data serialization: Converting data to storable format
"""

import json
import csv
import os

# ===== SECTION 1: Introduction to JSON =====
print("=== INTRODUCTION TO JSON ===\n")

# JSON Structure
# Objects (dictionaries): {"key": "value"}
# Arrays (lists): [1, 2, 3]
# Values: strings, numbers, booleans, null, objects, arrays

# Example JSON data
json_string = '''
{
    "name": "Ahmed",
    "age": 25,
    "is_student": true,
    "courses": ["Python", "JavaScript", "Data Science"],
    "address": {
        "city": "Cairo",
        "country": "Egypt"
    }
}
'''

print("JSON Example:")
print(json_string)


# ===== SECTION 2: Creating and Writing JSON Files =====
print("\n=== WRITING JSON FILES ===\n")

# Python dictionary to be converted to JSON
student = {
    "name": "Sara",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Web Dev", "Databases"],
    "active": True
}

# Write to JSON file
filename = "student.json"
with open(filename, 'w') as file:
    json.dump(student, file, indent=4)

print(f"✓ Created {filename}")
print("\nFile content:")
with open(filename, 'r') as file:
    print(file.read())


# ===== SECTION 3: Reading JSON Files =====
print("\n=== READING JSON FILES ===\n")

# Read from JSON file
with open(filename, 'r') as file:
    loaded_student = json.load(file)

print(f"Loaded data type: {type(loaded_student)}")
print(f"Student name: {loaded_student['name']}")
print(f"Student courses: {loaded_student['courses']}")
print(f"GPA: {loaded_student['gpa']}")


# ===== SECTION 4: Working with JSON Arrays =====
print("\n=== JSON ARRAYS ===\n")

# Create a list of students
students = [
    {"name": "Ahmed", "age": 25, "score": 95},
    {"name": "Fatima", "age": 23, "score": 88},
    {"name": "Ali", "age": 24, "score": 92},
    {"name": "Sara", "age": 22, "score": 90}
]

# Write to JSON file
filename = "students.json"
with open(filename, 'w') as file:
    json.dump(students, file, indent=4)

print(f"✓ Created {filename}")

# Read and process
with open(filename, 'r') as file:
    loaded_students = json.load(file)

print(f"\nTotal students: {len(loaded_students)}")
for student in loaded_students:
    print(f"  {student['name']}: Score {student['score']}")

# Find average score
avg_score = sum(s['score'] for s in loaded_students) / len(loaded_students)
print(f"Average score: {avg_score:.2f}")


# ===== SECTION 5: Modifying JSON Data =====
print("\n=== MODIFYING JSON DATA ===\n")

# Load existing JSON
with open(filename, 'r') as file:
    students = json.load(file)

# Modify data
students[0]['score'] = 98  # Update Ahmed's score
students.append({"name": "Omar", "age": 26, "score": 85})  # Add new student

# Save modified data
with open(filename, 'w') as file:
    json.dump(students, file, indent=4)

print(f"✓ Updated {filename}")
print("New content:")
with open(filename, 'r') as file:
    print(file.read())


# ===== SECTION 6: JSON String Conversion =====
print("\n=== JSON STRING CONVERSION ===\n")

# Convert Python object to JSON string
person = {"name": "Ali", "age": 30, "city": "Dubai"}
json_string = json.dumps(person, indent=2)

print("JSON String:")
print(json_string)
print(f"Type: {type(json_string)}")

# Convert JSON string back to Python object
parsed = json.loads(json_string)
print(f"\nParsed back to Python:")
print(f"Name: {parsed['name']}")
print(f"Age: {parsed['age']}")


# ===== SECTION 7: Introduction to CSV =====
print("\n=== INTRODUCTION TO CSV ===\n")

# CSV Example
csv_content = """Name,Age,City
Ahmed,25,Cairo
Sara,23,Alexandria
Ali,24,Giza
Fatima,22,Aswan"""

print("CSV Format Example:")
print(csv_content)


# ===== SECTION 8: Writing CSV Files =====
print("\n\n=== WRITING CSV FILES ===\n")

# Data to write
employees = [
    ["Name", "Department", "Salary"],
    ["Ahmed", "IT", 50000],
    ["Fatima", "HR", 45000],
    ["Ali", "Sales", 40000],
    ["Sara", "IT", 55000]
]

# Write to CSV file
filename = "employees.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print(f"✓ Created {filename}")
print("\nFile content:")
with open(filename, 'r') as file:
    print(file.read())


# ===== SECTION 9: Reading CSV Files =====
print("\n=== READING CSV FILES ===\n")

# Read from CSV file
filename = "employees.csv"
with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

print(f"Headers: {rows[0]}")
print(f"\nEmployee data:")
for row in rows[1:]:
    print(f"  {row[0]}: {row[1]} department, ${row[2]}")

# Calculate average salary
salaries = [int(row[2]) for row in rows[1:]]
avg_salary = sum(salaries) / len(salaries)
print(f"\nAverage salary: ${avg_salary:,.2f}")


# ===== SECTION 10: Working with CSV Dictionaries =====
print("\n=== CSV WITH DICTIONARIES ===\n")

# Write CSV with column names
filename = "products.csv"
fieldnames = ["Product", "Price", "Quantity", "Category"]

products = [
    {"Product": "Laptop", "Price": 1200, "Quantity": 5, "Category": "Electronics"},
    {"Product": "Mouse", "Price": 25, "Quantity": 50, "Category": "Electronics"},
    {"Product": "Desk", "Price": 300, "Quantity": 10, "Category": "Furniture"},
    {"Product": "Chair", "Price": 150, "Quantity": 15, "Category": "Furniture"}
]

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"✓ Created {filename}")

# Read CSV with DictReader
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Product']}: ${row['Price']} ({row['Quantity']} in stock)")


# ===== SECTION 11: Data Format Conversion =====
print("\n=== CONVERTING BETWEEN FORMATS ===\n")

# Create data in JSON
json_data = [
    {"name": "Project A", "status": "Active", "budget": 50000},
    {"name": "Project B", "status": "Complete", "budget": 75000},
    {"name": "Project C", "status": "Active", "budget": 60000}
]

# Save as JSON
json_file = "projects.json"
with open(json_file, 'w') as file:
    json.dump(json_data, file, indent=2)

# Convert to CSV
csv_file = "projects.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "status", "budget"])
    writer.writeheader()
    writer.writerows(json_data)

print(f"✓ Converted JSON to CSV")
print(f"JSON file: {json_file}")
print(f"CSV file: {csv_file}")

# Read back and verify
print("\nJSON Content:")
with open(json_file, 'r') as file:
    print(file.read())

print("\nCSV Content:")
with open(csv_file, 'r') as file:
    print(file.read())


# ===== SECTION 12: Practical Example - Student Database =====
print("\n=== PRACTICAL EXAMPLE: STUDENT DATABASE ===\n")

# Create sample data
students_data = {
    "students": [
        {
            "id": 1,
            "name": "Ahmed Hassan",
            "email": "ahmed@example.com",
            "gpa": 3.8,
            "courses": ["Python", "Web Dev"]
        },
        {
            "id": 2,
            "name": "Sara Mohamed",
            "email": "sara@example.com",
            "gpa": 3.9,
            "courses": ["Python", "Data Science", "ML"]
        },
        {
            "id": 3,
            "name": "Ali Ibrahim",
            "email": "ali@example.com",
            "gpa": 3.5,
            "courses": ["Python", "Web Dev"]
        }
    ]
}

# Save as JSON
json_file = "students_db.json"
with open(json_file, 'w') as file:
    json.dump(students_data, file, indent=2)

print(f"✓ Created student database: {json_file}")

# Read and create CSV report
csv_file = "students_report.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Email", "GPA", "Courses"])
    
    for student in students_data['students']:
        courses_str = ", ".join(student['courses'])
        writer.writerow([
            student['id'],
            student['name'],
            student['email'],
            student['gpa'],
            courses_str
        ])

print(f"✓ Created report: {csv_file}")

# Display the report
print("\nStudent Report:")
with open(csv_file, 'r') as file:
    print(file.read())

# Query JSON data
print("Students with GPA >= 3.8:")
for student in students_data['students']:
    if student['gpa'] >= 3.8:
        print(f"  {student['name']}: {student['gpa']}")


print("\n✅ Lesson 6 Complete!")
print("Next: Making API Requests")
