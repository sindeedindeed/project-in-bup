import requests

def get_weather(location):
    api_key = 'c6ac3f52b81b568b315c17ae2175e1ba' 
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()

    if data['cod'] == 200: #200 means API request was successful
        main = data['main']
        weather = data['weather'][0]
        print(f"Weather in {location}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    location = input("Enter the location: ")
    get_weather(location)
