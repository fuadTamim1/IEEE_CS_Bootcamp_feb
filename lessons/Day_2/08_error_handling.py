"""
DAY 2 - LESSON 8: Error Handling
=================================

Learning Objectives:
- Learn try/except blocks
- Understand error types
- Practice debugging
"""

print("=== ERROR HANDLING ===\n")

# Basic try-except
print("Example 1: Dividing by zero")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

# Multiple exceptions
print("\nExample 2: File not found")
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("❌ File not found!")
except Exception as e:
    print(f"❌ Error: {e}")

# Try-except-else
print("\nExample 3: Try-except-else")
try:
    num = int("42")
except ValueError:
    print("❌ Invalid number format")
else:
    print(f"✅ Successfully converted: {num}")

# Type conversion error
print("\nExample 4: Type conversion")
try:
    value = int("hello")
except ValueError:
    print("❌ Cannot convert string to integer")

# Finally block
print("\nExample 5: Finally block")
try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("❌ File not found")
finally:
    print("✅ Cleanup complete")

print("\n✅ Lesson 8 Complete!")
