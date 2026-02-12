"""
DAY 2 - LESSON 7: API Requests
==============================

Learning Objectives:
- Learn how to make API requests
- Understand JSON responses
- Practice working with external data
- Work with GET, POST, query params, headers
"""

print("=== API REQUESTS ===\n")

# Note: Install requests library with: pip install requests

try:
    import requests

    # --------------------------------------------------
    # 1️⃣ Simple GET request (single user)
    # --------------------------------------------------
    print("Making API request to JSONPlaceholder (single user)...")
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

    # --------------------------------------------------
    # 2️⃣ GET multiple users
    # --------------------------------------------------
    print("\nFetching all users...")
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    print(f"Total users fetched: {len(users)}")

    # Print first 3 users
    print("First 3 users:")
    for user in users[:3]:
        print(f"- {user['name']} ({user['email']})")

    # --------------------------------------------------
    # 3️⃣ GET with query parameters
    # --------------------------------------------------
    print("\nFetching posts by userId=1...")
    params = {"userId": 1}
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    posts = response.json()
    print(f"Number of posts by user 1: {len(posts)}")
    print("Titles of first 3 posts:")
    for post in posts[:3]:
        print(f"- {post['title']}")

    # --------------------------------------------------
    # 4️⃣ POST request (create new resource)
    # --------------------------------------------------
    print("\nCreating a new post with POST request...")
    new_post = {
        "title": "My new post",
        "body": "This is a test post created via API",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    if response.status_code == 201:
        created_post = response.json()
        print("✅ Post created!")
        print(f"Post ID: {created_post['id']}")
    else:
        print(f"❌ Failed to create post: {response.status_code}")

    # --------------------------------------------------
    # 5️⃣ Handling headers
    # --------------------------------------------------
    print("\nExample: GET request with custom headers...")
    headers = {"User-Agent": "Python API Client"}
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", headers=headers)
    print(f"Status: {response.status_code}")

    # --------------------------------------------------
    # 6️⃣ Save API response to JSON file
    # --------------------------------------------------
    print("\nSaving all users to users.json...")
    with open("users.json", "w") as f:
        import json
        json.dump(users, f, indent=4)
    print("✅ Saved successfully!")

    # --------------------------------------------------
    # 7️⃣ Error handling & exceptions
    # --------------------------------------------------
    try:
        print("\nFetching from a wrong URL to trigger error...")
        response = requests.get("https://jsonplaceholder.typicode.com/invalidendpoint")
        response.raise_for_status()  # raises HTTPError for bad status
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")

except ImportError:
    print("⚠️ requests library not installed")
    print("Install it with: pip install requests")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n✅ Lesson 7 Complete!")
