"""
DAY 2 - LESSON 5: File Handling
================================

Learning Objectives:
- Learn how to read files
- Learn how to write files
- Understand file operations
"""

print("=== FILE HANDLING ===\n")

# Writing to a file
file = open("sample.txt", "w")
file.write("Hello, World!\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.close()
print("✅ File written successfully!")

# Reading from a file
file = open("sample.txt", "r")
content = file.read()
print(f"\nFile content:\n{content}")
file.close()

# Reading line by line
print("Reading line by line:")
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Appending to a file
file = open("sample.txt", "a")
file.write("This is an appended line\n")
file.close()
print("\n✅ Line appended successfully!")

print("\n✅ Lesson 5 Complete!")
