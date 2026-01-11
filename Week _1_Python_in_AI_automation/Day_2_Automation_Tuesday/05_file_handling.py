"""
DAY 2 - LESSON 5: File Handling and Operations
============================================

Learning Objectives:
- Understand how to read files
- Learn how to write to files
- Learn about file modes (read, write, append)
- Understand file paths and the 'with' statement
- Practice working with text files

Key Concepts:
- File modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write)
- open() function: Opens a file
- read() / write() / readlines(): Methods to work with files
- with statement: Automatically closes files
- File paths: Absolute and relative paths
"""

# ===== SECTION 1: Reading Files =====
print("=== READING FILES ===\n")

# Method 1: Read entire file at once
# Assumes a file 'example.txt' exists
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Note: example.txt not found. Creating demo instead...")

# Method 2: Read line by line
print("\nReading line by line:")
try:
    with open('example.txt', 'r') as file:
        for line in file:
            print(f"Line: {line.strip()}")
except FileNotFoundError:
    print("Note: example.txt not found")

# Method 3: Read all lines into a list
print("\nReading all lines into a list:")
try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Note: example.txt not found")


# ===== SECTION 2: Creating and Writing Files =====
print("\n=== WRITING FILES ===\n")

# Create and write to a file
filename = "my_first_file.txt"

with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is my first file in Python.\n")
    file.write("Python is awesome!\n")

print(f"✓ Created '{filename}'")

# Read back what we wrote
with open(filename, 'r') as file:
    content = file.read()
    print(f"Content of '{filename}':")
    print(content)


# ===== SECTION 3: Appending to Files =====
print("\n=== APPENDING TO FILES ===\n")

# Append (add to end) without overwriting
filename = "notes.txt"

# Create initial file
with open(filename, 'w') as file:
    file.write("Monday: Started Python\n")

print(f"Initial content of '{filename}':")
with open(filename, 'r') as file:
    print(file.read())

# Append new content
with open(filename, 'a') as file:
    file.write("Tuesday: Learned functions\n")
    file.write("Wednesday: Started automation\n")

print(f"After appending:")
with open(filename, 'r') as file:
    print(file.read())


# ===== SECTION 4: Working with File Content =====
print("\n=== PROCESSING FILE CONTENT ===\n")

# Create a file with numbers
filename = "numbers.txt"
with open(filename, 'w') as file:
    for i in range(1, 6):
        file.write(f"{i}\n")

# Read and process the numbers
with open(filename, 'r') as file:
    total = 0
    count = 0
    for line in file:
        number = int(line.strip())
        total += number
        count += 1

print(f"Sum of numbers: {total}")
print(f"Count: {count}")
print(f"Average: {total / count}")


# ===== SECTION 5: Counting Words and Characters =====
print("\n=== TEXT ANALYSIS ===\n")

# Create a sample file
filename = "sample.txt"
with open(filename, 'w') as file:
    file.write("Python is a powerful programming language. Python is used in AI and automation.")

# Analyze the file
with open(filename, 'r') as file:
    content = file.read()

word_count = len(content.split())
char_count = len(content)
line_count = len(content.split('\n'))

print(f"File: {filename}")
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Lines: {line_count}")

# Count specific word
word_to_find = "Python"
count = content.lower().count(word_to_find.lower())
print(f"Count of '{word_to_find}': {count}")


# ===== SECTION 6: File Processing - Search and Filter =====
print("\n=== SEARCH AND FILTER ===\n")

# Create a sample data file
filename = "students.txt"
with open(filename, 'w') as file:
    file.write("Ahmed 95\n")
    file.write("Sara 88\n")
    file.write("Ali 92\n")
    file.write("Fatima 85\n")
    file.write("Omar 90\n")

# Find students with score > 90
print(f"Students with score > 90:")
with open(filename, 'r') as file:
    for line in file:
        name, score = line.strip().split()
        score = int(score)
        if score > 90:
            print(f"  {name}: {score}")


# ===== SECTION 7: Writing Summary Report =====
print("\n=== GENERATING REPORTS ===\n")

# Create summary report from data
input_file = "students.txt"
output_file = "report.txt"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write("=== STUDENT SCORES REPORT ===\n\n")
    
    total = 0
    count = 0
    highest = 0
    lowest = 100
    
    for line in infile:
        name, score = line.strip().split()
        score = int(score)
        
        outfile.write(f"{name}: {score}/100\n")
        
        total += score
        count += 1
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    outfile.write(f"\n--- SUMMARY ---\n")
    outfile.write(f"Total students: {count}\n")
    outfile.write(f"Average score: {total / count:.2f}\n")
    outfile.write(f"Highest score: {highest}\n")
    outfile.write(f"Lowest score: {lowest}\n")

print(f"✓ Report created: {output_file}")
print("\nReport content:")
with open(output_file, 'r') as file:
    print(file.read())


# ===== SECTION 8: File Path Handling =====
print("\n=== FILE PATH HANDLING ===\n")

import os

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in current directory
print(f"\nFiles in current directory:")
files = os.listdir('.')
for file in files[:5]:  # Show first 5 files
    if os.path.isfile(file):
        print(f"  - {file}")

# Check if file exists
filename = "my_first_file.txt"
if os.path.exists(filename):
    print(f"\n✓ {filename} exists")
    file_size = os.path.getsize(filename)
    print(f"  Size: {file_size} bytes")
else:
    print(f"\n✗ {filename} does not exist")


# ===== SECTION 9: Common File Operations =====
print("\n=== COMMON FILE OPERATIONS ===\n")

# Copy content from one file to another
source = "my_first_file.txt"
destination = "backup.txt"

if os.path.exists(source):
    with open(source, 'r') as infile:
        content = infile.read()
    
    with open(destination, 'w') as outfile:
        outfile.write(content)
    
    print(f"✓ Copied {source} to {destination}")

# Delete a file (commented out for safety)
# os.remove("temp.txt")

# Rename a file (commented out for safety)
# os.rename("old_name.txt", "new_name.txt")


# ===== SECTION 10: Practice - Log File Analyzer =====
print("\n=== PRACTICE: LOG FILE ANALYZER ===\n")

# Create a sample log file
log_file = "app.log"
with open(log_file, 'w') as file:
    file.write("INFO: Application started\n")
    file.write("DEBUG: Connecting to database\n")
    file.write("ERROR: Connection timeout\n")
    file.write("INFO: Retrying connection\n")
    file.write("INFO: Connection established\n")
    file.write("WARNING: Memory usage high\n")
    file.write("INFO: Operation completed\n")

# Analyze the log
print(f"Analyzing {log_file}:")

with open(log_file, 'r') as file:
    errors = 0
    warnings = 0
    infos = 0
    
    print("\nLog entries:")
    for line in file:
        line = line.strip()
        if line:
            print(f"  {line}")
            
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1
            elif "INFO" in line:
                infos += 1

print(f"\nSummary:")
print(f"  INFO entries: {infos}")
print(f"  WARNING entries: {warnings}")
print(f"  ERROR entries: {errors}")


# ===== SECTION 11: Exception Handling with Files =====
print("\n=== ERROR HANDLING WITH FILES ===\n")

# Method 1: Checking if file exists
def read_file_safely(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        return "File not found!"

result = read_file_safely("nonexistent.txt")
print(f"Result: {result}")

# Method 2: Using try-except (covered in next lesson)
print("\nNote: Exception handling for files will be covered in Lesson 8")


print("\n✅ Lesson 5 Complete!")
print("Next: JSON and CSV Data Formats")
