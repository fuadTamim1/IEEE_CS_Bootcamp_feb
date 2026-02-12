"""
DAY 2 - LESSON 5: File Handling
================================

Learning Objectives:
- Learn how to read files
- Learn how to write files
- Understand file operations
- Learn best practices (with open)
- Explore file modes, cursor control, and file management
"""

print("=== FILE HANDLING ===\n")

# --------------------------------------------------
# 1️⃣ Writing to a file (Overwrite mode - "w")
# --------------------------------------------------
file = open("sample.txt", "w")
file.write("Hello, World!\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.close()

print("✅ File written successfully!")

# --------------------------------------------------
# 2️⃣ Reading full file content
# --------------------------------------------------
file = open("sample.txt", "r")
content = file.read()
print(f"\nFile content:\n{content}")
file.close()

# --------------------------------------------------
# 3️⃣ Reading line by line
# --------------------------------------------------
print("Reading line by line:")

file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()

# --------------------------------------------------
# 4️⃣ Appending to a file ("a")
# --------------------------------------------------
file = open("sample.txt", "a")
file.write("This is an appended line\n")
file.close()

print("\n✅ Line appended successfully!")

# --------------------------------------------------
# 5️⃣ Using 'with open' (Best Practice)
# Automatically closes file
# --------------------------------------------------
with open("sample2.txt", "w") as file:
    file.write("Using with statement\n")
    file.write("File closes automatically\n")

print("\n✅ Written using 'with open'")

# --------------------------------------------------
# 6️⃣ readlines() → returns list of lines
# --------------------------------------------------
with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nReadlines output:")
print(lines)

# --------------------------------------------------
# 7️⃣ readline() → read one line at a time
# --------------------------------------------------
with open("sample.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

print("\nFirst line:", first_line.strip())
print("Second line:", second_line.strip())

# --------------------------------------------------
# 8️⃣ File Modes Reference
# --------------------------------------------------
"""
File Modes:
r  -> Read
w  -> Write (overwrite)
a  -> Append
x  -> Create new file (error if exists)
rb -> Read binary
wb -> Write binary
"""

# Example of "x" mode
try:
    with open("newfile.txt", "x") as file:
        file.write("Created using x mode")
    print("\n✅ newfile.txt created!")
except FileExistsError:
    print("\n⚠️ newfile.txt already exists!")

# --------------------------------------------------
# 9️⃣ File Information
# --------------------------------------------------
with open("sample.txt", "r") as file:
    print("\nFile Info:")
    print("Name:", file.name)
    print("Mode:", file.mode)
    print("Closed?:", file.closed)

# --------------------------------------------------
# 🔟 File Cursor Control (seek & tell)
# --------------------------------------------------
with open("sample.txt", "r") as file:
    print("\nFirst 5 characters:", file.read(5))
    print("Cursor position:", file.tell())

    file.seek(0)
    print("After seek →", file.read(5))

# --------------------------------------------------
# 1️⃣1️⃣ Write Multiple Lines
# --------------------------------------------------
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]

with open("multi.txt", "w") as file:
    file.writelines(lines_to_write)

print("\n✅ Multiple lines written!")

# --------------------------------------------------
# 1️⃣2️⃣ Copy File Content
# --------------------------------------------------
with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("✅ File copied successfully!")

# --------------------------------------------------
# 1️⃣3️⃣ Check if File Exists
# --------------------------------------------------
import os

if os.path.exists("sample.txt"):
    print("\n✅ sample.txt exists")
else:
    print("\n❌ sample.txt not found")

# --------------------------------------------------
# 1️⃣4️⃣ Delete a File
# --------------------------------------------------
if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("🗑️ File deleted")
else:
    print("No file to delete")

# --------------------------------------------------
print("\n✅ Lesson 5 Complete!")
