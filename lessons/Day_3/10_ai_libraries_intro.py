"""
DAY 3 - LESSON 10: AI Libraries Intro
======================================

Learning Objectives:
- Understand AI library basics
- Learn where to use each library
- Prepare for advanced topics
"""

print("=== AI LIBRARIES INTRO ===\n")

print("🤖 Key AI/Automation Libraries for Python:\n")

libraries = {
    "NumPy": "Numerical computing and array operations",
    "Pandas": "Data manipulation and analysis",
    "scikit-learn": "Machine learning algorithms",
    "Requests": "HTTP requests and APIs",
    "os": "Operating system interactions",
    "json": "JSON data handling",
    "csv": "CSV file processing",
    "time/schedule": "Task scheduling",
}

for lib, description in libraries.items():
    print(f"📚 {lib:15} - {description}")

print("\n\n📊 Use cases in automation:\n")

use_cases = {
    "File Organization": "os + time libraries",
    "Data Processing": "Pandas + CSV",
    "Machine Learning": "scikit-learn + NumPy",
    "API Integration": "Requests + JSON",
    "Scheduled Tasks": "schedule library"
}

for use, tools in use_cases.items():
    print(f"  {use:20} → {tools}")

print("\n\n🎓 Your learning path:\n")
print("  Week 1: Python basics + automation patterns")
print("  Week 2: Linux & system interaction (os module)")
print("  Week 3: Web technologies & APIs")
print("  Advanced: Specialized AI/ML libraries")

print("\n✅ Lesson 10 Complete!")
print("🎉 You've completed all Day 3 lessons!")
