import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()

        area = data["nearest_area"][0]["areaName"][0]["value"]
        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]

        print(f"\nWeather in {area}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {desc}\n")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except (KeyError, IndexError) as e:
        print("Error parsing weather data. Maybe the city name is incorrect.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
