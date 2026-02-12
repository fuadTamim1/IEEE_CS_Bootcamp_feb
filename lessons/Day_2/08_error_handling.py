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


def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"Result: {result}")
        
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")
        
    except TypeError:
        print("Error: Please enter valid numbers.")

safe_division(10, 2)  # Successful run
safe_division(5, 0)   # Triggers ZeroDivisionError
safe_division(10, "a") # Triggers TypeError





import logging

# Setup basic logging to record errors (as mentioned in 'Error Reporting and Logging')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data_file(filename):
    file_handler = None
    try:
        # Attempt to open the file in read mode
        file_handler = open(filename, 'r')
        data = file_handler.read()
        
        # Simulate processing data
        if not data:
            raise ValueError("The file is empty.")
            
        print(f"Successfully processed {len(data)} characters from '{filename}'.")
        return data

    except FileNotFoundError:
        # Handles the specific case where the file doesn't exist
        print(f"Error: The file '{filename}' was not found.")
        logging.error(f"FileNotFoundError: '{filename}' missing.")
        
    except PermissionError:
        # Handles cases where the user doesn't have read permissions
        print(f"Error: Permission denied for file '{filename}'.")
        logging.error(f"PermissionError: Access denied to '{filename}'.")

    except ValueError as e:
        # Catches our custom error for empty files
        print(f"Data Error: {e}")
        
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected Error: {e}")
        
    finally:
        # This block ALWAYS runs, regardless of error or success
        # It is crucial for 'cleanup' tasks
        if file_handler:
            file_handler.close()
            print("Cleanup: File stream closed.")

# Testing the function
process_data_file("non_existent_file.txt")