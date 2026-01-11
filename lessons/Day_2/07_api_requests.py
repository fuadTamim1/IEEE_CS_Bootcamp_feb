"""
DAY 2 - LESSON 7: API Requests
==============================

Learning Objectives:
- Learn how to make API requests
- Understand JSON responses
- Practice working with external data
"""

print("=== API REQUESTS ===\n")

# Note: Install requests library with: pip install requests

try:
    import requests
    
    print("Making API request to JSONPlaceholder...")
    
    # Simple API call
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    if response.status_code == 200:
        print("✅ Request successful!")
        user = response.json()
        print(f"\nUser data:")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Company: {user['company']['name']}")
    else:
        print(f"❌ Request failed with status {response.status_code}")
        
except ImportError:
    print("⚠️ requests library not installed")
    print("Install it with: pip install requests")
except Exception as e:
    print(f"Error: {e}")

print("\n✅ Lesson 7 Complete!")
