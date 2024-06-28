import random
import requests

# You would need to replace 'YOUR_API_KEY' with an actual Google Maps API key
API_KEY = 'YOUR_API_KEY'

# A list of tuples containing coordinates and country names
LOCATIONS = [
    ((48.8566, 2.3522), "France"),
    ((40.7128, -74.0060), "USA"),
    ((35.6762, 139.6503), "Japan"),
    ((-33.8688, 151.2093), "Australia"),
    ((51.5074, -0.1278), "UK")
]

def get_map_url(lat, lon):
    return f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=5&size=400x400&key={API_KEY}"

def play_game():
    score = 0
    total_rounds = 5

    for round in range(total_rounds):
        location = random.choice(LOCATIONS)
        coordinates, country = location

        print(f"\nRound {round + 1}")
        print(f"Coordinates: {coordinates}")
        
        # In a real implementation, you would display the map image here
        map_url = get_map_url(coordinates[0], coordinates[1])
        print(f"Map URL: {map_url}")

        guess = input("Guess the country: ").strip().lower()

        if guess == country.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer was {country}")

    print(f"\nGame over! Your score: {score}/{total_rounds}")

if __name__ == "__main__":
    play_game()