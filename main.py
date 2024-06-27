import requests

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = 'your_api_key_here'  # Replace with your actual OpenWeatherMap API key
    get_weather(city, api_key)
