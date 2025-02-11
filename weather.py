import requests

def get_weather(city):
    """
    Fetches weather data for the specified city.
    """
    api_key = "0cbce788f0bdef30e73a41a212f7b560"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        # Send the GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON data
        data = response.json()
        
        # Extract relevant information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed_mps = data['wind']['speed']
        wind_speed_mph = wind_speed_mps * 2.237  # Convert m/s to mph
        
        # Return the weather data as a dictionary
        return {
            'city': city,
            'weather': weather.capitalize(),
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed_mph
        }
        
    except requests.exceptions.RequestException as e:
        return {'error': f"Error fetching weather data: {e}"}
    except KeyError:
        return {'error': "Could not retrieve weather information. Please check the city name or try again."}

if __name__ == "__main__":
    city_name = input("Enter the name of the city: ")
    weather = get_weather(city_name)
    if 'error' in weather:
        print(weather['error'])
    else:
        print(f"Weather in {weather['city']}:")
        print(f"Condition: {weather['weather']}")
        print(f"Temperature: {weather['temperature']}°F")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']:.2f} mph")