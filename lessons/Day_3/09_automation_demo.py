"""
DAY 3 - LESSON 9: Automation Demo
==================================

Learning Objectives:
- See practical automation examples
- Understand real-world use cases
- Practice combining concepts
"""

import os
from datetime import datetime

print("=== AUTOMATION DEMO ===\n")

# Example 1: Simple File Organizer Preview
print("Example 1: List files in a directory")
current_dir = "."
files = os.listdir(current_dir)
python_files = [f for f in files if f.endswith(".py")]
print(f"Python files found: {len(python_files)}")
for f in python_files[:3]:
    print(f"  - {f}")

# Example 2: Batch rename preview
print("\n\nExample 2: How to rename multiple files")
print("Code pattern for batch renaming:")
print("""
for file in files:
    if file.endswith(".txt"):
        old_name = file
        new_name = f"processed_{file}"
        os.rename(old_name, new_name)
""")

# Example 3: Summary report
print("\nExample 3: Generating a summary report")
summary = {
    "Total files processed": 42,
    "Files organized": 38,
    "Errors": 0,
    "Time taken": "2.3 seconds"
}

for key, value in summary.items():
    print(f"  {key}: {value}")

print("\n✅ Lesson 9 Complete!")
