# Movie Manager - Partial Solution (With Hints) 🐍
# ---------------------------------------------
# This file is NOT a complete solution.
# It contains guidance + hints to help you finish the task.

import requests
import json

API_KEY = "bd4afefa"
BASE_URL = "https://www.omdbapi.com/"
FILE_NAME = "movie_data.json"


# ---------------------------------------------
# Hint 1: Get Movie Name from User
# ---------------------------------------------

movie_name = input("Enter Movie Name: ").strip()

# Hint:
# Check if the input is empty.
# If empty → print error message and stop execution.


# ---------------------------------------------
# Hint 2: Call the API
# ---------------------------------------------

params = {
    "apikey": API_KEY,
    "t": movie_name
}

try:
    response = requests.get(BASE_URL, params=params)

    # Hint:
    # Check status code (200)
    # Then convert response to JSON

    data = response.json()

    # Hint:
    # If data["Response"] == "False"
    # → Movie not found → stop program

except requests.exceptions.RequestException:
    print("Error: مشكلة بالاتصال بالإنترنت")
    data = None


# ---------------------------------------------
# Hint 3: Extract Required Fields
# ---------------------------------------------

if data and data.get("Response") != "False":

    movie_info = {
        "Title": data.get("Title"),
        "Year": data.get("Year"),
        "IMDB Rating": data.get("imdbRating")
    }

    print("\nMovie Info:")
    for key, value in movie_info.items():
        print(f"{key}: {value}")


    # ---------------------------------------------
    # Hint 4: Save to JSON File
    # ---------------------------------------------

    try:
        # Hint:
        # 1) Try reading existing file
        # 2) Load JSON data
        # 3) Append new movie
        # 4) Write back to file

        with open(FILE_NAME, "w") as file:
            json.dump(movie_info, file, indent=4)

        print("\nMovie saved successfully ✅")

    except Exception as e:
        print("Error while saving:", e)


# ---------------------------------------------
# Extra Challenges (Optional) 💡
# ---------------------------------------------
# 1) Add Plot field
# 2) Allow multiple movies saving
# 3) Prevent duplicates
# 4) Add delete movie feature
# 5) Convert program to Functions Menu
# ---------------------------------------------