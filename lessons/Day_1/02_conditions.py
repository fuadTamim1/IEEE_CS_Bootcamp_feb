"""
DAY 1 - LESSON 2: Conditions (If/Else)
========================================

Learning Objectives:
- Understand conditional logic
- Learn if/elif/else statements
- Work with comparison and logical operators
"""

print("=== CONDITIONS ===\n")

# Simple if statement
age = 20
if age >= 18:
    print("You are an adult!")

# if-else
score = 45
if score >= 50:
    print("You passed!")
else:
    print("You need to study more.")

# if-elif-else
grade = 75
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
print(f"\n5 > 3: {5 > 3}")
print(f"10 == 10: {10 == 10}")
print(f"7 != 7: {7 != 7}")

# Logical operators
x = 15
if x > 10 and x < 20:
    print("x is between 10 and 20")

if x < 5 or x > 100:
    print("x is small or large")
else:
    print("x is in the middle range")

print("\n✅ Lesson 2 Complete!")
