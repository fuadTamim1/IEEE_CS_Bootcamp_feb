# Movie Manager - Full Solution
# ---------------------------------------------

import requests
import json

API_KEY = "bd4afefa"
BASE_URL = "https://www.omdbapi.com/"
FILE_NAME = "movie_data.json"

movie_name = input("Enter Movie Name: ")

try:
    if movie_name is "":
        raise ValueError("The movie name input is empty!")
    
    response = requests.get(f"{BASE_URL}?apikey=bd4afefa&t={movie_name}")

    if(response.status_code != 200):
        raise ValueError("There Is No Response")
    data = response.json()

except ValueError as e:
    print(f"Error: {e}")
    data = None

except requests.exceptions.RequestException:
    print("Error: Internet connection error")
    data = None


movie_info = {
    "Title": data["Title"],
    "Year": data["Year"],
    "IMDB Rating": data["imdbRating"]
}

try:
    with open(FILE_NAME, "w") as file:
        json.dump(movie_info, file, indent=4)
    print("Movie saved successfully!")

except Exception as e:
    print("Error while saving:", e)