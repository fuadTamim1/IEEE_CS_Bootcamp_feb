"""
DAY 1 - LESSON 3: Loops
=======================

Learning Objectives:
- Understand for and while loops
- Learn the range() function
- Practice iteration patterns
"""

print("=== LOOPS ===\n")

# For loop with range
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# For loop with list
print("\nIterating over a list:")
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop
print("\nWhile loop - Counting down:")
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blastoff!")

# Multiplication table
print("\nMultiplication table for 5:")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

# Sum numbers
total = 0
for num in range(1, 6):
    total = total + num
print(f"\nSum of 1 to 5: {total}")

print("\n✅ Lesson 3 Complete!")
